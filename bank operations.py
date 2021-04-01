question='Lets rock'
print(question)
account_state=0
count=0
while question!='No':
    ADD=input('Please enter a sum to top up an account: ')
    SUB=input('Please enter a transaction sum: ')
    ADD=float(ADD)
    SUB=float(SUB)
    account_state+=ADD-SUB
    if ADD==0 and SUB==0:
        count=count
    else:
        count+=1
    print(account_state)
    print(count)
    question = input('If u wanna make another operation pls type: "Yes" or "No: ')