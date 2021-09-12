filename = input('Enter file name: ')

try:
    handle = open(filename)
except:
    print(filename, 'goes brrrr')
    quit()

counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)


