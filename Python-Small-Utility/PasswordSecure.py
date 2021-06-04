
def secure(passwd):
    oldPass=passwd;
    SECURE=(('s','$'),('and','&'),('a','@')
            , ('o','0'),('i','1'),('I','|'))

    for item in passwd:
        # print(item)
        for itemS in SECURE:
            # print(itemS)
            if item in itemS:
                passwd=passwd.replace(item,itemS[1])
                # print(passwd)
        #simply use
    # for a,b in passwd:
        #passwd=passwd.repalce(a,b)
    #return passwd

    print("Your secure password is",passwd)
if __name__ == '__main__':
    # passwd=input("pass")
    secure("Indians123")
