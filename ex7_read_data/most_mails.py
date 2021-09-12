filename = input('Enter file name: ')

try:
    handle = open(filename)
except:
    print(filename, 'goes brrrr')
    quit()

counts = dict()

for line in handle:
    if not line.startswith('From'):
        continue
    word = line.split()
    email = word[1].split('@')
    inst = email[1]
    counts[inst] = counts.get(inst, 0) + 1

# Find the top 5 most count
tmp = list()
for key, value in counts.items():
    tmp.append(( value, key ))

tmp_sorted = sorted(tmp, reverse=True)
for value, key in tmp_sorted[:5]:
    print(value, key)


# Find the most count
# bigcount = None
# bigword = None

# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigcount = count
#         bigword = word

# print(bigword, bigcount)


