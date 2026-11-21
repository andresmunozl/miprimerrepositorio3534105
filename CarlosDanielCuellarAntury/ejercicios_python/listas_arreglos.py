numbers =   [342, 678, 854, 20, 8123, 000, 777, 666, 777]

numbers.append(10)
print(numbers)

numbers.remove(342)
print(numbers)

print(numbers.count(342))
numbers.sort()
print(numbers)

print(len(numbers))

for element in range(len(numbers)):
    print(numbers[element])
    print(type(numbers[element]))
cont = 0
while len(numbers) > cont:
    print(numbers[cont])
    print(type(numbers[cont]))
    cont += 1