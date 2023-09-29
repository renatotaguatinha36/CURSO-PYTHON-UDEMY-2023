# 1. Short-circuit "or" operator (looks for the first falsy value)
print('apple' or 'banana' or 'strawberry')
print('apple' or print('CALLED') or 'banana' or 'strawberry')
print('' or print('CALLED') or 'banana' or 'strawberry')
print('' or 0 or [] or {} or print('CALLED'))
print('apple' or 'banana')


# 2. Short-circuit "and" operator (looks for the first truthy value)
print('apple' and 'banana')
print('apple' and 'banana' and 'strawberry')
print('' and 'banana' and 'strawberry')
print(0 and 'banana' and 'strawberry')
print(0 and print('CALLED') and 'banana' and 'strawberry')
print(10 > 100 and print('CALLED') and 'banana' and 'strawberry')
print('apple' and print('CALLED') and 'banana' and 'strawberry')
print('apple' and 'banana' and 'strawberry')


# 3. Logical operators could be chained
print('apple' or 'banana' and 'strawberry')


# 4. Round brackets impact order of the operands evaluation
print(('apple' or 'banana') and 'strawberry')


# 5. Result of entire expression with "or" is truthy if any of the operands is truthy
my_list = [1, 2]
other_list = ['a', 'b']

print(my_list or other_list)


# 6. Round brackets impact order of the operands evaluation
my_list = []
other_list = [1]

print(not not (my_list or other_list))


# 7. "and" operator instead of the if statement
my_list = [1, 2]

if my_list:
    print("List is not empty")

my_list and print("List is not empty")
