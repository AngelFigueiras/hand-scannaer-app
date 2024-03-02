import cv2
import numpy as np

def detectar_lineas_palma(imagen):
  """
  Esta función detecta las líneas principales de la palma de la mano en una imagen.

  Parámetros:
    imagen: La imagen en la que se desea detectar las líneas.

  Retorno:
    Una imagen con las líneas de la palma de la mano dibujadas.
  """

  # Convertir la imagen a escala de grises
  gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

  # Aplicar un filtro de suavizado
  gris = cv2.GaussianBlur(gris, (5, 5), 0)

  # Binarizar la imagen
  umbral = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

  # Encontrar los contornos de la mano
  contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Seleccionar el contorno de la mano más grande
  mano = max(contornos, key=cv2.contourArea)

  # Encontrar los puntos de la palma
  puntos_palma = cv2.convexHull(mano, returnPoints=True)

  # Dibujar las líneas de la palma
  lineas = []

  # Línea de la vida
  lineas.append((puntos_palma[0], puntos_palma[len(puntos_palma) // 2]))

  # Línea de la cabeza
  lineas.append((puntos_palma[len(puntos_palma) // 4], puntos_palma[3 * len(puntos_palma) // 4]))

  # Línea del corazón
  lineas.append((puntos_palma[len(puntos_palma) // 5], puntos_palma[4 * len(puntos_palma) // 5]))

  for linea in lineas:
    cv2.line(imagen, linea[0], linea[1], (0, 255, 0), 2)

  return imagen
