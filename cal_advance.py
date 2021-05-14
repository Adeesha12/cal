from operator import truediv, mul, sub, add

input_equation = input("please enter equation: ")
lst_input = list(input_equation) 

number_list = []
new_number_list = []
counts=0

operators = {
    "*" : mul,
    "/" : truediv,
    "+" : add,
    "-" : sub 
}

for i in lst_input:
    counts += 1
    if i.isdigit():
        number_list.append(i) 
        if counts == len(lst_input):
            new_number = ''.join(number_list)
            new_number_list.append(new_number)
    else:
        new_number = ''.join(number_list)
        new_number_list.append(new_number)
        new_number_list.append(i)
        number_list.clear()

def calculation(lst,ptrn):
    if len(lst) == 1:
        answer = lst[0]
        return answer
    else:
        for O in ptrn:
            if O in lst:
                indx = lst.index(O)
                temp = operators[O](float(lst[indx-1]),float(lst[indx+1]))
                lst[indx-1:indx+2] = [temp]
                return calculation(lst,ptrn)

pattern=[]
def operation_pattern(ls):
    for element in ls:
        if not(element.isdigit()): 
            pattern.append(element)
    temp1=[]
    temp2=[]
    for p in pattern:
        if p in ['*','/']:
           temp1.append(p) 
        else:
            temp2.append(p)
    return temp1 + temp2

opr = operation_pattern(new_number_list)
answer = calculation(new_number_list,opr)

print(answer)
