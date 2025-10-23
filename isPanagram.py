def isPanagram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in str.lower():
            return False
    return True

str=input("Enter a string:")
if(isPanagram(str)==True):
    print("Panagram")
else:
    print("NOt panagram")
