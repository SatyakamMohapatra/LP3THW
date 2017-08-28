#String and Text

#Create variable and insert the variable into the string using format String
#f"<String>"
type_of_people = 10
x = f"there are {type_of_people} types  of people."
binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

#Create a Variable and populate the same into a String using .format() function
hilarious = False
joke_evaluation = "Isn't that jock so funny?! {} or {}"

print(joke_evaluation.format(hilarious,type_of_people))

#Concat 2 string to form 1 string
w = "This is the left side of..."
e = "a String with a right side."

print(w + e)
