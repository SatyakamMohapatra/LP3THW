from sys import argv
script  = argv
print(argv[0])
print("How old are you?",end=' ')
age = input()
print("How tall are you?",end=' ')
height = int(input())
height = height+10
#3print("How much do you weight?",end =' ')
weight = input("How much do you weight? ")
print(f"So, you're {age} old,", (height+10), f"tall and {weight} heavy")
print(age)
