#LOOPS
the_count = [1,2,3,4,5,6]
Fruits = ["apples","oranges","pears","apricots"]
changes = [1,"pennies",2,"demes",3,"quaters"]

#For each loop to go throuth the List
a = None
if a is not None:
    for number in the_count:
        print(f"The number in the List the_count is {number}")

#The ForEach loops to go through the string List
for Fruit in Fruits:
    print(f"The Fruits are {Fruit}")

#The ForEach loop and gothrouth the mixed Lint and print
for i in changes:
    print(f"I got {i}")

#We canalso build a List
#1 create a empty List
elements = []
#2 populate the List
for i in range(1,11):
    print(f"Adding {i} to the List")
    elements.append(i)

print("Printing the list ",elements)
#Now we can ittrate through the list and print them out
for element in elements:
    print("The current elements are {}".format(element))
