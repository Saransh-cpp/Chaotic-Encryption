def weird_function(n):
    weird_variable = {}
    for i in range(1, n+1):
        weird_variable[i] = i ** 2
    return weird_variable


n = int(input('Enter number of keys\n'))
print(weird_function(n))
