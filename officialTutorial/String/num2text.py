def main():
    instring = input("please enter a sequence: ")
    message = ''
    chars=[]
    for cha in instring.split():
        temp = int(cha)
        message = message + chr(temp)
        chars.append(chr(temp))
    print(message)
    #uncommen this to get the right output. message.join does a "join" step for each elements in "message"
    #message=''  
    print(message.join(chars))

main()
