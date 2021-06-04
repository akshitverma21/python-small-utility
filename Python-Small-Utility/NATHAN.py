import random

cards=[]
for i in range(20):
    cards.append(1) #making all cards face down , as fd=1
print(cards)


counter=0
while 1 in cards:
    rPick=random.randint(0,len(cards)-1)
    print(f"picking {rPick} card")
    if cards[rPick]==1:
        cards[rPick]=0
        if rPick!=len(cards)-1:
            right=rPick+1
            if right ==1:
                cards[right]=0
                print(f"picking right")
            else:
                cards[right]=1
                print(f"picking right")

    else:
        continue

    counter+=1
print(f"all face up in {counter} counts now cards are {cards}")
