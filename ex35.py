from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input('> ')
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Men, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here")
    print("The bear has bunch of honey!")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear")
    bear_moved = False

    while True:
         choice  = input('> ')

         if choice == "take Honey":
             dead("bear looked at you and then slaped your face off")
         elif choice == "taunt bear" and not bear_moved:
             print("The bear moved from the door.")
             print("You can go through it now.")
             bear_moved = True
         elif choice == 'taunt bear' and bear_moved:
             dead("bear get pissed of and chew your leg off.")
         elif choice  == 'open door' and bear_moved:
             gold_room()
         else:
             print("I got no idea what that means.")

def cthilhu_room():
    print("Here you see the grat  evil cthilhu")
    print("He , it whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input('> ')

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthilhu_room()

def dead(why):
    print(why, "Good job")
    exit(0)


def start():
    print("You are in a dark room")
    print("There is a door to your right and left")
    print("Which door do you take?")

    choose = input("> ")

    if choose == "left":
        bear_room()
    elif choose == "right":
        cthilhu_room()
    else:
        dead("you stumble around the room until you starve...")

start()
