x = input("Enter a word: ")
first = ""
for i in x:
    c = ord(i)+13
    if (ord(i) >= 97 and ord(i) <= 122):
        if (c > 122):
            difference = c - 122
            first += chr(96 + difference)
        elif (c <= 122 and c >=97):
            first += chr(c)    
    elif (ord(i) >= 65 and ord(i) <= 90):
        if (c > 90):
            subtraction = c - 90
            first += chr(64 + subtraction)
        elif (c <= 90 and c >= 65 ):
            first += chr(c)
print("Your word in code is:")
print(first)
        
        
            
