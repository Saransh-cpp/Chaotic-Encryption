def logistic_key(x, r, size):
    """
    This function accepts the initial x value, 
    r value and the number of keys required for
    encryption.
    The function returns a list of pseudo-random
    numbers generated from the logistic equation. 
    """

    key = []

    for i in range(size):   
        x = r*x*(1-x)   # The logistic equation
        key.append(int((x*pow(10, 16))%256))    # Converting the generated number between 0 to 255

    return key
