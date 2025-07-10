import sqlite3

conexion = sqlite3.connect("medicamentos.db")
cursor = conexion.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS medicamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    componentes TEXT,
    uso TEXT,
    presentacion TEXT
)
''')

medicamentos = [
    ("Dolo-Ibu", "ibuprofeno", "dolor muscular", "tableta"),
    ("Tempra", "paracetamol", "fiebre", "jarabe"),
    ("Panadol", "paracetamol", "dolor leve", "tableta"),
    ("Ibupirac", "ibuprofeno", "inflamación", "cápsula"),
]

cursor.executemany('''
INSERT INTO medicamentos (nombre, componentes, uso, presentacion)
VALUES (?, ?, ?, ?)
''', medicamentos)

conexion.commit()
conexion.close()
print("Datos cargados correctamente.")
