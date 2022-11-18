from ClassLesson import *
def testCircle():
 myCircle =Circle(50)
 print(myCircle)
 myCircle.set(15)
 myCircle2=Circle(30)
 if myCircle<myCircle2:
   print(f"Длина окружности {myCircle.getL()} меньше длины окружности {myCircle2.getL()}") 
 myCircle.set(30)   
 if myCircle==myCircle2:
   print(f"Длина окружности {myCircle.getL()} равна длины окружности {myCircle2.getL()}") 
 myCircle.set(40)   
 if myCircle>=myCircle2:
   print(f"Длина окружности {myCircle.getL()} больше длины окружности {myCircle2.getL()}") 

 myCircle=myCircle+10
 print(myCircle)
 # myCircle=myCircle+50
 # print(myCircle)

 myCircle+=10
 print(myCircle)
 # myCircle=myCircle-10
 # print(myCircle)
 myCircle-=10
 print(myCircle)

 myCircle-=10
 print(myCircle)

 myCircle-=60
 print(myCircle)

def testAirplane():
  myAirplane01=Airplane("Грузовой",250,150)
  myAirplane02=Airplane("Пассажирский",150,50)
  print("*"*100)
  print(myAirplane01)
  print(myAirplane02)
  print("*"*100)
# ■■Проверка на равенство типов самолетов (операция = =);
  if myAirplane01==myAirplane02:
   print(f" Это однотипные самолеты")
  myAirplane01.setTypeAirplane("Пассажирский") 
  print("*"*100)
  print(myAirplane01)
  print(myAirplane02)
  print("*"*100)
  if myAirplane01==myAirplane02:
   print(f" Это однотипные самолеты")
 
# ■■Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
  myAirplane01=myAirplane01+50
  print(myAirplane01)
  myAirplane01+=50
  print(myAirplane01)

  myAirplane01=myAirplane01-50
  print(myAirplane01)

  myAirplane01-=50
  print(myAirplane01)  


# ■■Сравнение двух самолетов по максимально возможному количеству пассажиров на борту (операции > < <= >=).
  myAirplane01.setMaxKolPass(250)
  if myAirplane01>myAirplane02:
    print(f" Самолет типа {myAirplane01.TypeAirplane} по максимальному количеству пассажиров {myAirplane01.MaxKolPass} больще чем самолет типа {myAirplane02.TypeAirplane} у него  {myAirplane02.MaxKolPass}") 

  myAirplane01.setMaxKolPass(150) 
  if myAirplane01>=myAirplane02:
    print(f" Самолет типа {myAirplane01.TypeAirplane} по максимальному количеству пассажиров {myAirplane01.MaxKolPass} больще или равен чем самолет типа {myAirplane02.TypeAirplane} у него  {myAirplane02.MaxKolPass}") 

  myAirplane01.setMaxKolPass(100) 
  if myAirplane01<myAirplane02:
    print(f" Самолет типа {myAirplane01.TypeAirplane} по максимальному количеству пассажиров {myAirplane01.MaxKolPass} меньше чем самолет типа {myAirplane02.TypeAirplane} у него  {myAirplane02.MaxKolPass}") 

  myAirplane01.setMaxKolPass(150) 
  if myAirplane01<=myAirplane02:
    print(f" Самолет типа {myAirplane01.TypeAirplane} по максимальному количеству пассажиров {myAirplane01.MaxKolPass} меньше или равен чем самолет типа {myAirplane02.TypeAirplane} у него  {myAirplane02.MaxKolPass}") 




def testFlat():
  myFlat01=Flat(35.6,30000)
  myFlat02=Flat(50.70,50000)
  print(myFlat01)
  print(myFlat02)

  if myFlat01==myFlat02:
     print(f" Площадь квартиры {myFlat01.square} равна площади квартиры {myFlat02.square}")

  if myFlat01!=myFlat02:
     print(f" Площадь квартиры {myFlat01.square} не равна площади квартиры {myFlat02.square}")

  myFlat01.setPrice(60000)
  

  if myFlat01>myFlat02:
     print(f" Цена квартиры {myFlat01.price} больше цены квартиры {myFlat02.price}")

  myFlat01.setPrice(50000)
  if myFlat01>=myFlat02:
     print(f" Цена квартиры {myFlat01.price}  больше или равна цены квартиры {myFlat02.price}")

  myFlat02.setPrice(60000)
  if myFlat01<myFlat02:
     print(f" Цена квартиры {myFlat01.price} меньше цены квартиры {myFlat02.price}")

  myFlat02.setPrice(50000)
  if myFlat01<=myFlat02:
     print(f" Цена квартиры {myFlat01.price} меньше или равно цены квартиры {myFlat02.price}")



# testCircle()
testAirplane()
# testFlat()  