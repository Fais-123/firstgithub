
#secret number
secretNum=99

#User guess the Secret number
i=0

#while loop to count no of tries of guess.
while(i<=secretNum):
      guess=int(input("Guess the secret number:"))
      i=i+1
      print(f"No of tries is {i}")
      
      if(secretNum > guess):
           guess=guess+1
           print("Secret num was forward")
      elif(guess==secretNum):
           print("guess was right")
           break
      else:
           guess=guess-1
           print("Secret num was Backward")

print("You got right Number")

    
