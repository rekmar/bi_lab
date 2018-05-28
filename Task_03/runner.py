import pytasks


def runner(*args):
    if len(args) != 0:
        for func in args:
            print("\n", func)
            getattr(pytasks, func)()
    else:
        for func in dir(pytasks):
            if func[:2] != "__":
                print("\n", func)
                getattr(pytasks, func)()
    return


runner('is_palindrome', 'generate_numbers')
runner()
