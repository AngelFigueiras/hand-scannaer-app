import cv2
import numpy as np

def calcular_similitud_M(imagen, lineas_palma, imagen_M):
  """
  Esta función calcula la similitud entre las líneas de la palma de la mano y una letra M predefinida.

  Parámetros:
    imagen: La imagen con las líneas de la palma de la mano dibujadas.
    lineas_palma: Una lista con las coordenadas de las líneas de la palma de la mano.
    imagen_M: La imagen con la letra M predefinida.

  Retorno:
    Un porcentaje de similitud entre las líneas de la palma y la letra M predefinida.
  """

  # Extraer las líneas de la palma
  linea_vida = lineas_palma[0]
  linea_cabeza = lineas_palma[1]

  # Calcular la altura y anchura de la palma
  altura_palma = linea_vida[1][1] - linea_vida[0][1]
  anchura_palma = linea_cabeza[1][0] - linea_cabeza[0][0]

  # Redimensionar la imagen M para que coincida con la palma
  imagen_M_redim = cv2.resize(imagen_M, (anchura_palma, altura_palma))

  # Calcular la correlación entre las imágenes
  correlacion = cv2.matchTemplate(imagen, imagen_M_redim, cv2.TM_CCOEFF_NORMED)

  # Encontrar el punto máximo de correlación
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(correlacion)

  # Calcular el porcentaje de similitud
  similitud = max_val * 100


  return similitud
