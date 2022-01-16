#if a series is 2,4,8,.....,n
#guess its 4th element


insert_coin=input("insert a 5 cent coin:")


a=[2,4,8,None,32,64,None]

third_element=a[2] * 2

seven_element=a[5] * 2


if(insert_coin=="y"):
    
      guess=int(input("enter a number:"))
      
      if (guess==third_element):
          
               print("You are winner")
               
               wanted_more=input("Want to continue reinsert a 5 cent coin:")

               if(wanted_more=='y'):
                   
                   guess=int(input("enter a number:"))

                   if (guess==seven_element):

                          print("You are winner")
                   else:
                        print("Better luck next time")
               else:
                   print("Try next time")

               


      else:
               print("Batter luck next time")

else:
    print("First insert coin")


