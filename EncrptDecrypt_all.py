def machine():
    keys =  "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890 @#$%?^&*()/_+{<}/\>.,;'[]\:! |"
    #! won't be in the beginning otherwise it is replacing with pipe sign |
    value = keys[-1] + keys[0:-1]
    encryptDict = dict(zip(keys, value))
    decryptDict = dict(zip(value,keys))
    message = input("Please enter your secret message : ")
    mode = input("Please enter the mode : Encode(E) OR Decode(D) : ")
    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter]
                        for letter in message])
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter] 
                        for letter in message])
    else:
        print("Please enter  a correct choice")
    return newMessage
    #return newMessage.capitalize()

print(machine())