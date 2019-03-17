### Lists are like arrays in JS 

colors = ['red', 'blue', 'green']

len(colors) ## => 3 

colors[-1] # => green

colors[-1] = 'baby_blue'

### add multiple to our list at once 

colors.extend(['orange', 'black'])

### insert() items anywehre but the end og the list 

colors.insert(1, 'yellow')

### .pop method 

green = colors.pop(2)

### Deleting color at index 1
del colors[1]

colors.remove('red')

print(colors)

### clear out any array 

colors.clear() ## => an empty array 

for color in colors:
    print(color)

    ## let's say we needed the index number 

    for index, color in enumerate(colors):
        print(index, color)


## list comprehensions 

nums = [1,2,3,4,5,6,7,8,9,10]


## we need to square all the numbers and put them in a new list 

squares = []

for n in nums:
    squares.append(n * n)


print(squares)


## List comrehension 
squares = [n * n for n in nums]

### [<expression> for <item> in <list>]


## List comprehension filtering 

## wanted to make a list with all the even squares 

even_squares = []

for n in nums:
    square = n * n
    if square % 2 == 0:
        even_squares.append(square)
print(even_squares)

## Pythonic way
even_squares = [n * n for n in nums if (n * n) % 2 == 0]

## Tuples we can think of them as immutable list 

colors = ('blue', 'purple', 'green')

colors = 'red', 'green', 'orange'

print(colors)

print(len(colors))

## Finding the type of something 

print(type(colors)) ### => class tuple 

## Tuples are immutable they are great for protecting data we don't want to change 
##Since they are immutable it is faster to iterate over over them than lists 

print(colors[0]) # => red 

green_index = colors.index('green')

print(green_index) # => 1

for index, color in enumerate(colors):
    print(index, color)

### unpacking , tuples can be unpacked or (destructed)

## var that are being assigned to the corresponding index

red, green, orange = colors

red = 'bright red'

print(red, green, orange)

### const arr = [1,2,3] 
### [one, two, three] = arr

### ranges 

### ranges have a class type of range 

## range type represents an immutable sequence of numbers, and they're 
## usually used with a for loop to iterte a certain number of times 

for num in range(5):
    print(num)

## by default the sequence is going to start at zero and goes up to
## the integer passed 


## first argument is the starting point, step 

for even in range(2, 10, 2):
    print(even)

nums_through_nine = list(range(10))

print(nums_through_nine)

odds = tuple(range(1, 10, 2))

print(odds)


## the end point is not inclusive 

for num in range(5, 0, -1):
    print(num)

### Sequence can be sliced, array, string, tuple, range 

## the end point is not inclusve

short_hand = 'Alexandria'[0:4]

print(short_hand)

colors = ('red' , 'green', 'blue')

## omit the firt imdex the sequence starts copying at the beggining

print(colors[:2])

print(colors[1:]) ## => green and blue

fruit = ('apples', 'bananas', 'oranges')

fruit_copy = fruit[:]

print(fruit_copy)

print(type(fruit_copy))



