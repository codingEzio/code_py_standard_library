
# vals 
i = 1 
j = 0 
k = 3 

try:
    res = k * (i / j) + (i / k)
    
except Exception:
    
    import dis 
    import sys 

    exc_type, exc_val, exc_trabk = sys.exc_info()
    dis.distb(exc_trabk)