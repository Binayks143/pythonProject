def carExceptionHandling():
    car={'make':"BMW","model":"BMW-7656yyy","year":2019}
    try:
        print(car["color"])
    except KeyError:
        print("Key not found")
    except:
        print("there is an other exception")
        raise Exception("Exception is")
    finally:
        print("task completed")


carExceptionHandling()



