import random

def roll(dice1, dice2):
    
    x = (random.choice(dice1))
    y = (random.choice(dice2))
    print ("Shake em up")
    print ("Shake em up")
    print ("Shake em up")
    print ("Shake em!!!") 
    if (x, y) == (1, 1):
        print ("SNAKE EYES!!!")
    return (x, y)



print("WELCOME TO ICE CUBE'S STREET CRAPS.")
while True:
    try:
        answer = (input("Ready to shake 'em up shake 'em? Type Roll: "))
        answer = answer.upper() or answer.lower()
        #print ("")
       
                
        if answer == 'ROLL':
            break
        elif answer == "roll":
            break
        else:
            print ("Please type Roll")
            print ("")
    except ValueError:
        print ("NOPE")
        print ("")
        
def main():
    dice2 = [1,2,3,4,5,6] 
    dice1 = [1,2,3,4,5,6]        
    run_roll = roll(dice1, dice2)
    print (run_roll)
    print ("")
    while True:
        reroll = input("Press any key to Roll again. Hit Q to quit: ")
        reroll = reroll.upper() or reroll.lower()
        print ("")
        if reroll == "Q":
            print ("Goodbye")
            quit()
        else:
            print (main())
            print ("")

        

if __name__ == '__main__':
    main()
