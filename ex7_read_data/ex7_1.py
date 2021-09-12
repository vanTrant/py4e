fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print(f'Error: {fname} can\'t be found')
    quit()

for line in fhand:
    line_uppercase = line.upper()
    print(line_uppercase)


