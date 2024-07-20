#!/bin/bash

# URL de la página web a validar
URL="https://proofof-concept.azurewebsites.net"

# Usar curl para obtener el status code
status_code=$(curl -o /dev/null -s -w "%{http_code}\n" "$URL")

# Imprimir el status code
echo "El status code de la página web $URL es: $status_code"

# Opcional: Comprobar si el status code es 200 (OK)
if [ "$status_code" -eq 200 ]; then
  echo "La página web está disponible."
else
  echo "La página web no está disponible. Status code: $status_code"
  exit 1  # Salir con código de error si la página no está disponible
fi
