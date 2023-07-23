def only_ints (a,b):
    if type(a) == int and type(b) == int:
        return True
    else:
        return False
    
call = only_ints('a',1)
print(call)
