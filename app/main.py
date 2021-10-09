file1 = open('/test.log', 'r')
Lines = file1.readlines()
 
# Strips the newline character because print will add it back
for line in Lines:
    print(line.rstrip())
