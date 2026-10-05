import cv2

# Cargar la imagen
imagen = cv2.imread("aguila.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    3
)

# Mostrar imágenes
cv2.imshow("Imagen original 0087", imagen)
cv2.imshow("Imagen con filtro de mediana 0087", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "../resultados/aguila_mediana.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/aguila_mediana.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()