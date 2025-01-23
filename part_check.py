
def old(code):
    code  =str(code)
    inp = code[3] 
    inp = int(inp)
    if (inp > 5) and (inp < 9):
        return True
    else:
        return False
    
part = 0
op = 0
tp = -1
while part != "9999":
    part = input("input code: ")
    if old(part):
        op = op + 1
    tp = tp + 1
else:
    print(op,"old parts")
    print(tp,"total parts")