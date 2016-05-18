from sys import argv
script, filename = argv

print ("We are going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C(^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')
#file is opened in w mode, which overwrites anyway, so behaviour is same truncate is used or not
print ("Truncating the file. Goodbye!")
target.truncate()

##If i want to append to file, i will need to open in a mode
print ("Now I am going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I am going to write these to the file.")

#line1 = line1+"\n"+line2+"\n"+line3+"\n"
target.write(line1+"\n"+line2+"\n"+line3+"\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print ("And finally, we close it.")
target.close()

file_read = open(filename)
print (file_read.read())
file_read.close()