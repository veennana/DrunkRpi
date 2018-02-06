x=2

def writeto():
    f = open("test.txt","w") #opens file with name of "test.txt"
    f.write("I am a test file.")
    f.write("%d" %x)
    f.close()
    return x
