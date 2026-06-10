from abc import ABC, abstractmethod

class FoodPackage (ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    

#Embalaje utilizado para hamburguesas:    
class Wrapping(FoodPackage):  
  def pack(self):
     return "Food Wrap Paper"
  def material(self):
     return "Aluminium"
  
#Embalaje para bebidas embotelladas:
class Bottle(FoodPackage):  
  def pack(self):
     return "Bottle"
  def material(self):
     return "Plastic"

#Embalaje para productos delicados:
class Glass(FoodPackage):  
  def pack(self):
     return "Glass"
  def material(self):
     return "Cardboard"

#Embalaje para productos en caja:
class Box(FoodPackage):  
  def pack(self):
     return "Box"
  def material(self):
     return "Cardboard"
  