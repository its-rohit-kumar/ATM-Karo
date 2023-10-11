import time
import mysql.connector as sp
from win32com.client import Dispatch
import numpy as np
speak=Dispatch(("SAPI.SpVoice"))
# speak=speak(str)
a=0
o=0
p=0
c=0
m=0
e=0
s=1
mydb=sp.connect(host='localhost',user='root',passwd='Rohit@123')
cur=mydb.cursor()
# a="insert into account_details(stno,name,account_no,pin,current_balance,saving_balance,phone_no)values(1,'a',00001,5,1000,1000,101010101)"


# cur.execute('create database rohit')
cur.execute('use rohit')

# cur.execute("create table account_details(stno int(10) not null,name char(25) not null,account_no int(10) not null,pin int(10) not null,current_balance bigint(20) not null,saving_balance bigint(20) not null,phone_no bigint(13) not null)")
cur.execute(a)
mydb.commit()



def speak(str):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)
    mydb.commit()




def makeaccount():

    
    l=[]
    cur.execute("select stno from account_details")
    cur.fetchall()
    e=cur.rowcount
    o=e+1
    l.append(o)


     
  
    speak("enter your name")


    name=input("Enter Name: ")
    l.append(name)


    cur.execute("select account_no from account_details where stno='%s'"%e)
    dat=cur.fetchone()
    for i in dat:
        p=i
    ab=p+1
    l.append(ab)

    
    speak("Pin you want")

 
    pin=int(input('Enter Your Pin(4 digit): '))
    l.append(pin)


    speak("enter amount you want to deposit in current balance")

    current_balance=int(input("Enter amount you want to deposit in current balance: "))
    l.append(current_balance)


    
    speak("enter amount you want to deposit in saving balance")

    saving_balance=int(input("Enter amount you want to deposit in saving: "))
    l.append(saving_balance)


    speak("enter your phone number")

    x=int(input("Enter ur phone no: "))
    # list=[.0,.1,.2,.3,.4,.5,.6,.7,.8,.9]
    # v=x//10000000000

    while len(str(x)) ==10:
        
        cur.execute("select phone_no from account_details")
        phone_numbers = [row[0] for row in cur.fetchall()]

        #n=cur.fetchall()

        if x in phone_numbers:
            speak("Account is already created with this mobline number")

            print("Account is already created by this mobile number")
            break
            

        else:
            l.append(x)
            stud=(l)
            sql="insert into account_details(stno,name,account_no,pin,current_balance,saving_balance,phone_no) values(%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(sql,stud)
            mydb.commit()

            speak("your account is succefully created")
            print("\nYOUR ACCOUNT IS SUCCEFULLY CREATED")
            print("")
            print(" DETAILS ARE GIVEN BELOW ")
            print("")
            print("YOUR ACCOUNT NO IS -",ab,"AND PIN IS -",pin)
            print("")
            print("Name:- ",l[1] ,"\nAccount No:- ",l[2],"\nPin:- ",l[3],"\nCurrent Balance:-",l[4],"\nSaving Balance:-",l[5],"\nPhone No:-",l[6])    
            mydb.commit()
            break
    
        #else:
         #   print("Account is created by this mobile number")

    else:
        print("Enter correct phone number")
        
def cashwithdrawal():

    speak("Confirm your account number")

    x=int(input('Enter your account no: '))
    speak("withdraw from saving balance or from current balance")

    print(" ")
    z=input("Choose from (saving_balance or current_balance):  ")
    cur.execute("select %s from account_details where account_no='%s'"%(z,x))
    data=cur.fetchone()
    for i in data:
        a=i


    speak("enter amount you want to withdraw")
    
    c=int(input("Enter Amount: "))
    if(a>=c):
        v=a-c

        cur.execute("update account_details set %s='%d' where account_no='%s'"%(z,v,x))
        mydb.commit()
        print("Amount Withdrawn is",c)

        print("")
        speak("wait ")
        time.sleep(2)
        speak("wait ")
        time.sleep(1)
        speak("wait")
        time.sleep(1)
        speak("Transection completed")
        time.sleep(1)
        print(" SUCCESFULLY withdrawal of MONEY")        

        print("")
        speak("ENTER 1 to see balance otherwise enter 2")

        d=int(input("See balance :- 1 \nExit :- 2  : "))

        print("")

        if(d==1):
    
            print("you have Rs",v," in your account")
            print("")
            
        else:
            print("thanks for banking")
            print("")
            
    else:
        print("")
        print("your requirment is greater than money you have . You have ",a, "money")
    mydb.commit()

def balance():
    speak("Confirm your account number")

    x=int(input('Enter your account no: '))
    
    f="select current_balance from account_details where account_no='%s'"%(x,)
    cur.execute(f)
    res=cur.fetchone()
    for i in res:
        c=i
    a="select saving_balance from account_details where account_no='%s'"%(x,)
    cur.execute(a)
    re=cur.fetchone()
    for j in re:
        b=j
    
    
    print("Current Balance ------->",c,"\nSaving Balance------->",b)
    mydb.commit()
    
def tranfermoney():
    speak("Confirm your account number")

    x=int(input('Enter your account no: '))
    
    speak("enter receiver account number")

    y=int(input('Enter your account no: '))
    cur.execute("select * from account_details")
    n=cur.fetchall()
    for i in n:
        if(y==i[2]):
            a=y
    if(y==a):
            speak("enter amount")

            h=int(input("Enter Amount: "))
            cur.execute("select saving_balance from account_details where account_no='%s'"%x)
            data=cur.fetchone()
            for i in data:
                c=i
            if(c>=h):
                p=(c-h)
                j="update  account_details set saving_balance=%s where account_no='%s'"%(p,x)
                cur.execute(j)
                mydb.commit()
            
                cur.execute("select saving_balance from account_details where account_no='%s'"%y)
                data=cur.fetchone()
                for i in data:
                    e=i
                o=h+e
                cur.execute("update account_details set saving_balance=%d where account_no='%s'"%(o,y))
                mydb.commit()
                
                speak('''wait
        wait
        wait
        wait
        .
        .
        .
        .
        succesfull transtered''')

                print(" SUCCESFULLY TRANSFERED MONEY TO ACCOUNT NO -->",y)
            else:
                print("Not Sufficient Balance")
    else:
        print("INVALID ACCOUNT NUMBER")
         
def account_view():
    speak("Confirm your account number")

    x=int(input('Enter your account no: '))
    
    cur.execute("select * from account_details where account_no=%d"%x)
    n=cur.fetchall()
    for l in n:
        print("Name:- ",l[1] ,"\nAccount No:- ",l[2],"\nPin:- ",l[3],"\nCurrent Balance:-",l[4],"\nSaving Balance:-",l[5],"\nPhone No:-",l[6])        
    mydb.commit()

def luckydraw(s):
    speak("Confirm your account number")

    x=int(input('Enter your account no: '))
    if(s==1):
        speak("welcome to lucky draw")        
        m=int(input("Choose a number  1,2 or 3:  "))
        a=np.random.randint(low=1 ,high=4)
        if(m==a):
            price=np.random.randint(low=1 ,high=100)
            speak("WINNER WINNER CHICKEN DINNER")
            print("WINNER WINNER CHICKEN DINNER")
            print("\nYou are lucky person and you get Rupees -->",price,'.')
            cur.execute("select current_balance from account_details where account_no=%d"%x)
            data=cur.fetchone()
            for i in data:
                o=i        
            c=o+price            
            cur.execute("update account_details set current_balance=%d where account_no=%d"%(c,x))
            mydb.commit()
        else:
            speak("BETTER LUCK NEXT TIME")
            print("BETTER LUCK NEXT TIME")
        mydb.commit()
        s+=1
    else:
        print("Come Back After Seven Days!")

def changepin():

    
    speak("please enter your account number")
    
    a=input("Enter your Account Number:   ")
    print(" 1.> if you know your pin\n 2.> if not")
    b=int(input("Enter 1 or 2: "))
    if(b==1):
    
        speak("enter your existing pin")

        no=int(input("Enter your pin: "))
        cur.execute("select pin from account_details where account_no='%s'"%a)
        data=cur.fetchone()
        for i in data:
            o=i
    else:
        
        speak("enter your mobile number")

        no=int(input("Enter your mobile no: "))
        cur.execute("select phone_no from account_details where account_no='%s'"%a)
        data=cur.fetchone()
        for i in data:
            o=i
            
            
    if(no==o):

        
        speak("enter your new pin and conferm your pin")

        new=int(input("Enter your new pin:  "))
        check=int(input("Confirm your new pin:   "))
        if(new==check):
            cur.execute("update account_details set pin='%d' where account_no='%s'"%(new,a))
            mydb.commit()

        
            print("Your pin is successfully changed")
        else:
            print("Correctly enter your new pin")
    else:
        print("ENTER CORRECT DETAILS")
    mydb.commit()    

def space():
    print("")
    print("")
    print("")
    print("")
    print("1.------>Return to starting\n2.------> Exit")

                
print('''                    ^          -------------    |\\    //|
                  // \               ||         ||\\  //|| 
                 //   \              ||         || \\// || 
                //_____\             ||         ||     || 
               //       \            ||         ||     ||
              //         \           ||         ||     || 
             //           \          ||         ||     ||
             ''')
        
print("****************************************************************************")
print("*--------------->  A D V A N C E   A T M   M E C H I N E  <----------------*")
print("*<<<<<<<<<<<<<<<<<<<[ By   R O H I T  $  P U S H P A K  ]<<<<<<<<<<<<<<<<<<*")
print("****************************************************************************")
speak("welcome to ATMkaro")
print('')


def start():
    while True:
        s = 1

        print("")
        print("")
        print("")
        print("")
        
        print("--------------------------------------")
        print("| 1.------> Create Account            |\n| 2.------> Cash Withdrawl & Details  |\n| 3.------> Change Pin                |\n| 4.------> Exit                      |")
        print("--------------------------------------")
        print("")

        speak("enter your choice ")
        
        a=int(input("Enter your choice: "))
        
        if(a==1):
            makeaccount()

            space()
            
            b=int(input("Enter your choice "))
            if(b==1):
                continue
            else:
                print("EXIT")
                break
            


        elif(a==3):
            changepin()
            
            space()
            
            b=int(input("Enter your choice "))
            if(b==1):
                continue
            else:
                print("EXIT")
                break
            

        elif(a==2):
            print("")

            speak("Enter your account number")
            

            x=int(input('Enter your account no: '))
            cur.execute("select * from account_details")
            n=cur.fetchall()
            for i in n:
                if(x==i[2]):
                    a=x
            if(x==a):
                
                print("")
                speak("enter your pin")
                pin=int(input("Enter pin: "))
                cur.execute("select pin from account_details where account_no='%s'"%x)
                data=cur.fetchone()
                for i in data:
                    a=i
                if pin == a:

                    print("")
                    print("")
                    print("___________________________________")
                    print("| 1.------> Cashwithdrawal         |\n| 2.------> Balance Enqiury        |\n| 3.------> Transter Money         |\n| 4.------> Account Details        |\n| 5.------> Lucky Draw             |\n| 6.------> Exit                   | ")
                    print("|__________________________________|")
                    print("")
                    speak("enter your choice")
                    choice=int(input("Enter your choice:   "))
                    print("")
                    print("")


                    if(choice==1):
                        
                        cashwithdrawal()


                        space()
                        
                        b=int(input("Enter your choice: "))
                        if(b==1):
                            continue
                        else:
                            print("")
                                
                            print("EXIT")
                            break


                            
                    elif(choice==2):
                        
                        balance()

                        space()

                        b=int(input("Enter your choice: "))
                        if(b==1):
                            continue
                        else:
                            print("")
                            print("EXIT")
                            break
                    
                    elif(choice==5):
                        
                            luckydraw(s)
                            s+=1                        
                                    
                            space()

                            b=int(input("Enter your choice: "))
                            if(b==1):
                                continue
                            else:
                                    
                                print("EXIT")
                                break
                            

                    elif(choice==3):
                        tranfermoney()

                        space()

                            
                        b=int(input("Enter your choice: "))
                        if(b==1):
                            continue
                        else:
                            print("")
                            print("EXIT")
                            break
                    
                            

                    elif(choice==4):
                        account_view()

                        space()
                        
                        b=int(input("Enter your choice: "))
                        if(b==1):
                            continue
                        else:
                            print("")
                            print("EXIT")
                            break
                    
                        
                    else:
                        print("")
                        print("EXIT")
                        break
                    
                else:
                    print("")
                    if(m<=1):
                        print("Please! Enter Correct Pin.")
                        print("\nTry once more")
                        m+=1
                    else:
                        print("YOUR ACCOUNT IS BLOCKED ")
                        break
                    
            elif(x!=a):
                print("INVALID ACCOUNT NUMBER")
                break
            
        else:
            print("")
            speak("THANKS FOR VISITING")
            print("EXIT")
            break
        mydb.commit()

print("")
speak("Enter Any random number between 1 to 10")
m=int(input('Enter a number between 1 to 10: '))
if(m>=1)and(m<=10):
    start()
    print("Chalo")

else:
    print('TYPE CORRECT NUMBER')
    
