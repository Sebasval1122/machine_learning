class ErrorValoresIngresadosPorcentajes(Exception):
    def __init__(self, porcentaje_precio_real, tasa_de_interes_mensual):
        super().__init__(f"El valor de los porcentajes de la vivienda y la tasa de interes son invalidos. Los Valores del porcentaje de la vivienda ({porcentaje_precio_real}) y/o ({tasa_de_interes_mensual}) no pueden ser negativos. Vuelvalo a intentar con valores positivos")

class ErrorEdadIncorrecta(Exception):
    def __init__(self, edad):
        super().__init__(f"El valor de la edad del cliente no es válida. La edad ingresada ({edad}) es incorrecta. Vuelvalo a intentar teniendo en cuenta que la edad minima para la hipoteca inversa es 65")

class ErrorCuotas(Exception):
    def __init__(self, total_cuotas):
        super().__init__(f"El valor de las cuotas no es válido. El numero de cuotas ({total_cuotas}) es incorrecta. Vuelvalo a intentar sabiendo que el numero de cuotas no puede ser negativo o igual que 0, sepa que el valor debe ser mayor que 0")

class ErrorEdadnegativa(Exception):
    def __init__(self, edad):
        super().__init__(f"La edad ingresada no puede ser negativa. La edad ingresada ({edad}) es incorrecta. Vuelvalo a intentar teniendo en cuenta que la edad no debe ser negativa")

class Hipoteca:
    def __init__(self, edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual):
        self.edad = edad
        self.precio_de_la_vivienda = precio_de_la_vivienda
        self.porcentaje_precio_real = porcentaje_precio_real
        self.total_cuotas = total_cuotas
        self.tasa_de_interes_mensual = tasa_de_interes_mensual
        self.validar_datos()

    def validar_datos(self):
        """
        Valida los datos ingresados para la hipoteca.
        Raises exceptions if any of the input values are invalid.
        """
        if self.edad < 0:
            # La edad no puede ser negativa.
            raise ErrorEdadnegativa(self.edad)
        
        if self.edad < 65:
            # La edad mínima para la hipoteca inversa es 65.
            raise ErrorEdadIncorrecta(self.edad)
        
        if self.total_cuotas <= 0:
            # El número de cuotas debe ser mayor que 0.
            raise ErrorCuotas(self.total_cuotas)
        
        if self.porcentaje_precio_real < 0 or self.tasa_de_interes_mensual < 0:
            # Los porcentajes y la tasa de interés no pueden ser negativos.
            raise ErrorValoresIngresadosPorcentajes(self.porcentaje_precio_real, self.tasa_de_interes_mensual)

    def calcular_ingreso_mensual(self):
        """
        Calcula el ingreso mensual basado en los datos de la hipoteca.
        Returns the monthly income.
        """
        self.validar_datos()

        porcentaje_precio_real_porcentual = self.porcentaje_precio_real / 100
        valor_de_la_hipoteca = self.precio_de_la_vivienda * porcentaje_precio_real_porcentual
        ingreso_mensual = valor_de_la_hipoteca / self.total_cuotas

        if self.porcentaje_precio_real == 100:
            # Si el porcentaje del precio real es 100, el ingreso mensual es 0.
            ingreso_mensual = 0

        if self.total_cuotas == 1:
            # Si solo hay una cuota, el ingreso mensual es igual al valor de la hipoteca.
            ingreso_mensual = valor_de_la_hipoteca
        else:
            ingreso_mensual = valor_de_la_hipoteca / self.total_cuotas

        return ingreso_mensual

    def calcular_deuda_total(self, ingreso_mensual):
        """
        Calcula la deuda total basada en el ingreso mensual y la tasa de interés.
        Returns the total debt.
        """
        if self.total_cuotas <= 0:
            # El número de cuotas debe ser mayor que 0.
            raise ErrorCuotas(self.total_cuotas)
        
        if self.tasa_de_interes_mensual < 0:
            # La tasa de interés no puede ser negativa.
            raise ErrorValoresIngresadosPorcentajes(self.porcentaje_precio_real, self.tasa_de_interes_mensual)

        tasa_de_interes_mensual_decimal = self.tasa_de_interes_mensual / 100
        
        if self.tasa_de_interes_mensual == 0:
            # Si la tasa de interés es 0, la deuda total es el ingreso mensual multiplicado por el número de cuotas.
            saldo = ingreso_mensual * self.total_cuotas
            return saldo

        if self.total_cuotas == 1:
            # Si solo hay una cuota, la deuda total es el ingreso mensual más el interés.
            interes = ingreso_mensual * tasa_de_interes_mensual_decimal
            saldo = ingreso_mensual + interes
        else:
            saldo = 0
            for i in range(self.total_cuotas):
                saldo += ingreso_mensual
                interes = saldo * tasa_de_interes_mensual_decimal
                saldo += interes

        return saldo