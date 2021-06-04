import pandas as pd #we will import excel
import datetime
import smtplib
import os
#write your gmail credentials
os.chdir(r"C:\Users\DELL\PycharmProjects\PythonPractice")
os.mkdir("test")
GMAIL_id=''
GMAIL_psw=''

def sendEmail(to,sub,msg):
    print(f"Email to {to} sent with subject {sub} and message {msg} ")

    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_id,GMAIL_psw)
    s.sendmail(GMAIL_id,to,f"Subject : {sub}\n\n{msg}")

    #input your gmail id and pass
    #turn off security for less secure apps
    s.quit()


if __name__ == '__main__':
    df=pd.read_excel("Data.xlsx")
    # print(df)
    today=datetime.datetime.now().strftime("%d-%m")
    yearNow=datetime.datetime.now().strftime("%Y")
    print(today)
    writeInd=[]
    for index,item in df.iterrows():
        # print(index,item["Birthday"])
        bday=item["Birthday"].strftime("%d-%m")
        print(bday)

        if today==bday and yearNow not in str(item["Year"]):

            sendEmail(item["Email"],"Happy Birthday",item["Dialogue"])
            writeInd.append(index) ##?

    print(writeInd)
    if len(writeInd) !=0:

        for i in writeInd:
            yr=df.loc[i,"Year"]
            print(yr)
            df.loc[i,"Year"]
            df.loc[i,"Year"]=str(yr) +','+str(yearNow)
            print("updated year column : ",df.loc[i,"Year"])

    # print(df)
        df.to_excel("data.xlsx",index=False)
    else :
        print("writInd is null")