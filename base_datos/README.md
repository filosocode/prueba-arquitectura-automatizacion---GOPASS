# 📂 Módulo: base_datos

Este módulo simula operaciones básicas con una base de datos PostgreSQL utilizando Docker y Python.

---

## ¿Qué hace este módulo?

- Levanta una base de datos PostgreSQL usando Docker.
- Crea una tabla llamada `usuarios`.
- Inserta 3 usuarios ficticios automáticamente al iniciar.
- Ejecuta un script Python que:
  - Inserta un nuevo usuario si no existe.
  - Consulta los usuarios registrados en los últimos 7 días.
  - Muestra los resultados organizados en formato tabla por consola.

---

## Requisitos

- Tener Docker y Docker Compose instalados.
- Tener Python 3.10 o superior.
- Tener pip instalado (para instalar librerías).

---

## ¿Cómo usarlo paso a paso?

### 1. Ir a la carpeta del módulo

```bash
cd base_datos
```

### 2. Levantar la base de datos PostgreSQL con Docker

Este comando descargará la imagen de PostgreSQL y levantará el servicio.

```bash
docker-compose up -d
```

### 3. Instalar la dependencia de Python (`psycopg2-binary`)

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el script Python

```bash
python insertar_y_listar.py
```

Esto mostrará algo como:

```
Usuario 'Andres Muñoz' insertado.

Usuarios registrados en los últimos 7 días:

ID   Nombre                              Correo                        Fecha registro
------------------------------------------------------------------------------------------
1    Juan Pérez                          juan@example.com              2025-07-07 10:00:00
2    María Gómez                         maria@example.com             2025-07-07 10:00:00
3    Carlos Rodríguez                    carlos@example.com            2025-07-07 10:00:00
4    Andres Muñoz                        aemunoz@gopass.com            2025-07-07 10:05:00
```

> Si el usuario ya existe, se muestra un mensaje de que no se volverá a insertar.

---

## ¿Cómo reiniciar la base de datos desde cero?

Si deseas eliminar todos los datos y recrear la base limpia:

```bash
docker-compose down -v
docker-compose up -d
```

Esto volverá a ejecutar el script `init.sql` y restaurará los 3 usuarios base.

---

## Nota técnica

- El script está desarrollado con Programación Orientada a Objetos (POO).
- El archivo `insertar_y_listar.py` contiene validación para evitar insertar correos duplicados.
- Toda la lógica está estructurada de forma clara y modular.
