from ClassLesson import *

myCircle =Circle(5)
print(myCircle)
myCircle.set(15)
myCircle2=Circle(30)
if myCircle<myCircle2:
   print(f"Длина окружности {myCircle.getL()} меньше длины окружности {myCircle2.getL()}") 
myCircle.set(30)   
if myCircle==myCircle2:
   print(f"Длина окружности {myCircle.getL()} равна длины окружности {myCircle2.getL()}") 


