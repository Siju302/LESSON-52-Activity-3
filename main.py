# Program to remove lines starting with any prefix

file1 = open('file.txt', 'r')
file2 = open('updatedfile.txt', 'w')

# reading each line from original
# text file
for line in file1.readlines():

    if not (line.startswith('I')):

        # printing those lines
        print(line)

        # storing only those lines that
        # do not begin with "I"
        file2.write(line)

# close and save the files
file2.close()
file1.close()