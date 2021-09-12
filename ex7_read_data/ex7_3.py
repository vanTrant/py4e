fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print(f'{fname} go brrrrr')
    quit()

print('\n-----Calculate Average Spam Confidence-----\n')

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1

print(f'There were {int(count)} subject lines in {fname}')
