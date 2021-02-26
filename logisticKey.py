def logistic_key(x, r, size):

    key = []

    for i in range(size):
        x = r*x*(1-x)
        key.append(int((x*pow(10, 16))%256))

    return key
