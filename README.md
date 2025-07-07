# Prueba Técnica: Especialista en Arquitectura y Automatización

Este repositorio contiene la solución completa a una prueba técnica compuesta por tres módulos:

- 📂 `automatizacion_archivos/` → Automatización de manejo de archivos `.txt` con Python
- 📂 `base_datos/` → Interacción con base de datos PostgreSQL usando Docker y Python
- 📂 `administracion_linux/` → Comandos de administración Linux y simulación de backup con Docker

---

## 📁 Estructura del proyecto

```
prueba-arquitectura-automatizacion/
├── automatizacion_archivos/
├── base_datos/
├── administracion_linux/
├── .gitignore
└── README.md
```

---

## ✅ Requisitos generales

- Python 3.10 o superior
- Docker + Docker Compose
- Git

---

## Cómo correr cada módulo

### 📂 `automatizacion_archivos/`

Automatiza la generación de un archivo de reporte con los nombres y cantidad de líneas de archivos `.txt`.

```bash
cd automatizacion_archivos
python generar_reporte.py
```

> Resultado: se genera `reportes/reporte_YYYYMMDD.txt` con el detalle de los `.txt` en la misma carpeta.

---

### 📂 `base_datos/`

Simula operaciones básicas con PostgreSQL y Python.

#### 1. Levantar la base de datos con Docker:

```bash
cd base_datos
docker-compose up -d
```

#### 2. Instalar dependencias:

```bash
pip install -r base_datos/requirements.txt
```

#### 3. Ejecutar el script Python:

```bash
python base_datos/insertar_y_listar.py
```

> Resultado: se inserta un usuario si no existe y se listan los usuarios registrados en los últimos 7 días, formateados en consola.

---

### 📂 `administracion_linux/`

Contiene:

- `respuestas.md` → respuestas documentadas a comandos básicos de administración Linux.
- `backup.sh` → script que simula un respaldo comprimido (`.tar.gz`) de `/home/usuario1` a `/backups/`.

#### Simular en entorno real con Docker:

```bash
cd administracion_linux
docker-compose run linux
```

Ya dentro del contenedor:

```bash
apt update && apt install -y tar
mkdir -p /home/usuario1
echo "archivo de prueba" > /home/usuario1/archivo.txt
chmod +x backup.sh
./backup.sh
```

> Resultado: genera un archivo `usuario1_backup_<fecha>.tar.gz` en `/backups`.

---

## Consideraciones

- Cada módulo está organizado y documentado de forma independiente.
- Todos los procesos fueron probados y pueden reproducirse con Docker y Python.
- No se requiere base de datos externa ni instalación de software adicional fuera de lo documentado.

---

## 🧠 Autor

**Andrés Muñoz**  
📞 3138717169  
📧 91andresmunoz@gmail.com
