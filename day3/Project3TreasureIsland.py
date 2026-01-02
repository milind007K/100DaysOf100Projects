print("welcome to treasure island")
print("your mission is to find the treasure")
choice1 = input('you are at the crossroad where do you want to go?'
                ' type "left" or "right".').lower()

if choice1 == "left":
    choice2 =  input('you\'ve come to a lake , there is a island in the middle of the lake . '
          'type "wait" to wait for the boat. type "swim" to swim across')

    if choice2 == "wait":
        choice3 = input("you arrived at the island unharmed."
          " there is a house with 3 doors one red, one yellow,one blue which color do you choose").lower()
        if choice3 ==  "red":
            print("GAME OVER")
        elif choice3 == "yellow":
            print("you find the tresure .YOU WIN !")
        elif choice3 == "blue":
            print("GAME OVER")
        else:
            print("you choose a door that doesn't exist GAME OVER")
    else:
        print("you get attacked bby angry throut .GAME OVER")
else:
    print("you fell into a hole . GAME OVER")
