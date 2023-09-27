# ---------------------------------------------- #
# Métodos númericos
# Entregable 1 - Interpolación de imágenes
# ---------------------------------------------- #
# Código Interpolación de imágenes con la función
# de Newton
# ---------------------------------------------- #
# - Miguel Angel Vélez
# - Alejandro García
# ---------------------------------------------- #
# ------------------ Librerías ----------------- #
from functools import reduce

# ------------------ Función de Newton ----------------- #

def newton(x, points):
  '''
  Es una función que genera un polinomio según los puntos
  recibidos como parámetros y realiza una interpolación
  evaluada en el punto x.
  
  Parameters
  ----------
  x : float
      El punto x en el que se evaluará el polinomio.
      
  points : list
      Es un arreglo con los puntos con los que se realizará
      la interpolación.
      
  Returns
  -------
  newton_pol : float
      Es el valor del polinomio resuelto y evaluado en el punto x.
  '''
  last_divided = []

  for count in range(len(points) - 1):
    divided_length = len(last_divided)
    new_points = points if divided_length == 0 else last_divided[divided_length - 1]
    last_divided.append(diff_divided(new_points, points, count + 1))
      
  indexes = list(map(lambda index: index[0][1], last_divided))
  newton_pol = points[0][1]

  for index in range(len(indexes)):
    newton_pol = newton_pol + indexes[index] * get_polynomial(x, points, index)
  
  return newton_pol

# ------------------ Utilidades ----------------- #

def diff_divided(points, original_points, count = 1):
  fn = lambda fxi, fxj, xi, xj: (fxi - fxj) / (xi - xj)
  divided_values = []
  amount_points = len(points)

  if amount_points == 1:
    return divided_values

  for index in range(amount_points - 1):
    divided_values.append([
      points[index][0],
        fn(
          points[index][1],
          points[index + 1][1],
          original_points[index][0],
          original_points[index + count][0]
        )])

  return divided_values

def get_polynomial(x, points, potent):
  return 1 if potent == -1 else (x - points[potent][0]) * get_polynomial(x, points, potent - 1)
