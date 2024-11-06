'''
lesson 2.3
created by leo xu
last edited on oct 16 2024
'''

def q1(): 
  #Write Assignment code here
  word = input("In: ")
  if (word[-2:]) == "ey":
    print("-eys")
  elif (word[-1:]) == "y":
    print("-ies")
  elif (word[-3:]) == "ife":
    print("-ives")
  else:
    print("-s")

def q2(): 
  #Write Assignment code here
  num = int(input("In: "))
  if num > 0: 
    print(f"{num} is positive")
  elif num < 0:
    print(f"{num} is negative")
def q3():
  #Write Assignment code here
  tri1 = float(input("Input a number: "))
  tri2 = float(input("Input a number: "))
  tri3 = float(input("Input a number: "))

  if tri1 + tri2 < tri3 or tri2 + tri1 < tri3 or tri3 + tri1 < tri2: 
    print("No Triangle")
  elif tri1 == tri2 and tri2 == tri3:
    print("Equilateral")  
  elif tri1 == tri2 and tri1 != tri3:
    print("Isosceles")
  elif tri1 != tri2 and tri2 != tri3:
    print("Scalene")

#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
# q3()