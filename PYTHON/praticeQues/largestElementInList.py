def largest(numbers):
    large=numbers[0]
    for num in numbers:
        if(num>large):
            large=num
    return large

list=[12,21,32,89,9]
result=largest(list)
print(result)
