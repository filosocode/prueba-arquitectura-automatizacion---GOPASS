CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    fecha_registro TIMESTAMP DEFAULT NOW()
);

INSERT INTO usuarios (nombre, correo) VALUES
('Andres Muñoz', 'aemunoz@gopass.com'),
('Kevin Antonio Herrera Acosta', 'kvhacosta@gopass.com'),
('Juan David Garcia', 'jdgarcia@gopass.com');
