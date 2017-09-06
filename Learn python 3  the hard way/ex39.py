#Dictionary
#Create a mapping of state and there abbrevation
states = {
        'Oregon':'OR',
        'Florida':'FL',
        'California':'CA',
        'New Work':'NY',
        'Michigan':'MI'
}

#Create a basic state of state and some cities in them
cities ={
        'CA':'San Francisco',
        'MI':'Detroit',
        'FL':'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('_'*10)
print("NY states has: ",cities['NY'])
print("OR states has: ",cities['OR'])

#print some states
print('_'*10)
print("Michigan abbrevation is: ",states['Michigan'])
print("Florida abbrevation is: ",states['Florida'])

#Do it by states then cities
print('_'*10)
print("Michigan states has: ",cities[states['Michigan']])
print("Florida states has: ",cities[states['Florida']])

#print every state abbrevation
print('_'*10)
for state,abbrevation in list(states.items()):
    print(f"{state} abbrevation is: {abbrevation}")

#Print every city in the states
print('_'*10)
for city,state in list(cities.items()):
    print(f"{city} states has: {state}")

#now both at the same time
print('_'*10)
for state,abbrevation in list(states.items()):
    print(f"""
    {state} abbrevation is: {abbrevation} &
    has cities like: {cities[abbrevation]}
    """)

#Get a abbrevation by state that might not be there
print('_'*10)
state   = states.get('Texas')
if state:
    print(state)
else:
    print("Sry no Texas")

#Get a city with defult value
city = cities.get('TX','Does not exist')
print(city)
