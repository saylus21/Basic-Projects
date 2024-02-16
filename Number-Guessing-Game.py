#guess the number
import random

def play():
  global num,bigcount,smallcount
  num=random.randrange(0,100)
  bigcount=0
  smallcount=0
play()
#print(num)

Status = True
while Status == True:
  user_num=int(input("Guess the number\n"))
  if user_num==num:
    print("You got it \n")
    play_again = input("Do You Want to play again ? \n")
    if play_again =="yes":
      play()
    else:
      Status = False
      print("Thank you")


  elif user_num > num and bigcount ==0:
    print("Too Big")
    bigcount+=1
  elif user_num > num and bigcount >=1 and bigcount <4:
    print("still Too Big")
    bigcount+=1
  elif user_num > num and bigcount >=4 and bigcount <10:
    print("still Too Big, try harder")
    bigcount+=1
  elif user_num > num and bigcount >=10:
    print("are you serious\n", "hers a ans :(  " ,num   )
    bigcount+=1

  elif user_num < num and smallcount ==0:
    print("Too small")
    smallcount+=1
  elif user_num < num and smallcount >=1 and smallcount <4:
    print("Still Too small")
    smallcount+=1
  elif user_num < num and smallcount >=4 and smallcount <10:
    print("Still Too small,try harder ")
    smallcount+=1
  elif user_num < num and smallcount >=10:
    print("are you serious\n", "hers a ans :(  " ,num   )
    smallcount+=1
