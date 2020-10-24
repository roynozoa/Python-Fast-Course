# Intermediate Programming in python
# handling with files
import os.path


# Handling Files


# creating a file (w=writing)
file = open("./[3] Intermediate Python/data.csv", "w")


# opening a file (r = read only, r+ = read and write)
# (a = appending)
file = open("./[3] Intermediate Python/data.csv", "r+")
file.write("id,name,phone number,email\n")  # write data to file
file.write('1,roy,08888888,roy@roy.com\n')
file.write('2,adi,08888887,adi@adi.com\n')
file.close()  # you need to close file after perform operation


# reading from files (r= read only)
# open file again after closing in line 17
file = open("./[3] Intermediate Python/data.csv", "r")
# print(file.read()) # print all data inside file

# print each line with for loops
# for line in file:
#    print(line)

print(file.readlines())  # read a files into a list
file.close()  # close file
print("============")

# better way to work with files
# 'with' keyword you don't have to close file manually
# (automatically close file)
with open("./[3] Intermediate Python/data.csv", "r") as file:
    print(file.readlines())


# file error handling
# with exception
try:
    with open("./[3] Intermediate Python/datas.csv", "r") as file:
        print(file.readlines())
except FileNotFoundError as file_error:
    print('file does not exist')

# with os.path
# import os.path (top of the line)

filename = "./[3] Intermediate Python/dataa.csv"
if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.readlines())
else:
    print(f'file does not exist')
