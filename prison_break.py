from typing import Hashable
import random
import sys,time,os


cheesepic='''       
       __
     .'o O'-.
    / O o_.-`|   
   /O_.-'  O | 
   | o   o  o|   
   |o   o O.-`  
   | O _.-'       
   '--`        


'''
mousepic="""
                                      ____    .-.
                                  .-"`    `",( __\_
                   .-==:;-._    .'         .-.     `'.
                 .'      `"-:'-/          (  \} -=a  .)
                /            \/       \,== `-  __..-'`
             '-'              |       |   |  .'\ `;
                               \    _/---'\ (   `"`
                              /.`._ )      \ `;
                              \`-/.'        `"`
                               `"\`-.
                               `"`

                               """

fusepic='''
                ╔════════════════════════════╗
               ╔╝ ═════════════════════════  ╚╗
              (║     A133 electrical Fuse     ║)
               ╚╗ ═════════════════════════  ╔╝
                ╚════════════════════════════╝

'''

ventpic='''
╔══════════════════════════════════════╗
║ x║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║ x║
║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║
║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║
║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║
║ x║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║ x║
╚══════════════════════════════════════╝
'''
ventpicopen='''
╔══════════════════════════════════════╗
║                                      ║
║                                      ║
║                                      ║
║                                      ║
╚══════════════════════════════════════╝

╔══════════════════════════════════════╗
║ x║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║ x║
║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║
║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║
║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║
║ x║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║ x║
╚══════════════════════════════════════╝
'''
brokenmirrorpic='''
       //-----------\\
     //       | |   | \\
   //  \__   /   \ /  | \\
  ||       \|     |  / __||
  ||         \    | |_/  ||
  ||\     __  |   |/ __  ||
  ||  \__/   \|   |_/  \_||
  ||  _    ___|  /  \_   ||
  ||_/ \__/   |/_     \_/||
  ||          o  \      _||
  ||\       / |    \___/ ||
  ||  \___/   |     \   /||
  ||     |   / \_    )-<_||
  ||    /  /     \  /    ||
   \\ /   |      _><    //
    \\   |     /   \   //
     \\---------------//   
'''

lockpic='''
     _____________
    ||           ||
    ||    0000   ||
    ||           ||
    ||___________||
    |   _______   |
    |  |    __ |  |
    |  |   |__||  |
    '--|_______|--'

'''

ending='''

  ______   ______   .__   __.   _______ .______          ___   .___________.__    __   __          ___   .___________. __    ______   .__   __.      ________.
 /      | /  __  \  |  \ |  |  /  _____||   _  \        /   \  |           ||  |  |  | |  |        /   \  |           ||  |  /  __  \  |  \ |  |    /        |
|  ,----'|  |  |  | |   \|  | |  |  __  |  |_)  |      /  ^  \ `---|  |----`|  |  |  | |  |       /  ^  \ `---|  |----`|  | |  |  |  | |   \|  |   |    (----~
|  |     |  |  |  | |  . `  | |  | |_ | |      /      /  /_\  \    |  |     |  |  |  | |  |      /  /_\  \    |  |     |  | |  |  |  | |  . `  |    \   \ 
|  `----.|  `--'  | |  |\   | |  |__| | |  |\  \----./  _____  \   |  |     |  `--'  | |  `----./  _____  \   |  |     |  | |  `--'  | |  |\   |.----)  |
 \______| \______/  |__| \__|  \______| | _| `._____/__/     \__\  |__|      \______/  |_______/__/     \__\  |__|     |__|  \______/  |__| \__|_______/ 
                                                                            
  ____    ____  ______    __    __     _______     _______.  ______     ___      .______    _______  _______ 
  \   \  /   / /  __  \  |  |  |  |   |   ____|   /       | /      |   /   \     |   _  \  |   ____||       \ 
   \   \/   / |  |  |  | |  |  |  |   |  |__     |   (----`|  ,----'  /  ^  \    |  |_)  | |  |__   |  .--.  |
    \_    _/  |  |  |  | |  |  |  |   |   __|     \   \    |  |      /  /_\  \   |   ___/  |   __|  |  |  |  |
      |  |    |  `--'  | |  `--'  |   |  |____.----)   |   |  `----./  _____  \  |  |      |  |____ |  '--'  |
      |__|     \______/   \______/    |_______|_______/     \______/__/     \__\ | _|      |_______||_______/ 
 
'''

def typewriter(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

ventopen= False
hasfuse= False
hascheese= False
hasmirror= False
typewriter("You wake up in a small cell on your own,\n your head hurts and you have no memory of how you got there\n You start looking round the room for a way to escape\n")
while True:
    print("Where should you go? Bed, Vent, Toilet, Food, Hole, Lock, Mirror")
    check=input(">").lower()
    if check =="bed":
         typewriter ("nothing that can help me here\n")
    elif check=="hole":
        if hascheese:
            print(fusepic)
            typewriter("It worked! Now lets hope this fuse works too\n")
            hasfuse=True
        elif ventopen:
         typewriter("Maybe theres something I can distract him with\n")
        else:
            typewriter("I can hear some scratching coming from that wall\n")
    elif check=="lock":
        if hasfuse:
            typewriter("the fuse works! now to figure out this password\n")
            print(lockpic)            
            num = random.randrange(1000, 9999)    
            n = int(input("Guess the 4 digit number:"))
            if (n == num):  
                typewriter("Wow, first attempt, I guess my lucks starting to turn round\n")
            else:   
                attempts = 0      
                while (n != num):          
                    attempts += 1    
                    count = 0         
                    n = str(n)            
                    num = str(num)           
                    correct = ['X']*4            
                    for i in range(0, 4):                
                        if (n[i] == num[i]):                  
                            count += 1    
                            correct[i] = n[i]  
                        else:
                            continue  
                    if (count < 4) and (count != 0):  
                        print("Not quite the number. But you did get ", count, " digit(s) correct!")
                        print("Also these numbers in your input were correct.")
                        for k in correct:
                            print(k, end=' ')
                        print('\n')
                        print('\n')
                        n = int(input("Enter your next choice of numbers: "))  
                    elif (count == 0):  
                        print("None of the numbers in your input match.")
                        n = int(input("Enter your next choice of numbers: "))
                    else:
                        print("I just need to think of the 4 digit code")
                if n == num:  
                    print("That did it! And it ony took", attempts, "tries. Lets get out of here.")
                    print(ending)
                    break    
        else:
            typewriter("A 4 number digital lock, looks like theres a fuse missing\n")       
    elif check=="food":
        if hascheese:
             typewriter("theres nothing left for me here\n")
        elif ventopen:
            print(cheesepic)
            typewriter("This cheese should distract the mouse long enough\n")
            hascheese=True            
        else:
                typewriter("This food looks like it's been here a while\n")
    elif check=="toilet":
        typewriter("The smell is disgusting\n")
    elif check=="vent":
        print(ventpic)
        if hasmirror:
            typewriter("maybe I could us that piece of the mirror to remove the screws\n")
            response =input ("use piece of mirror on screw? [Y/N]")
            if response.lower()== "y" or response.lower()== "yes":
                ventopen=True
                print(ventpicopen)
                typewriter("An electrical fuse falls out of the vent,\n You reach down to pick it up\n")
                print(mousepic)
                typewriter("But a mouse scurries past and takes it,\n running into the hole in the wall\n")
            else:
                typewriter("I'll come back to this later")
        else:
            typewriter("Theres something in this vent,\n the screws looks pretty loose,\n maybe i can find something to remove them\n")
    elif check=="mirror":
        print(brokenmirrorpic)
        if hasmirror:
            typewriter("Theres nothing left for me here\n")
        else:
            typewriter("This mirror is completely shattered, I'll take this piece of glass,\n it could come in handy\n")
            hasmirror=True
    else:
        typewriter("I cant waste any time\n")
