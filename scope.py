# global variable
name="KLT"

def sayMyName() :
    #local
    global name; #to update local to global from local
    name="MMM"
    print(name)

sayMyName()

print(name)