from ClassLesson import *

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
