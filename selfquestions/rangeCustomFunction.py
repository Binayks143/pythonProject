def custom_range(*args):

    #The *args parameter allows the function to accept a variable number of arguments.
    # This is useful for creating a flexible range function that can handle different numbers of inputs.


    num_args = len(args)

    if num_args == 0:
        raise TypeError("this function need at least 1 arguments")

    elif num_args >3:
        raise TypeError("This function can take max 3 arguments")


    start =0
    step =1


    if num_args == 1:
        stop =args[0]
    elif num_args == 2:
        start, stop =args

    else:
        start ,stop ,step =args

    if step == 0:
        raise ValueError("args is zero")

    """
    If step is positive and start is greater than or equal to stop, the range is invalid, and the function returns without yielding any values.
    If step is negative and start is less than or equal to stop, the range is invalid, and the function returns without yielding any values.
    """
    if (step >0 and start >= stop) or (step <0 and start <= stop):
        return

    current = start

    if step > 0:
        while current < stop:
            yield current
            current += step

    else:
        while current > stop:
            yield current
            current += step


print(list(custom_range(2, 10, 2)))
print(list(custom_range(20, 10, -2)))
print(list(custom_range(-20, -10, 2)))
