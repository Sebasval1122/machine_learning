import unittest

import sys
sys.path.append("src/model")

from model import hipoteca_inversa

class PruebasHipotecaInversa(unittest.TestCase):
    """
    Clase de pruebas unitarias para la clase Hipoteca.
    Unit test class for the Hipoteca class.
    """

    # 3 Casos de Prueba Normales    
    def test_calcular_hipoteca_inversa_1(self):
        """
        Prueba el cálculo de la hipoteca inversa con valores normales.
        Tests the reverse mortgage calculation with normal values.

        Parámetros:
        - edad (int): Edad del cliente. Mínimo 65.
        - expectativa_de_vida (int): Expectativa de vida del cliente.
        - años_de_renta (int): Años de renta esperados.
        - total_cuotas (int): Número total de cuotas. Mayor que 0.
        - precio_de_la_vivienda (int): Precio de la vivienda.
        - porcentaje_precio_real (int): Porcentaje del precio real de la vivienda.
        - valor_de_la_hipoteca (int): Valor de la hipoteca.
        - tasa_de_interes_mensual (float): Tasa de interés mensual.

        Retorna: - resultado_ingreso_mensual_esperado: Float - resultado_deuda_total_esperada: Float

        Excepciones:
        - Ninguna
        """
        edad = 70
        expectativa_de_vida = 75
        años_de_renta = 5
        total_cuotas = 60
        precio_de_la_vivienda = 200_000_000
        porcentaje_precio_real = 30
        valor_de_la_hipoteca = 60_000_000
        tasa_de_interes_mensual = 10

        resultado_ingreso_mensual_esperado = 1_000_000
        resultado_deuda_total_esperada = 3_338_298_035

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Normal 1")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calcular_hipoteca_inversa_2(self):
        """
        Prueba el cálculo de la hipoteca inversa con valores normales.
        Tests the reverse mortgage calculation with normal values.

        Parámetros:
        - edad (int): Edad del cliente. Mínimo 65.
        - expectativa_de_vida (int): Expectativa de vida del cliente.
        - años_de_renta (int): Años de renta esperados.
        - total_cuotas (int): Número total de cuotas. Mayor que 0.
        - precio_de_la_vivienda (int): Precio de la vivienda.
        - porcentaje_precio_real (int): Porcentaje del precio real de la vivienda.
        - valor_de_la_hipoteca (int): Valor de la hipoteca.
        - tasa_de_interes_mensual (float): Tasa de interés mensual.

        Retorna: - resultado_ingreso_mensual_esperado - Float
                 - resultado_deuda_total_esperada - Float

        Excepciones:
        - Ninguna
        """
        edad = 75
        expectativa_de_vida = 88
        años_de_renta = 17
        total_cuotas = 156
        precio_de_la_vivienda = 412_949_945
        porcentaje_precio_real = 50
        valor_de_la_hipoteca = 206_474_973
        tasa_de_interes_mensual = 5.50

        resultado_ingreso_mensual_esperado = 1_323_558
        resultado_deuda_total_esperada = 107_625_171_318

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Normal 2")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calcular_hipoteca_inversa_3(self):
        """
        Prueba el cálculo de la hipoteca inversa con valores normales.
        Tests the reverse mortgage calculation with normal values.

        Parámetros:
        - edad (int): Edad del cliente. Mínimo 65.
        - expectativa_de_vida (int): Expectativa de vida del cliente.
        - años_de_renta (int): Años de renta esperados.
        - total_cuotas (int): Número total de cuotas. Mayor que 0.
        - precio_de_la_vivienda (int): Precio de la vivienda.
        - porcentaje_precio_real (int): Porcentaje del precio real de la vivienda.
        - valor_de_la_hipoteca (int): Valor de la hipoteca.
        - tasa_de_interes_mensual (float): Tasa de interés mensual.

        Retorna: - resultado_ingreso_mensual_esperado - Float
                 - resultado_deuda_total_esperada - Float

        Excepciones:
        - Ninguna
        """
        edad = 85
        expectativa_de_vida = 89
        años_de_renta = 4
        total_cuotas = 48
        precio_de_la_vivienda = 619_424_917
        porcentaje_precio_real = 40
        valor_de_la_hipoteca = 247_769_967
        tasa_de_interes_mensual = 4.80

        resultado_ingreso_mensual_esperado = 5_161_874
        resultado_deuda_total_esperada = 957_016_422

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Normal 3")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    # 3 Casos de Prueba Extraordinarios
    def test_calcular_hipoteca_inversa_total_cuotas_1(self):
        """
        Prueba el cálculo de la hipoteca inversa con un número mínimo de cuotas.
        Tests the reverse mortgage calculation with a minimum number of installments.

        Parámetros:
        - edad (int): Edad del cliente. Mínimo 65.
        - expectativa_de_vida (int): Expectativa de vida del cliente.
        - años_de_renta (int): Años de renta esperados.
        - total_cuotas (int): Número total de cuotas. Mayor que 0.
        - precio_de_la_vivienda (int): Precio de la vivienda.
        - porcentaje_precio_real (int): Porcentaje del precio real de la vivienda.
        - valor_de_la_hipoteca (int): Valor de la hipoteca.
        - tasa_de_interes_mensual (float): Tasa de interés mensual.

        Retorna: - resultado_ingreso_mensual_esperado - Float
                 - resultado_deuda_total_esperada - Float

        Excepciones:
        - Ninguna
        """
        edad = 70
        expectativa_de_vida = 85
        años_de_renta = 20                                       
        total_cuotas = 1
        precio_de_la_vivienda = 908_489_879
        porcentaje_precio_real = 55
        valor_de_la_hipoteca = 499_699_433
        tasa_de_interes_mensual = 1.20

        resultado_ingreso_mensual_esperado = 499_669_433
        resultado_deuda_total_esperada = 505_665_467

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Extraordinario 1")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calculos_hipoteca_inversa_tasa_de_interes_0(self):
        """
        Prueba el cálculo de la hipoteca inversa con una tasa de interés mensual de 0.
        Tests the reverse mortgage calculation with a monthly interest rate of 0.

        Parámetros:
        - edad (int): Edad del cliente. Mínimo 65.
        - expectativa_de_vida (int): Expectativa de vida del cliente.
        - años_de_renta (int): Años de renta esperados.
        - total_cuotas (int): Número total de cuotas. Mayor que 0.
        - precio_de_la_vivienda (int): Precio de la vivienda.
        - porcentaje_precio_real (int): Porcentaje del precio real de la vivienda.
        - valor_de_la_hipoteca (int): Valor de la hipoteca.
        - tasa_de_interes_mensual (float): Tasa de interés mensual.

        Retorna: - resultado_ingreso_mensual_esperado - Float
                 - resultado_deuda_total_esperada - Float

        Excepciones:
        - Ninguna
        """
        edad = 78
        expectativa_de_vida = 90
        años_de_renta = 12
        total_cuotas = 144
        precio_de_la_vivienda = 1_238_849_835
        porcentaje_precio_real = 50
        valor_de_la_hipoteca = 619_424_918
        tasa_de_interes_mensual = 0

        resultado_ingreso_mensual_esperado = 4_301_562
        resultado_deuda_total_esperada = 619_424_918

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Extraordinario 2")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calcular_hipoteca_inversa_hipoteca_porcentaje_precio_real_100(self):
        """
        Prueba el cálculo de la hipoteca inversa con un porcentaje del precio real de la vivienda del 100%.
        Tests the reverse mortgage calculation with a percentage of the real price of the house of 100%.

        Parámetros:
        - edad (int): Edad del cliente. Mínimo 65.
        - expectativa_de_vida (int): Expectativa de vida del cliente.
        - años_de_renta (int): Años de renta esperados.
        - total_cuotas (int): Número total de cuotas. Mayor que 0.
        - precio_de_la_vivienda (int): Precio de la vivienda.
        - porcentaje_precio_real (int): Porcentaje del precio real de la vivienda.
        - valor_de_la_hipoteca (int): Valor de la hipoteca.
        - tasa_de_interes_mensual (float): Tasa de interés mensual.

        Retorna: - resultado_ingreso_mensual_esperado - Float
                 - resultado_deuda_total_esperada - Float

        Excepciones:
        - Ninguna
        """
        edad = 76
        expectativa_de_vida = 88
        años_de_renta = 12
        total_cuotas = 144
        precio_de_la_vivienda = 743_309_901
        porcentaje_precio_real = 100
        valor_de_la_hipoteca = 743_309_901
        tasa_de_interes_mensual = 1.1

        resultado_ingreso_mensual_esperado = 5_161_874
        resultado_deuda_total_esperada = 1_818_198_009

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Extraordinario 3")
        print("Advertencia: La hipoteca cubre el 100% del precio de la vivienda.")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    # 4 Casos de Prueba con Errores
    def test_calcular_hipoteca_inversa_con_porcentajes_negativos(self):
        """
        Prueba el cálculo de la hipoteca inversa con porcentajes negativos.
        Tests the reverse mortgage calculation with negative percentages.

        Parámetros:
        - edad (int): Edad del cliente. Mínimo 65.
        - expectativa_de_vida (int): Expectativa de vida del cliente.
        - años_de_renta (int): Años de renta esperados.
        - total_cuotas (int): Número total de cuotas. Mayor que 0.
        - precio_de_la_vivienda (int): Precio de la vivienda.
        - porcentaje_precio_real (int): Porcentaje del precio real de la vivienda. No puede ser negativo.
        - valor_de_la_hipoteca (int): Valor de la hipoteca.
        - tasa_de_interes_mensual (float): Tasa de interés mensual. No puede ser negativa.

        Retorna:
        - None

        Excepciones:
        - hipoteca_inversa.ErrorValoresIngresadosPorcentajes: Si los porcentajes son negativos.
        """
        edad = 74
        expectativa_de_vida = 88
        años_de_renta = 14
        total_cuotas = 168
        precio_de_la_vivienda = 1_032_374_862
        porcentaje_precio_real = -5.0
        valor_de_la_hipoteca = 516_187_431
        tasa_de_interes_mensual = -2.8

        with self.assertRaises(hipoteca_inversa.ErrorValoresIngresadosPorcentajes) as comentario:
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)
        print("\nCaso de Error 1")
        print(f"Mensaje de error: El valor de los porcentajes de la vivienda y la tasa de interes son invalidos. Los Valores del porcentaje de la vivienda ({porcentaje_precio_real}) y/o ({tasa_de_interes_mensual}) no pueden ser negativos. Vuelvalo a intentar con valores positivos")

    def test_calcular_hipoteca_inversa_con_edad_invalida(self):
        """
        Prueba el cálculo de la hipoteca inversa con una edad inválida.
        Tests the reverse mortgage calculation with an invalid age.

        Parámetros:
        - edad (int): Edad del cliente. Mínimo 65.
        - expectativa_de_vida (int): Expectativa de vida del cliente.
        - años_de_renta (int): Años de renta esperados.
        - total_cuotas (int): Número total de cuotas. Mayor que 0.
        - precio_de_la_vivienda (int): Precio de la vivienda.
        - porcentaje_precio_real (int): Porcentaje del precio real de la vivienda.
        - valor_de_la_hipoteca (int): Valor de la hipoteca.
        - tasa_de_interes_mensual (float): Tasa de interés mensual.

        Retorna:
        - None

        Excepciones:
        - hipoteca_inversa.ErrorEdadIncorrecta: Si la edad es menor a 65.
        """
        edad = 50
        expectativa_de_vida = 90
        años_de_renta = 30
        total_cuotas = 360
        precio_de_la_vivienda = 825_899_890
        porcentaje_precio_real = 45
        valor_de_la_hipoteca = 371_654_951
        tasa_de_interes_mensual = 6

        with self.assertRaises(hipoteca_inversa.ErrorEdadIncorrecta) as comentario:
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)
        print("\nCaso de Error 2")
        print(f"Mensaje de error: El valor de la edad del cliente no es válida. La edad ingresada ({edad}) es incorrecta. Vuelvalo a intentar teniendo en cuenta que la edad minima para la hipoteca inversa es 65")

    def test_calcular_hipoteca_inversa_con_cuotas_invalida(self):
        """
        Prueba el cálculo de la hipoteca inversa con un número de cuotas inválido.
        Tests the reverse mortgage calculation with an invalid number of installments.

        Parámetros:
        - edad (int): Edad del cliente. Mínimo 65.
        - expectativa_de_vida (int): Expectativa de vida del cliente.
        - años_de_renta (int): Años de renta esperados.
        - total_cuotas (int): Número total de cuotas. Mayor que 0.
        - precio_de_la_vivienda (int): Precio de la vivienda.
        - porcentaje_precio_real (int): Porcentaje del precio real de la vivienda.
        - valor_de_la_hipoteca (int): Valor de la hipoteca.
        - tasa_de_interes_mensual (float): Tasa de interés mensual.

        Retorna:
        - None

        Excepciones:
        - hipoteca_inversa.ErrorCuotas: Si el número de cuotas es menor o igual a 0.
        """
        edad = 80
        expectativa_de_vida = 92
        años_de_renta = 12
        total_cuotas = 0
        precio_de_la_vivienda = 1_238_849_835
        porcentaje_precio_real = 50
        valor_de_la_hipoteca = 619_424_918
        tasa_de_interes_mensual = 5

        with self.assertRaises(hipoteca_inversa.ErrorCuotas) as comentario:
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)
        print("\nCaso de Error 3")
        print(f"Mensaje de error: El valor de las cuotas no es válido. El numero de cuotas ({total_cuotas}) es incorrecta. Vuelvalo a intentar sabiendo que el numero de cuotas no puede ser negativo o igual que 0, sepa que el valor debe ser mayor que 0")

    def test_calcular_hipoteca_inversa_con_edad_negativa(self):
        """
        Prueba el cálculo de la hipoteca inversa con una edad negativa.
        Tests the reverse mortgage calculation with a negative age.

        Parámetros:
        - edad (int): Edad del cliente. No puede ser negativa.
        - expectativa_de_vida (int): Expectativa de vida del cliente.
        - años_de_renta (int): Años de renta esperados.
        - total_cuotas (int): Número total de cuotas. Mayor que 0.
        - precio_de_la_vivienda (int): Precio de la vivienda.
        - porcentaje_precio_real (int): Porcentaje del precio real de la vivienda.
        - valor_de_la_hipoteca (int): Valor de la hipoteca.
        - tasa_de_interes_mensual (float): Tasa de interés mensual.

        Retorna:
        - None

        Excepciones:
        - hipoteca_inversa.ErrorEdadnegativa: Si la edad es negativa.
        """
        edad = -65
        expectativa_de_vida = 79
        años_de_renta = 14
        total_cuotas = 168
        precio_de_la_vivienda = 619_424_917
        porcentaje_precio_real = 40
        valor_de_la_hipoteca = 247_769_967
        tasa_de_interes_mensual = 2.3

        with self.assertRaises(hipoteca_inversa.ErrorEdadnegativa) as comentario:
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)
        print("\nCaso de Error 4")
        print(f"Mensaje de error: La edad ingresada no puede ser negativa. La edad ingresada ({edad}) es incorrecta. Vuelvalo a intentar teniendo en cuenta que la edad no debe ser negativa")

if __name__ == '__main__':
    unittest.main()