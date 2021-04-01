question='Lets rock'
print(question)
account_state=0
count=0
def get_and_transform()->float:
    """Get from keybord a sum to add for account and transaction sum.
    Transform it for float type date and make difference"""
    ADD = input('Please enter a sum to top up an account: ')
    SUB = input('Please enter a transaction sum: ')
    ADD = float(ADD)
    SUB = float(SUB)
    return  ADD-SUB
def check_in(get_and_transform:float)->int:
    """Checking result of function 'get_and_transform """
    if get_and_transform==0:
        return 0
    else:
        return 1
while question!='No':
    account_state+=get_and_transform()
    count+=check_in(get_and_transform)
    print(account_state)
    print(count)
    question = input('If u wanna make another operation pls type: "Yes" or "No: ')
