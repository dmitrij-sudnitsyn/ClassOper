# Задание 1
# Создайте класс Circle (окружность). Для данного
# класса реализуйте ряд перегруженных операторов:
# ■■Проверка на равенство радиусов двух окружностей (операция = =);
# ■■Сравнения длин двух окружностей (операции >, <,
# <=,>=);
# Длина окружности l=2πr
# ■■Пропорциональное изменение размеров окружности,
# путем изменения ее радиуса (операции + - += -=).
def is_number(str):
      try:
       float(str)  
       return True
      except ValueError:
       print("Переменная {str} не численного типа")  
       return False


class Circle:
   def __init__(self,r):
      if is_number(r):
       self.r=r
       self.l=2*3.14*r
      else:
       print(f"переменная {r} не числового типа")   

   def __set__(self,r):
      if is_number(r):
       self.r=r
       self.l=2*3.14*r
      else:
       print(f"переменная {r} не числового типа")   

   def setR(self,r):
      if is_number(r):      
       self.r = r
       self.l =2*3.14*r       
      else:
       print(f"переменная {r} не числового типа")   

   def getR(self):
      return self.r

   def getL(self):
      return self.l

   def __str__(self):
     return f'Радиус окружности = {self.r} Длина окружности {self.l}\n'

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
       self.l=2*3.14*self.r
       return self
      except ValueError:
       print(f"  {a} тип значения не соответсвует типу операции ")     

# __sub__(self, other) - вычитание (x - y).
   def __sub__(self,a):
      try:
       if self.r-a <0:
        print(f" {self.r-a} Радиус и длина не может быть отрицательной - ")
       else: 
        return Circle(self.r-a)
      except ValueError:
       print(f"  {a} тип значения не соответсвует типу операции ")     


# __isub__(self, other) - -=.
   def __isub__(self,a):
      try:
       if self.r-a <0:
        print(f" {self.r-a} Радиус и длина не может быть отрицательной - ")
       else:  
        self.r-=a  
        self.l=2*3.14*self.r
        return self
      except ValueError:
       print(f"  {a} тип значения не соответсвует типу операции ")     

# Вам необходимо создать класс Airplane (самолет). С помощью перегрузки операторов реализовать:
# ■■Проверка на равенство типов самолетов (операция = =);
# ■■Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# ■■Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > < <= >=).

class Airplane:
  def __init__(self,TypeAirplane,MaxKolPass,KolPass) -> None:
    self.TypeAirplane =TypeAirplane
    self.MaxKolPass      =MaxKolPass
    self.KolPass      =KolPass


  def __str__(self) -> str:
    return f'Самолет типа {self.TypeAirplane} количество пассажирова {self.KolPass} при максимально возможном количестве пассажиров {self.MaxKolPass}'

  def __set__(self,TypeAirplane,MaxKolPass,KolPass):
    self.TypeAirplane = TypeAirplane
    self.MaxKolPass   = MaxKolPass
    self.KolPass      = KolPass
  
  def getTypeAirplane(self):
   return self.TypeAirplane

  def getMaxKolPass(self):
   return self.MaxKolPass

  def getKolPass(self):
   return self.KolPass

  def setTypeAirplane(self,a):
    self.TypeAirplane=a

  def setMaxKolPass(self,a):
   if is_number(a):
    if a>=0:  
     self.MaxKolPass  =a
    else:
     print("Количество не может быть меньше 0. Неможет быть отрицательным")  
   else:
    print("Количество должно быть целочисленое")   

  def setKolPass(self,a):
   if is_number(a):
    if a>=0:  
     if self.MaxKolPass>=a: 
      self.KolPass  =a
     else:
      print(f"Количество пассажиров не может быть больше максимально возможного количества пассажиров {self.MaxKolPass}") 
    else:
     print("Количество не может быть меньше 0. Неможет быть отрицательным")  
   else:
    print("Количество должно быть целочисленое")   
  
  def is_MaxKolPass(self,a):
    if is_number(a):
     if self.MaxKolPass>=self.KolPass+a:
      return True
     else:
      print(f"Количество пассажиров не может быть больше максимально возможного количества пассажиров {self.MaxKolPass}")
      return False  

# Проверка на равенство типов самолетов (операция = =);
# Тут проверить как сравниваются типы в Python
  # __eq__(self, other) - x == y вызывает x.__eq__(y).
  def __eq__(self,other) -> bool:
   return self.TypeAirplane==other.TypeAirplane

# __ne__(self, other) - x != y вызывает x.__ne__(y)
#   def __ne__(self,other):
#     return self.MaxKolPass!=other.MaxKolPass     


# Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);   
# __add__(self, other) - сложение. x + y вызывает x.__add__(y).
  def __add__(self,a):
    if self.is_MaxKolPass(a):
     self.KolPass=self.KolPass+a
     return Airplane(self)
# __iadd__(self, other) - +=.
  def __iadd__(self,a):
   if self.is_MaxKolPass(a):
      self.KolPass+=a  
      return self

# __sub__(self, other) - вычитание (x - y).
  def __sub__(self,a):
    if self.is_MaxKolPass(a):
       self.KolPass=self.KolPass-a
       return Airplane(self)

# __isub__(self, other) - -=.
  def __isub__(self,a):
    if self.is_MaxKolPass(a):
       self.KolPass-=a  
       return self

# Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > < <= >=).
# __lt__(self, other) - x < y вызывает x.__lt__(y).
  def __lt__(self,other):
     return self.MaxKolPass<=other.MaxKolPass

# __le__(self, other) - x ≤ y вызывает x.__le__(y).
  def __le__(self,other):
     return self.MaxKolPass<=other.MaxKolPass

# __gt__(self, other) - x > y вызывает x.__gt__(y).
  def __gt__(self,other):
     return self.MaxKolPass>other.MaxKolPass      

# __ge__(self, other) - x ≥ y вызывает x.__ge__(y).      
  def __ge__(self,other):
     return self.MaxKolPass>=other.MaxKolPass      


# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# ■■Проверка на равенство площадей квартир (операция==);
# ■■Проверка на неравенство площадей квартир (операция !=);
# ■■Сравнение двух квартир по цене (операции > < <= >=).
class Flat:
   def __init__(self,square,price):
      if is_number(square):
         self.square = square
      if is_number(price):
         self.price = price

   def set(self,square,price):
      if is_number(square):
         self.square = square
      if is_number(price):
         self.price = price

   def getsquare(self):
      return self.square 

   def getprice(self):
      return self.price


   def setSquare(self,a):
     if is_number(a):   
        self.square= a

   def setPrice(self,a):
     if is_number(a):   
        self.price= a
   
   def __str__(self) -> str:
     return f"Площадь квартиры {self.square} ее цена {self.price}"


# Проверка на равенство площадей квартир (операция==);

  # __eq__(self, other) - x == y вызывает x.__eq__(y).
   def __eq__(self,other) -> bool:
    return self.square==other.square     


# ■■Проверка на неравенство площадей квартир (операция !=);
# __ne__(self, other) - x != y вызывает x.__ne__(y)
   def __ne__(self,other):
     return self.square!=other.square     


# Сравнение двух квартир по цене (операции > < <= >=).
# __lt__(self, other) - x < y вызывает x.__lt__(y).
   def __lt__(self,other):
     return self.price<=other.price

# __le__(self, other) - x ≤ y вызывает x.__le__(y).
   def __le__(self,other):
     return self.price<=other.price

# __gt__(self, other) - x > y вызывает x.__gt__(y).
   def __gt__(self,other):
     return self.price>other.price      

# __ge__(self, other) - x ≥ y вызывает x.__ge__(y).      
   def __ge__(self,other):
     return self.price>=other.price



