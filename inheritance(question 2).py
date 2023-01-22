class dog:
      def __init__(self,name,age,coatcolour,sound,height):
          self.name=name
          self.age=age
          self.coatcolour=coatcolour
          self.sound=sound
          self.height=height
print("dog initalized!")
def description(self):
     return f"{self.name} is {self.age} years old"
def get_info(self,coatcolour):
     self.coatcolour=coatcolour
     print("dog.coatcolour")
class jackrussellterrier(dog):
     def speak(self,sound="arf"):
          return f"{self.name} says {sound}"
     def height(self,height="14 inches"):
          return f"{self.name} says {height}"
class bulldog(dog):
          def speak(self,sound="snoring"):
               return f"{self.name} says {sound}"
          def height(self,height="9 inches"):
               return f"{self.name} says {height}"
          x=dog()
          print(x.name())
          print(x.age())
          print(x.coatcolour())
          print(x.sound())
          print(x.height())
          print()