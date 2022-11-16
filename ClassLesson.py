# Задание 1
# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■■Проверка на равенство радиусов двух окружностей (операция = =);
# ■■Сравнения длин двух окружностей (операции >, <,
# <=,>=);
# Длина окружности l=2πr
# ■■Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).
class Circle:
   def is_number(self,str):
      try:
       float(str)  
       return True
      except ValueError:
       print("Переменная {str} не численного типа")  
       return False

   def __init__(self,r):
      if self.is_number(r):
       self.r=r
       self.l=2*3.14*r
      else:
       print(f"переменная {r} не числового типа")   

   def set(self,r):
      if self.is_number(r):
       self.r=r
       self.l=2*3.14*r
      else:
       print(f"переменная {r} не числового типа")   

   def setR(self,r):
      if self.is_number(r):      
       self.r = r
       self.l =2*3.14*r       
      else:
       print(f"переменная {r} не числового типа")   

   def getR(self):
      return self.r

   def getL(self):
      return self.l

   def __str__(self):
     return f'Радиус окружности = {self.r} Длина окружности {2*3.14*self.r}\n'

# Проверка на равенство радиусов двух окружностей (операция = =);
# __eq__(self, other) - x == y вызывает x.__eq__(y).
   def __eq__(self, other):
      return self.r==other.r

# Сравнения длин двух окружностей (операции >, <,<=,>=);

# __lt__(self, other) - x < y вызывает x.__lt__(y).
   def __lt__(self,other):
     return self.l<=other.l

# __le__(self, other) - x ≤ y вызывает x.__le__(y).
   def __le__(self,other):
     return self.l<=other.l

# __ne__(self, other) - x != y вызывает x.__ne__(y)
   def __ne__(self,other):
    return self.l!=other.l      

# __gt__(self, other) - x > y вызывает x.__gt__(y).
   def __gt__(self,other):
     return self.l>other.l      

# __ge__(self, other) - x ≥ y вызывает x.__ge__(y).      
   def __ge__(self,other):
     return self.l>=other.l      


# Пропорциональное изменение размеров окружности, путем изменения ее радиуса (операции + - += -=).


# __add__(self, other) - сложение. x + y вызывает x.__add__(y).
   def __add__(self,a):
      try:
       return Circle(self.r+a)
      except ValueError:
       print(f"  {a} тип значения не соответсвует типу операции ")     

# __iadd__(self, other) - +=.
   def __iadd__(self,a):
      try:
       self.r+=a  
       return self
      except TypeError:
       print(f"  {a} тип значения не соответсвует типу операции ")     

       
      
# __sub__(self, other) - вычитание (x - y).
   def __sub__(self,a):
      try:
       return Circle(self.r-a)
      except TypeError:
       print(f"  {a} тип значения не соответсвует типу операции ")     


# __isub__(self, other) - -=.
   def __isub__(self,a):
      try:
       self.r-=a  
       return self
      except TypeError:
       print(f"  {a} тип значения не соответсвует типу операции ")     

