# /////////////////////////////////////////////////////////////////////////////////////

print('enter nubers (each one on the next line / press enter to exit)')

numbers = []

# /////////////////////////////////////////////////////////////////////////////////////

while True:
    x = input()
    if (x != ''):
        try:
            numbers.append(int(x))
        except ValueError:
            print('its not a number. try again')
            continue
    else:
        break

# /////////////////////////////////////////////////////////////////////////////////////

print('numbers:', end=' ')

for i in numbers:
    print(i, end=' ')

# /////////////////////////////////////////////////////////////////////////////////////

print('quantity: ', len(numbers))

# /////////////////////////////////////////////////////////////////////////////////////

sum = 0

for i in numbers:
    sum += i

print('sum: ', sum)

# /////////////////////////////////////////////////////////////////////////////////////

min = float('inf')
max = float('-inf')

for i in numbers:
    if(i < min):
        min = i

for i in numbers:
    if(i > max):
        max = i

print('min: ', min, 'max: ', max)

# /////////////////////////////////////////////////////////////////////////////////////

print('average value: ', sum / len(numbers))

# /////////////////////////////////////////////////////////////////////////////////////