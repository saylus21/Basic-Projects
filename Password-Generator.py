#passwpord generator
import random
small="abcdefghijklmnopqrstuvwxyz"
capital="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567789"
characters="!@#$%^&*()"
passw = small+capital+numbers+characters

User_number= int(input(" enter number of password you want > \n"))
User_len  = int(input("ENter the length of password you would like > \n"))
seq=[]

for n in range(User_number):
  #for l in range(User_len):
  seq=(random.choices(passw,k=User_len))
  print(*seq,sep='')
