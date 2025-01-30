import random

confirm = "y"
  
while confirm == "y":
     
    num_dice = int(input("How many dice do you want to roll? "))

    dice_count = 0

    total = 0

    while dice_count < num_dice:

        no = random.randint(1,6)
     
        if no == 1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
        if no == 2:
            print("[-----]")
            print("[ 0   ]")
            print("[     ]")
            print("[   0 ]")
            print("[-----]")
        if no == 3:
            print("[-----]")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print("[-----]")
        if no == 4:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")
        if no == 5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")
        if no == 6:
            print("[-----]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[-----]")
        
        total += no
        dice_count += 1
        print("\n")

    print("Total dice roll = ", total)

    confirm=input("press y to roll again and n to exit:")
    print("\n")