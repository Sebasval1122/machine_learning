import sys
sys.path.append("src/model")
from model import hipoteca_inversa

#Se añade la consola, la cual pide los datos y calcula la deuda esperada y el ingreso mensual esperado

try:
    edad = int(input("Ingrese la edad del cliente: "))
    expectativa_de_vida = int(input("Ingrese la expectativa de vida del cliente: "))
    años_de_renta = int(input("Ingrese los años de renta del cliente: "))
    total_cuotas = int(input("Ingrese el total de cuotas: "))
    precio_de_la_vivienda = float(input("Ingrese el precio de la vivienda: "))
    porcentaje_precio_real = float(input("Ingrese el porcentaje del precio real a pagar de la vivienda: ")) 
    valor_de_la_hipoteca = float(input("Ingrese el valor de la hipoteca: "))
    tasa_de_interes_mensual = float(input("Ingrese la tasa de interés mensual: ")) 

    hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

    resultado_ingreso_mensual_esperado = hipoteca.calcular_ingreso_mensual()
    resultado_deuda_total_esperada = hipoteca.calcular_deuda_total()

    print(f"Ingreso mensual esperado: {resultado_ingreso_mensual_esperado}")
    print(f"Deuda total esperada: {resultado_deuda_total_esperada}")

except Exception as excepcion_de_error:
    print("Hubo un error en los datos ingresados:")
    print(str(excepcion_de_error))