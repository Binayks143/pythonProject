"""
Exceptions are errors
We should handle exceptions in our code
to make sure the code is working the way we want and is handling all the unwanted issues
Link to 3.5 built-in exceptions - https://docs.python.org/3/library/exceptions.html

else: if there is no exception else block is executing.
finally: always executed
raise: code will fail and inform related the issue
"""

def exceptionHandling():
    try:
        a=10
        b=20
        c=0
        d="hii"
        e=(a+b)/c
        print(e)
    except ZeroDivisionError:
        print("Zero division error")
        raise Exception ("Exception description:")
    except:
        print("This is except block")
    else:
        print("no exception")
    finally:
        print("This is always executed")

exceptionHandling()
