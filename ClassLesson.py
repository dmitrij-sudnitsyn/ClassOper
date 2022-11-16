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
   def __init__(self,r):
      self.r=r
      self.l=2*3.14*r

   def set(self,r):
       self.r = r
       self.l=2*3.14*r

   def setR(self,r):
       self.r = r

   def setL(self,r):
       self.l =2*3.14*r

   def getR(self):
      return self.r

   def getL(self):
      return self.l

   def __str__(self):
     return f'Радиус окружности = {self.r} Длина окружности {2*3.14*self.r}\n'

# __lt__(self, other) - x < y вызывает x.__lt__(y).
   def __lt__(self,other):
     return 2*3.14*self.r<=2*3.14*other.r      

# __le__(self, other) - x ≤ y вызывает x.__le__(y).
   def __le__(self,other):
     return 2*3.14*self.r<=2*3.14*other.r

# Проверка на равенство радиусов двух окружностей (операция = =);
# __eq__(self, other) - x == y вызывает x.__eq__(y).
   def __eq__(self, other):
      return self.r==other.r

# __ne__(self, other) - x != y вызывает x.__ne__(y)
   def __ne__(self,other):
    return self.l!=other.l      

# __gt__(self, other) - x > y вызывает x.__gt__(y).
   def __gt__(self,other):
     return self.l>other.l      

# __ge__(self, other) - x ≥ y вызывает x.__ge__(y).      
   def __ge__(self,other):
     return self.l>=other.l      

