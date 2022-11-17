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



testCircle()
# testFlat()  