#provide variabe to the wildcard variables
formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("One","Two","Three","four") )
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter ))
