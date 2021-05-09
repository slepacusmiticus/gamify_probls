def converted(a):
    # check if a, the INPUT STRING, is a (float)number OR any other string(non-number)
    # if it is a string, return False
    # for number return True

    try:
        number = float(a)
        # if (type(number) in (int, float)):
        if isinstance(number, float):
            # TODO also check if number isn't big/small enough not to fit in a float
            print(type(number))
            return number
    except ValueError as my_except:  # or is it TypeError
        # print('My exception:', my_except, type(my_except))
        # print("It is possible that the number is not a float")
        return False
    except Exception as e:
        print('Exception:', e)
        print('some other exception rise in conversion str to float')
        return False
