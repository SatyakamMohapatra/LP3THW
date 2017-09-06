print("Let's practice everything.")
print('you\' need to know \'bout escape with \\ that do')
print('\n new line and \t tab')

poem="""
\tThe lovely world
with logical so firmly planted
cannot discern \nthe needs of love
nor comprehend passion from intution
and requires an explanation
\n\twhere there is none.
"""
print("----------------")
print(poem)
print("----------------")

five = 10 - 2 + 3 - 6
print(f"This should be {five}")

def secret_fromula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates = jars / 100
    return jelly_beans,jars,crates

start_point = 1000
beans,jars,crates = secret_fromula(start_point)

#This is another way to format a string
print("with a starting point of: {}.".format(start_point))

#it's just like with an f"" starting
print(f"we'd have {beans} beans,{jars} jars,{crates} crates.")

start_point = start_point / 10

print("We can also do in this way")
formula = secret_fromula(start_point)
#this is a easiest way to apply a list to a formated starting
print(formula)
print("we'd have {} beans,{} jars,{} crates.".format(*formula))
