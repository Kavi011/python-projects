name = input("Enter player name: ")
start = False

while True:
    input1 = input("> ").capitalize()
    if input1 in ('Start','Stop','Turn','Park','Help','Quit'):
        
        if input1 == "Start":
            if start:
                print("The car is already started! It can't be started again.")
            else:
                start = True
                print("The car is started!!!")
                
        elif input1 == "Stop":
            if not start:
                print("The car is already stopped! It can't be stopped again.")
            else:
                start = False
                print("The car is stopped!!!")
                
        elif input1 == "Turn": 
            turn = " "
            
            if not start:
                print("The car isn't started yet! Please start your car to turn!")
                
            else: 
                start = True
                print("Which side do you want to turn your car? (Left/Right) :")
                turn = input("> ")
                
                if turn == "left":
                    print("The car turns towards the left side!")
                elif turn == "right":
                    print("The car turns towards the right side!")
                    
        elif input1 == "Park":
            print("The car has been parked!!!")
            
            
        elif input1 == "Help":
            print('''
Instructions:

>>> Start => To start the car...
>>> Stop => To stop the car...
>>> Turn => To turn left or right...
>>> Park => To park the car...
>>> Quit => To quit the game...
            ''')
                
        elif input1 == "Quit":
              print("Thank You",name,"for participating!!!")
              break
        
    else:
        print("Sorry! I don't understand!")

        
                