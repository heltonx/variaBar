

#Tested at Python 3.11.2

def regressiveBar ( ) : #firt part of the funciton to declaring variables
        import time, os
        bar = "============"
        decreasingBar = bar
        eater = -1
        os.system ( "cls" )

        def timing(): #time waiting function called during the loops
                time.sleep(1)
                os.system("cls")
                
        while len(decreasingBar) > 0: #loop to decrease the bar
                print(decreasingBar)
                timing()
                decreasingBar = bar[0:eater]
                eater -= 1

        farewell = ['...','END!'] # you can keep the farewell and the for (for a transition to another code) or can remove it

        for i in range(len(farewell)):
                print (farewell[i])
                timing()

regressiveBar()
