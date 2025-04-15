def isprime(x):
    
    if x == 0:
        return False
     
    result = True

    for i in range (2, x):
        if x % i == 0:
            result = False
            break

    return result

