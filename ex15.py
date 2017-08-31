from sys import argv
script,file_name = argv
prompt  = ' > '

txt = open(file_name)

print(f"here is your file name:  {file_name}")
print(txt.read())

print("Type your file name again")
#file_name  = input(prompt)

print(f"here is your file name:  {file_name}")
#txt_again = open(file_name)

#print(txt_again.read())
#better way to write the code as it act as try catch block
with open(file_name,'r') as tx:
    print(tx.readlines())
tx.close()

with open(file_name,'r') as tx:
    print(tx.read())
tx.close()
