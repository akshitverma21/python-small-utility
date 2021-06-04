
sum=0
i=0
while True:

    feed=input("Enter price or press enter to quit")

    if feed.isnumeric():
        i += 1
        feedn = int(feed)
        print(f"{i}. {feed}")
        sum=sum+feedn
        continue

    else:

        print(sum)
        break

