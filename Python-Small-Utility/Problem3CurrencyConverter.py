def convertor(money,pto):
    pto1=pto.capitalize().split()[0]
    with open ("currency.txt") as c:
        for item in c:
            if pto1 in item:
                print(item)
                csplit=item.split("\t")
                ptoname=item.split("\t")[0]
                indian_value=float(csplit[1])
                primary1Value=float(csplit[2])
                moneyConverted =money * indian_value
                moneyConvertedToRupees=money*primary1Value
                print(f"{money} rupees to {ptoname} = {moneyConverted} ")
                print(f"{money} {ptoname} to rupees ={moneyConvertedToRupees} ")
                break

if __name__ == '__main__':
    money=int(input("Enter the amount\n"))
    with open("currency.txt") as r:
        print(r.read(),"\n")
    to=input("Enter the converting currency")
    convertor(money,to)

    # convertor(21,"yuan")