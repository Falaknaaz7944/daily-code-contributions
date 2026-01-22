#rock,paper and scissors game.............
#for rock choose 0,for paper choose 1 and for scissors choose -1
import random
computer=random.choice([0,1,-1])
yournum=int(input("enter your choice: "))

numdict ={ 0:"rock", 1:"paper",-1:"scissors"}
reversedict={"rock":0,"paper":1,"scissors":-1}
you =numdict[yournum]

print(f"you chose {numdict[yournum]} computer chose {numdict[computer]}")
if(computer==yournum):
    print("draw")
elif(computer==1 and yournum==0):
    print("computer wins")
elif(computer==1 and yournum==-1):
    print("you wins")
elif(computer==0 and yournum==1):
    print("you wins")
elif(computer==0 and yournum==-1):
    print("computer wins")
elif(computer==-1 and yournum==0):
    print("you wins")
elif(computer==-1 and yournum==1):
    print("computer wins")

