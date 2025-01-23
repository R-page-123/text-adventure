

def UIDcheck(UID, found):
    global strikes
    
    file = open("UIDdata.txt", "r")
    line=file.readline()
    
    while line != "":
        
        
        if line.strip() == UID:
            return True
        line=file.readline()
                
    strikes=strikes+1 
    return found
            
found=False   
strikes=0


while strikes<3 and found!=True:
    UID = str(input("input UID "))
    found=UIDcheck(UID, found)

#print found
#print strikes
if found==True:
     print("valid")
else:
     print("invalid")
