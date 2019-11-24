
def f(*args):
    nargs = len(args)
    print(nargs, args)


if __name__ == '__main__':

    # you can dis it in two ways 
    #   whole file  --  python3 -m dis __file__ 
    #   only func   --  dis.dis(f)  ( same as python3 __file__ )

    import dis
    dis.dis(f)
