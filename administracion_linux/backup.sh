#!/bin/bash

# Script para simular un backup de /home/usuario1

# Guardar la fecha actual en formato YYYYMMDD
FECHA=$(date +%Y%m%d)

# Definir la ruta destino del respaldo
BACKUP_DIR="/backups"
DESTINO="$BACKUP_DIR/usuario1_backup_$FECHA.tar.gz"

# Ruta de origen a respaldar
ORIGEN="/home/usuario1"

# Mostrar información
echo "[INFO] Creando backup simulado de $ORIGEN en $DESTINO"

# Crear carpeta /backups si no existe (en un sistema real)
mkdir -p "$BACKUP_DIR"

# Comprimir la carpeta (en un sistema real)
tar -czf "$DESTINO" "$ORIGEN"

# Confirmar
echo "[OK] Backup generado: $DESTINO"
