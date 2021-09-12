fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print(f'Error: {fname} can\'t be found')
    quit()

print('\n-----Calculate Average Spam Confidence-----\n')

total_score = 0
count = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        lstart = line.find(':')
        score = float(line[lstart+1:].strip())
        total_score += score

print('Average spam confidence:', total_score/count)
