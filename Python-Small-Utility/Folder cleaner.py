import os

def start():
    current=input("Enter the directory you wan to manage")
    os.chdir(current)
    current = os.getcwd()
    print(f"You are in {current}")
    createIfNotExists(current)
    move(current)

def createIfNotExists(current):
    for entry in os.listdir(current):
        if os.path.isfile(entry):
            print("Entry is ",entry)
            fileEnd=os.path.splitext(entry)[1]
            if not os.path.exists(fileEnd) and not os.path.exists("torrent") and entry.endswith("torrent"):
                os.mkdir("torrent")
            elif not os.path.exists(fileEnd) and not entry.endswith("torrent"):
                 # workrs for every file except torrent
                print(entry.split(".")[1])
                os.mkdir(fileEnd)

def move(current):
    # torrent=[]
    for item in os.listdir(current):
        if item.endswith("torrent") and os.path.isfile(item):
            # torrent.append(item)
            os.replace(item,f"torrent/{item}")
        elif os.path.isfile(item):
            entrySplit=os.path.splitext(item)[1]
            os.replace(item,f"{entrySplit}\{item}")



        # os.replace(entry,"torrentFiles")

if __name__ == '__main__':
    start()
