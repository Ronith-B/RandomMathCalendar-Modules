import random

gen_num=random.randint(1,100)
tries=0
while True:
  num1=int(input("Guess a number "))
  tries = tries+1
  if num1 == gen_num:
    print('Correct Guess')
    break
  elif num1 > gen_num:
    print('Guess a lower number')
  else :
    print('Guess a higher number')

print('You have taken',tries,'chances')