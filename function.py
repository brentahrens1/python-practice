def sum_to(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total 
print(sum_to(9))

def largest( list ):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
print (largest([4, 10, 7, 8]))
    

def occurances(str1):
    dup = {}
    for n in str1:
        keys = dup.keys()
        if n in keys:
            dup[n] += 1
        else:
            dup[n] = 1
    return dup 
print(occurances('tootsieroll'))

def product(* num):
    total = 1
    for i in num:
        total *= i
    return total
print(product(3,7,6))