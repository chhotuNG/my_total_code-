secret_number = 9
chance=3
starting_chance=1
while starting_chance <= chance:
    guess_number = int(input("gusses number : "))
    if guess_number==secret_number:
        print("you won!!")
        break
    else:
        print("you lost chance")
        print("remaind chance is",chance-starting_chance)
    
    starting_chance+=1
else:
    print("you failed !!")