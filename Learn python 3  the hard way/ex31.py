#IF ELSE
print("""
you enter a drak room with two doors!
Do You go through door #1 or #2?
""")

door = int(input('> '))

if door == 1:

    print("There is a gient beer sitting and eating cake")
    print("What to do?")
    print("1. Take the cake")
    print("2. scream at the bear")

    bear = input('> ')

    if bear == '1':
        print("The bear eats your face")
    elif bear == '2':
        print("The bear eats your legs")
    else:
        print(f"well,dowing {bear} is probably better.")
        print("Bear Runs away.")

#elif door =='2':
elif door in range(2,10):

    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberry")
    print("2. yello Jacket")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input('> ')
    if insanity == '1' or insanity == '2':
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
else:
    print("You stumble around and fall on a knife and die. Good job!")
