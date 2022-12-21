def fibonacci(n):
    """ This function return the nth value in
    the fibonacci series"""
    # checks if n <= 0, then return 0
    if n == 0:
        return 0
    # checks if n == 1, then return 1
    elif n == 1 or n == 2:
        return 1
    # checks if n < 0
    elif n < 0:
        return "Please enter numbers >= 0"
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    """This function return the nth value in
        the lucas series"""
    #checks if n <= 0, then return 2
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n < 0:
        return "Please enter numbers >= 0"
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(req, opt1, opt2):
    if opt1 == 0 and opt2 == 1:
        return fibonacci(req)
    elif opt1 == 2 and opt2 == 1:
        return lucas(req)
    else:
        if req == 0:
            return opt1
        elif req == 1:
            return opt2
        else:
            return sum_series(req - 1, opt1, opt2) + sum_series(req - 2, opt1, opt2)

