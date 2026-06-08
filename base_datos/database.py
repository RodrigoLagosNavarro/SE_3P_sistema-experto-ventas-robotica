import sqlite3


def crear_base_datos():

    conexion = sqlite3.connect("base_datos/ventas.db")

    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nivel TEXT,
        presupuesto TEXT,
        proyecto TEXT,
        categoria TEXT,
        producto TEXT,
        regla TEXT
    )
    """)

    conexion.commit()
    conexion.close()


def guardar_consulta(datos_cliente, resultado):

    conexion = sqlite3.connect("base_datos/ventas.db")

    cursor = conexion.cursor()

    cursor.execute("""
    INSERT INTO consultas
    (
        nivel,
        presupuesto,
        proyecto,
        categoria,
        producto,
        regla
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datos_cliente["nivel"],
        datos_cliente["presupuesto"],
        datos_cliente["proyecto"],
        datos_cliente["categoria"],
        resultado["producto"],
        resultado["regla"]
    ))

    conexion.commit()
    conexion.close()