from sys import argv
script,file_name = argv

def print_all(IO_file):
    print(IO_file.read())

def rewind(IO_file):
    IO_file.seek(0)
    print("rewind sucessfull")

def print_a_Line(line_count,IO_file):
    print(f"line Count: {line_count} and Line>>",IO_file.readline())

IO_file = open(file_name)

print_all(IO_file)

rewind(IO_file)

line_count = 2
print_a_Line(line_count,IO_file)

line_count = line_count + 1
print_a_Line(line_count,IO_file)

line_count = line_count + 1
print_a_Line(line_count,IO_file)
