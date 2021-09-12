# hours = input('Enter Hours: ')
# rate = input('Enter Rate: ')

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))

except:
    print('Please enter a valid number')
    quit()

if hours > 40:
    overtime_pay = (hours - 40) * (rate * 1.5)
    pay = 40 * rate + overtime_pay
else:
    pay = hours * rate

print('Pay: ', pay)
