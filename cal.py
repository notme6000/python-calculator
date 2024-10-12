my_list=[]
global a

def calculator():
    a=0
    print("enter {q} for quiting")
    while True:
        user_input =(input("enter the no. for calculation:"))
        if user_input.lower() == 'q':
            print("calculator exited")
            break
        try:
            a = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        value = input("Enter the operator (+,-,*,/,**):")

        if isinstance(my_list, list) and my_list:
            switch_case(value , a)
            print("Result:",my_list[0])
        else:
            my_list.insert(0,a)
            print("Ruesult:", my_list[0])



def switch_case(value,a):
    if value == '+':
        my_list.insert(0, my_list[0] + a)
    elif value == '-':
        my_list.insert(0, my_list[0] - a)
    elif value == '*':
        my_list.insert(0, my_list[0] * a)
    elif value == '/':
        if a != 0:
            my_list.insert(0, my_list[0] / a)
        else:
            print("Error: Division by zero.")
            my_list.insert(0, my_list[0])
    elif value == '**':
        my_list.insert(0, my_list[0] ** a)
    else:
        print("invalid operator")

calculator()