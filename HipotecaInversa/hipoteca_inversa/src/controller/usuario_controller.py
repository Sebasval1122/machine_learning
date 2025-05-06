import sys
sys.path.append( "src" )

import psycopg2

from model.usuario import Usuario
import SecretConfig

class ControladorUsuario:
    def crear_tabla():
        cursor=ControladorUsuario.ObtenerCursor()
        cursor.execute("""CREATE TABLE usuario (
    id INT PRIMARY KEY ,
    edad INT NOT NULL,
    expectativa_vida INT NOT NULL,
    anos_renta INT NOT NULL,
    total_cuotas INT NOT NULL,
    precio_vivienda DECIMAL(15,2) NOT NULL,
    porcentaje_precio_real DECIMAL(5,2) NOT NULL,  
    valor_hipoteca DECIMAL(15,2) NOT NULL,
    ingreso_mensual DECIMAL(15,2) NOT NULL,
    tasa_interes_mensual DECIMAL(5,4) NOT NULL     
);""")
    def eliminar_tabla():
        cursor = ControladorUsuario.ObtenerCursor()

        cursor.execute("""drop table usuarios""" )
        cursor.connection.commit()

    def ObtenerCursor():
        """ Crea la conexion a la base de datos y retorna un cursor para hacer consultas """
        connection = psycopg2.connect(database=SecretConfig.PGDATABASE, user=SecretConfig.PGUSER, password=SecretConfig.PGPASSWORD, host=SecretConfig.PGHOST, port=SecretConfig.PGPORT)
        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        return cursor