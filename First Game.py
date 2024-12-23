print("Lets Play Some Game Buddy!")

name = input("What is your Name? ")
print(f"Hello {name}, I am Glad to have you here!")
# print("Hello", name, "I am Glad to have you here!")

age = int(input("What is your Age? "))
print(f"You are {age} years old!")

health = 10

if age >= 21:
    print("You are eligible to play. Lets Start the Game!")

    ready_to_play = input("Do you want to play? (yes or no)>>> ").lower()
    if ready_to_play == "yes":
        print("You are starting with", health, "health to play")
        print("Select left or right")

        left_or_right = input("Choose One left or right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("Yes, You are on the right path! You want to walk in this beautiful nature or take that bike and go fast? (walk/bike) ")

            if ans == "bike":
                print("You almost WIN. Bike is Great, because Snakes are on the Walkway.")
            
            elif ans == "walk":
                 print("Oops. You bit by snake, You lost health of 5.. Run Faasttt")
                 health -= 5

            ans = input("You Seen Money Load of Million Dollars & a Beautiful Partner for Love. Choose only One - (dollars/partner)?  ")
            if ans == "dollars":
                print("You gotta Fight with SNAKES now. Because Money is secured by Venomous Snake.")
                health -= 3
                print("Your health is", health, "out of 10")

                giveup_or_fight = input("Will You give up or Fight. Just remember those snakes are Risky. On the other hand it's Million Dollars. Choose (fight/giveup)?  ")
                if giveup_or_fight == "giveup":
                    print("You are Rewarded with 1 Million Dollars, as those Snakes are like God for that Town.")
                    print("CONGRATULATIONS! You Won The GAME...Yayyyyyy!!")
                    print("Your Health is 10/10")
                    print("You got 1 Million Dollars...See you in the Next Game..!")
                else:
                    print("These Snakes are God in that Town. YOU CHOOSE WRONG PATH. You Lost!")
                    health -= 10
                    print("Your Health is 0")
                    print("Good Luck Next Time!")


            elif ans == "partner":
                print("You got Divine Partner got you 10 Million Dollars. Your Heart with Love Saved You.")
                health += 5
                print("Your Health is 10/10")
                print("CONGRATULATIONS! You Won The GAME...Yayyyyyy!!")
                print("See you in the Next Game..!")

            else:
                print("You Lost the Game!")

        elif left_or_right == "right":
            print("You are into tiger cave. You lost the Game!")

        else:
            print("You lost the Game!")

    
    else:
        print("Have a Great Day! Bye.")


else:
    print("Sorry Buddy! You are not eligible to play")