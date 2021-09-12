total = 0
count = 0

while True:
    num = input('Enter a number: ')

    if num == 'done':
        print(f'total: {str(total)}, count: {str(count)}, avg: {str(total/count)}')
        break

    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue

    total += fnum
    count += 1