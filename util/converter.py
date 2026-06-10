from abc import ABC, abstractmethod
#Importamos las clases necesarias para la conversión
from users import Cashier, Customer
from products import Hamburger, Soda, Drink, HappyMeal

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

#========= CONVERSOR DE CAJEROS ==========
class CashierConverter(Converter):
  def convert(self,dataFrame):    
    cashiers = []
    #Recorremos el DataFrame fila por fila y creamos un objeto Cashier con los datos de cada fila
    for index, row in dataFrame.iterrows():
      cashier = Cashier(
        row['dni'], 
        row['name'], 
        row['age'], 
        row['timetable'], 
        row['salary'])
      cashiers.append(cashier)
    return cashiers

#========= CONVERSOR DE CLIENTES ==========
class CustomerConverter(Converter):
  def convert(self,dataFrame):
    customers = []
    #Recorremos el DataFrame fila por fila y creamos un objeto Customer con los datos de cada fila
    for index, row in dataFrame.iterrows():
      customer = Customer(
        row['dni'], 
        row['name'], 
        row['age'], 
        row['email'], 
        row['postalcode'])
      customers.append(customer)
    return customers

#========= CONVERSOR DE PRODUCTOS ==========
class ProductConverter(Converter):
  def convert(self,dataFrame, product_class):
    products = []
    #Recorremos el DataFrame fila por fila y creamos un objeto del tipo product_class con los datos de cada fila
    for index, row in dataFrame.iterrows():
      product = product_class(
        row['id'],
        row['name'],
        row['price']
      )
      products.append(product)
    return products
