# 📂 Módulo: automatizacion_archivos

Este módulo automatiza la creación de un archivo de reporte con información sobre todos los archivos `.txt` presentes en la misma carpeta.

---

## ¿Qué hace este script?

- Revisa los archivos `.txt` que se encuentren en esta misma carpeta.
- Cuenta cuántas líneas tiene cada archivo.
- Genera un archivo de reporte con la fecha del día en la carpeta `reportes/`.

### Ejemplo de salida

Si tienes estos archivos:

```
ejemplo1.txt  (1 línea)
ejemplo2.txt  (3 líneas)
ejemplo3.txt  (0 líneas)
```

El script generará un archivo como:

```
reportes/reporte_20250707.txt
```

Con este contenido:

```
ejemplo1.txt: 1 líneas
ejemplo2.txt: 3 líneas
ejemplo3.txt: 0 líneas

Total de archivos procesados: 3
```

Si no hay ningún archivo `.txt`, el archivo de reporte dirá:

```
No se encontraron archivos de texto.
```

---

## ¿Cómo usarlo?

1. Abre una terminal y ubícate en esta carpeta:

```bash
cd automatizacion_archivos
```

2. Asegúrate de tener archivos `.txt` en esta carpeta.
   Puedes crear algunos con:

```bash
echo "Línea 1" > ejemplo1.txt
echo -e "Linea 1\nLinea 2\nLinea 3" > ejemplo2.txt
```

3. Ejecuta el script:

```bash
python generar_reporte.py
```

4. Verifica que se haya creado la carpeta `reportes/` y dentro el archivo `reporte_YYYYMMDD.txt`.

---

## Nota técnica

El script está desarrollado en Python 3 y estructurado en Programación Orientada a Objetos (POO) para facilitar su mantenimiento y extensión futura.

No requiere ninguna librería externa.
