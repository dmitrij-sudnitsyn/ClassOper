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
  



testFlat()  