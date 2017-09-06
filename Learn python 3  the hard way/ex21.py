#function can return something
def add(a,b):
    print(f"adding {a} and {b}")
    return a + b

def sub(a,b):
    print(f"subtrating {a} and {b}")
    return a - b

def mul(a,b):
    print(f"Multplying {a} with {b}")
    return a * b

def div(a,b):
    print(f"dividing {a} from {b}")
    return a / b

print("Let's do math with just function!")

age = add(20,5)
height = sub(78,4)
weight = mul(90,2)
iq = div(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#A puzzlw for the extra credit,type it in anyway.
print("Here is a puzzle")

what = add(age,sub(height,mul(weight,div(iq,2))))

print("That become: ",what, "Can yo do it by hand?")
