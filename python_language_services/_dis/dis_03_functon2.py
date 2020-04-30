
def f(*args):
    nargs = len(args)
    print(nargs, args)


if __name__ == '__main__':

    # well.. show the code (info) 
    #   run it without the '-m dis' 

    import dis
    dis.show_code(f)
