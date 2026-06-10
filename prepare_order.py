"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""

from util.file_manager import CSVFileManager
from util.converter import CashierConverter, CustomerConverter, ProductConverter
from orders.order import Order
from products.product import *
from users.user import *
from products.food_package import *
import os

#Ruta base del proyecto para localizar los archivos csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#Rutas de los archivos csv
cashiers_path = os.path.join(BASE_DIR, "data", "cashiers.csv")
customers_path = os.path.join(BASE_DIR, "data", "customers.csv")
drinks_path = os.path.join(BASE_DIR, "data", "drinks.csv")
sodas_path = os.path.join(BASE_DIR, "data", "sodas.csv")
hamburgers_path = os.path.join(BASE_DIR, "data", "hamburgers.csv")
happymeal_path = os.path.join(BASE_DIR, "data", "happyMeal.csv")
    
class PrepareOrder:
  def __init__(self):
        self.cashiers = []
        self.customers = []
        self.products = []


  def load_data(self):
      #Carga de todos los archivos csv utilizando la clase CSVFileManager y su método read()
      self.df_cashiers = CSVFileManager(cashiers_path).read()
      self.df_customers = CSVFileManager(customers_path).read()
      self.df_hamburgers = CSVFileManager(hamburgers_path).read()
      self.df_sodas = CSVFileManager(sodas_path).read()
      self.df_drinks = CSVFileManager(drinks_path).read()
      self.df_happymeal = CSVFileManager(happymeal_path).read()


  def convert_data(self):
      #Conversión de los Data Frames a listas de objetos utilizando las clases Converter y su método convert()
      cashier_conv = CashierConverter()
      customer_conv = CustomerConverter()
      product_conv = ProductConverter()

      #Conversión de cajeros, clientes a listas de objetos
      self.cashiers = cashier_conv.convert(self.df_cashiers)
      self.customers = customer_conv.convert(self.df_customers)
      
      #Conversión de productos a listas de objetos por cada tipo de producto
      self.products = []
      self.products += product_conv.convert(self.df_hamburgers, Hamburger)
      self.products += product_conv.convert(self.df_sodas, Soda)
      self.products += product_conv.convert(self.df_drinks, Drink)
      self.products += product_conv.convert(self.df_happymeal, HappyMeal)

  # ===== Funciones para buscar cajeros, clientes y productos por sus identificadores =====
  def find_cashier(self, dni):
      for c in self.cashiers:
          if str(c.dni) == str(dni):
              return c
      return None

  def find_customer(self, dni):
      for c in self.customers:
          if str(c.dni) == str(dni):
              return c
      return None

  def find_product(self, id):
      for p in self.products:
          if str(p.id) == str(id):
              return p
      return None
  
  # ===== Funciones para solicitar al usuario el dni del cajero, cliente y el id del producto =====        
  def ask_cashier(self):
      while True:
          dni = input("Introduce el DNI del cajero: ")
          cashier = self.find_cashier(dni)
          if cashier is not None:
              return cashier
          print("Cajero no encontrado. Intenta de nuevo.")

  def ask_customer(self):
      while True:
          dni = input("Introduce el DNI del cliente: ")
          customer = self.find_customer(dni)
          if customer is not None:
              return customer
          print("Cliente no encontrado. Intenta de nuevo.")

  def ask_product(self):
      while True:
          id = input("Introduce el ID del producto: ")
          product = self.find_product(id)
          if product is not None:
              return product
          print("Producto no encontrado. Intenta de nuevo.")
        
  # ===== Función para crear la orden, mostrar los productos disponibles y solicitar al usuario que agregue productos a la orden =====
  def create_order(self):
      cashier = self.ask_cashier()
      customer = self.ask_customer()

      order = Order(cashier, customer)

      while True:
          print("\nProductos disponibles:")
          for p in self.products:
              print(p.describe())

          product = self.ask_product()

          order.add(product)

          more = input("¿Deseas agregar otro producto? (s/n): ")
          if more.lower() != 's':
              break
      
      return order
  
  # ===== Función principal para ejecutar la aplicación =====
  def run(self):
      self.load_data()
      self.convert_data()

      order = self.create_order()

      print("\n=====ORDEN FINALIZADA=====")
      order.show()

# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = PrepareOrder()
    app.run()