#python var names are snale cased 


first_name = "Brent"

x = 2

x = 9 

# since there is no const 
# THIS VAR SHOULD'NT BE CHANGED, write in uppercase

NUMBER_OF_DAYS_OF_WEEK = 7

### falsey values 

False 

None ### null in JS

0 #integer

0.0 #float 

'' # string 

[] ### list 

{} # dictionary 

### Operators 

## JS 

## && || !

###python
## and 
## or
## not 

# basic arthmetic 

# + - * / // %

14.5 / 3 # => 4.8333

int(12.4) # => 12 

float(14) # => 14.0

thing_to_do = "Take it"

way_to_do_it = "easy"

pronoun = "dude"

### String interpolation 

"{}{}{}. But {}!".format(thing_to_do, way_to_do_it, pronoun, thing_to_do)

### Flow Control 

# if x < 0
    print('Negative') ### like console.log
elif x == 0
    print('Zero')
else:
    print('Positive')

### loops 

count = 0

while count < 5:
    print(count)
    count = count + 1
else:
    print(count, "is not less than 5")

count = 15 

for i in range(1, count):
    print(i)
else: 
    ### else function as a completetion handler totally optional.
    print('done')
    

### Functions 

def function_example(param_one, param_two):

    ### function always needs an explicit return, this is a docString
    return param_two

### invoking the function 
function_example('something', 4)

### lists they are like arrays in js

secret_files = ["Top Secret", "Also top Secret"]

new_secrets = ["this is secret", "Want to hear a secret"]

## merge list together 

secret_files = secret_files + new_secrets


## indstead of push we have append 

secret_files.append('')

## .pop() removes the last element from a Python list 

##removes the number entered in the parens 

## secret_files.remove(1)

## len operator as the length function

len(secret_files)

## looping through 

for file in secret_files:
    print(file)


### Dictionaries - (js objects)

## in CS you may hea these referred to as maps or assosiative arrays 

student = {
    'name': 'burt',
    'course': 'WDI',
    'pockets': ['tissue', 'nickel', 'pick']
}

print(student['age'])

print(student.get('age'))

student.get('name')

## set a value if non exists 

student.get('birthday', '9/1/60')

## Tuples are basically list that can't be changed 

## Getting and setting values 

### getting a name 

print(student['name'])

## setting a name 

student['name'] = 'cassandra'


## add properties on the fly 

student['hungry'] = True


## we can delete keys 

del student['hungry']

## check if keys exists 

'hungry' in student # => False 

len(student) # => to find out how man keys we have 

print(student.items(), ' this is .items')

## best practice 

for key, val in student.items():
    print( f"{key} = {val}")
