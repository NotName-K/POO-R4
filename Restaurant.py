import math

class MenuItem:
    def __init__(self, nombre, precio, cantidad):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters y Setters
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, value):
        self.__nombre = value

    def get_precio(self):
        return self.__precio
    def set_precio(self, value):
        self.__precio = value

    def get_cantidad(self):
        return self.__cantidad
    def set_cantidad(self, value):
        self.__cantidad = value

    def clc_precio(self):
        return self.__precio * self.__cantidad


class Bebidas(MenuItem):
    def __init__(self, nombre, precio, cantidad, tipo):
        super().__init__(nombre, precio, cantidad)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    def set_tipo(self, value):
        self.__tipo = value

    def aplicar_descuento_hora_feliz(self):
        self.set_precio(self.get_precio() * 0.8)


class Desayunos(MenuItem):
    def __init__(self, nombre, precio, cantidad, incluye_bebida):
        super().__init__(nombre, precio, cantidad)
        self.__incluye_bebida = incluye_bebida

    def get_incluye_bebida(self):
        return self.__incluye_bebida
    def set_incluye_bebida(self, value):
        self.__incluye_bebida = value

    def es_combo(self):
        return self.__incluye_bebida


class Entradas(MenuItem):
    def __init__(self, nombre, precio, cantidad, tamaño):
        super().__init__(nombre, precio, cantidad)
        self.__tamaño = tamaño

    def get_tamaño(self):
        return self.__tamaño
    def set_tamaño(self, value):
        self.__tamaño = value

    def porcion_extra(self):
        self.set_cantidad(self.get_cantidad() + 1)


class Infantil(MenuItem):
    def __init__(self, nombre, precio, cantidad, incluye_juguete):
        super().__init__(nombre, precio, cantidad)
        self.__incluye_juguete = incluye_juguete

    def get_incluye_juguete(self):
        return self.__incluye_juguete
    def set_incluye_juguete(self, value):
        self.__incluye_juguete = value

    def regalo(self):
        return "Juguete sorpresa" if self.__incluye_juguete else "Sin juguete"


class Vegetarianos(MenuItem):
    def __init__(self, nombre, precio, cantidad, vegano):
        super().__init__(nombre, precio, cantidad)
        self.__vegano = vegano

    def get_vegano(self):
        return self.__vegano
    def set_vegano(self, value):
        self.__vegano = value

    def es_apto_para_veganos(self):
        return self.__vegano


class Pescados(MenuItem):
    def __init__(self, nombre, precio, cantidad, tipo_pescado):
        super().__init__(nombre, precio, cantidad)
        self.__tipo_pescado = tipo_pescado

    def get_tipo_pescado(self):
        return self.__tipo_pescado
    def set_tipo_pescado(self, value):
        self.__tipo_pescado = value

    def es_marisco(self):
        return self.__tipo_pescado.lower() in ["camarón", "langosta", "pulpo"]


class Sopas(MenuItem):
    def __init__(self, nombre, precio, cantidad, tipo_sopa):
        super().__init__(nombre, precio, cantidad)
        self.__tipo_sopa = tipo_sopa

    def get_tipo_sopa(self):
        return self.__tipo_sopa
    def set_tipo_sopa(self, value):
        self.__tipo_sopa = value

    def se_sirve_caliente(self):
        return self.__tipo_sopa.lower() != "fría"


class Carnes(MenuItem):
    def __init__(self, nombre, precio, cantidad, termino):
        super().__init__(nombre, precio, cantidad)
        self.__termino = termino

    def get_termino(self):
        return self.__termino
    def set_termino(self, value):
        self.__termino = value

    def cambiar_termino(self, nuevo_termino):
        self.set_termino(nuevo_termino)



class Order:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def calculate_total_price(self):
        total = 0
        tiene_principal = any(isinstance(i, (Carnes, Pescados)) for i in self.items)

        for item in self.items:
            subtotal = item.clc_precio()


            if item.get_cantidad() > 3:
                subtotal *= 0.95


            if tiene_principal and isinstance(item, Bebidas):
                subtotal *= 0.9 

            total += subtotal


        if total > 50000:
            total *= 0.85

        return total



class Payment:
    def __init__(self):
        pass

    def pay(self, amount):
        raise NotImplementedError(".")


class CardPayment(Payment):
    def __init__(self, number, cvv):
        super().__init__()
        self.__number = number
        self.__cvv = cvv

    def get_number(self):
        return self.__number
    def set_number(self, value):
        self.__number = value

    def pay(self, amount):
        print(f"Pagando ${amount:.2f} con tarjeta terminada en {self.__number[-4:]}")


class CashPayment(Payment):
    def __init__(self, money_given):
        super().__init__()
        self.__money_given = money_given

    def get_money_given(self):
        return self.__money_given
    def set_money_given(self, value):
        self.__money_given = value

    def pay(self, amount):
        if self.__money_given >= amount:
            cambio = self.__money_given - amount
            print(f"Pago en efectivo completado. Cambio: ${cambio:.2f}")
        else:
            print(f"Fondos insuficientes. Faltan ${amount - self.__money_given:.2f}")


if __name__ == "__main__":
    orden = Order()
    orden.agregar_item(Bebidas("Jugo de naranja", 3000, 2, "natural"))
    orden.agregar_item(Carnes("Churrasco", 25000, 1, "Término medio"))
    orden.agregar_item(Entradas("Pan de ajo", 4000, 2, "Mediana"))

    total = orden.calculate_total_price()
    print(f"Total de la orden: ${round(total, 2)}")


    pago = CardPayment("1234567812345678", 123)
    pago.pay(total)


    pago2 = CashPayment(40000)
    pago2.pay(total)
