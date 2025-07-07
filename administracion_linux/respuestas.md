# Respuestas - Administración Linux

**1. Ver los 5 procesos que más memoria consumen:**
Este comando lista los procesos ordenados por uso de memoria en orden descendente, y muestra los 5 primeros (más el encabezado).

```bash
ps aux --sort=-%mem | head -n 6
```

**2. Agregar un nuevo usuario al sistema:**
Este comando crea un nuevo usuario con su propio directorio home, contraseña y configuración por defecto.

```bash
sudo adduser andres_muñoz_gopass
```

**3. Cambiar los permisos de un archivo para que solo el dueño pueda leer y escribir**
Este comando otorga permisos rw------- (lectura y escritura solo para el dueño).

```bash
chmod 600 archivo.txt
```

**4. Ver el estado del servidor ssh:**
Este comando muestra si el servicio ssh está activo, habilitado o detenido.

```bash
systemctl status ssh
```
