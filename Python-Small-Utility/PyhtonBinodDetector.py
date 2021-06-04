import os
def binoDetector():
    userDirectory=input("Please enter your directory")
    os.chdir(userDirectory)
    listdir=os.listdir()
    nBinod=0
    for item in listdir:
        if".txt" in item :
            with open (item) as listdirR:
                matter=listdirR.read()
                matter=matter.lower()
                if "binod" in matter:
                    print("binod found in :",item)
                    nBinod+=1

    print(f"{nBinod} binod found ")



if __name__ == '__main__':
    binoDetector()
