n=int(input('Enter a Number:'))
if n%2==0:
    print(n,'Is An Even Number')
else:
    print(n,'Is An Odd Number')
################################
sum=0

for number in range(1, 51):
    sum += number  # Add each number to the total sum

# Display the final sum
print("The sum of numbers from 1 to 50 is:",sum)

