total = int(input('What is the total amount: \t'))
def tasks():
    global task
    task = input('What do you want : (a) Withdraw (b) Deposit (c) Total Amount \n')
tasks()
while True:
    if 'a' in task:
        withdraw_amount = int(input('Enter amount you want to withdraw: \t'))
        print(f'Ok , you have withdrawn {withdraw_amount} from your total amount \n')
        total = total - withdraw_amount      
        tasks()

    elif 'b' in task:
        deposit_amount = int(input('Enter the amount you want to deposit: \t'))
        print(f'Ok, you have now deposited {deposit_amount} to your total amount \n')
        total = total + deposit_amount      
        tasks()

    elif 'c' in task:
        print(total)   
        tasks()