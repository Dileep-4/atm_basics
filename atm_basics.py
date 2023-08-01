password = 9542
account_balance = 20000
n = int(input("enter password: "))
a = "withdraw"
b = "balance enquiry"
c = "pin change"
d = "deposit amount"
A = int(input("press 1 or 0: "))
while A==1:
 if n== password:
    D=input("please press 'a' for withdrawl money or 'b' for balance enquiry or 'c' for change ping or 'd' for deposit amount : ")
    for B in D:
      if B=="a":
                withdraw_amount = int(input("enter amount you want to withdraw: "))
                print("withdrawl amount is: ", withdraw_amount)
                print("please take your money ")
                C = int(input("please press 1 or 0: "))
                if C==1:
                    balance = account_balance - withdraw_amount
                    print("your current balance is: ", balance)
                elif C==0:
                    print("thankyou, visit again")
                A=int(input("press 1 or 0: "))
                n = int(input("enter password: "))
      elif B=="b":
                balance_enquiry = print("your bank balance is: ", account_balance)
                A = int(input("press 1 or 0: "))
                n = int(input("enter password: "))
      elif B=="c":
                x = int(input("please enter your old pin: "))
                if n==x:
                    i = int(input("enter your new password: "))
                    pin_change = print("your pin was changed successfully")
                else:
                    print("please check your old pin")
                A = int(input("press 1 or 0: "))
                n = int(input("enter password: "))
      elif B=="d":
                deposit_amount = int(input("please give amount you want to deposit: "))
                print("deposited amount is: ", deposit_amount)
                D = int(input("please press 1 or 0: "))
                if D==1:
                    balance = account_balance+deposit_amount
                    print("your current balance is: ", balance)
                else:
                    print("thankyou")
                A = int(input("press 1 or 0: "))
                n = int(input("enter password: "))
 else:
    print("please check your password")
    break




    print(amount, "$")
