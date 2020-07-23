from django.shortcuts import render
from django.http import HttpResponse
from example.models import User

user = User("4321", "user1", "9921", 2000)

#Check Balance

def checkbalance(request):
    return render(request,'checkbalance.html', {'action':'Check Balance','user':user})

def displaybalance(request):
    result = ""
    error = ""

    acc_no = request.POST.get('accno')
    password = request.POST.get('pwd')

    if(acc_no == "" or password == "" or amount == ""):
        error = 'Error : Please enter Account number, Password and Amount'
    else:
        if(user.acc_no == acc_no and user.password == password):
            result = user
        else:
            error = 'Error : Please check Account number and Password'

    return render(request,'result.html', {'action':'Check Balance','user':result, 'error':error})

#Cash Withdrawal

def withdrawal(request):
    return render(request,'withdrawal.html', {'action':'Cash Withdrawal'})

def displaywithdrawal(request):
    result = ""
    error = ""
    msg = ""

    acc_no = request.POST.get('accno')
    password = request.POST.get('pwd')
    amount = request.POST.get('amt')

    if(acc_no == "" or password == "" or amount == ""):
        error = 'Error : Please enter Account number, Password and Amount'
    else:
        if(user.acc_no == acc_no and user.password == password):
            if(user.balance > int(amount)):
                user.balance = user.balance - int(amount)
                result = user            
                msg = 'Withdrawal Successful! Current balance'
            else:
                error = 'Error : Insufficient Balance'
            
        else:
            error = 'Error : Please check Account number and Password'    
    return render(request,'result.html', {'action':'Cash Withdrawal','user':result, 'msg':msg, 'error':error})

#Cash Deposit

def deposit(request):
    return render(request,'deposit.html', {'action':'Cash Deposit'})

def displaydeposit(request):
    result = ""
    error = ""
    msg = ""

    acc_no = request.POST.get('accno')
    password = request.POST.get('pwd')
    amount = request.POST.get('amt')

    if(acc_no == "" or password == "" or amount == ""):
        error = 'Error : Please enter Account number, Password and Amount'
    else:
        if(user.acc_no == acc_no and user.password == password):
            user.balance = user.balance + int(amount)
            result = user            
            msg = 'Deposit Successful! Current balance'
        else:
            error = 'Error : Please check Account number and Password'
    return render(request,'result.html', {'action':'Cash Deposit','user':result, 'msg':msg, 'error':error})

#Change Password

def changepassword(request):
    return render(request,'changepassword.html', {'action':'Change Password'})

def displaychangepassword(request):
    result = ""
    error = ""
    msg = ""

    acc_no = request.POST.get('accno')
    old_password = request.POST.get('oldpwd')
    new_password = request.POST.get('newpwd')

    if(acc_no == "" or old_password == "" or new_password == ""):
        error = 'Error : Please enter Account number, Old Password and New Password'
    else:
        if(user.acc_no != acc_no):
            error = 'Error : Please check Account number'
        elif(user.password != old_password):
            error = 'Error : Wrong Password.  Please check Old Password'
        else:
            user.password = new_password
            result = user
            msg = 'Change Password Successful'
    return render(request,'result.html', {'action':'Change Password','user':result, 'msg':msg, 'error':error})