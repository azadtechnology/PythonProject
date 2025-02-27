operand1=int(input('Enter a number: '))
operand2=int(input('Enter a number: '))
operator=(input ('Enter the operator (+,-,*,/):'))

if operator=='+':
    print(operand1+operand2)
elif operator=='-':
    print(operand1-operand2)
elif operator=='*':
    print(operand1*operand2)
elif operator=='/':
    print(operand1/operand2)
else:
    print('None')

print('thank you for using calculator')

