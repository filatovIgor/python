'''
Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7. Внимание: новый список не создавать!!!
'''

counter = 1
limit = 1000
degree = 3
number = 7
variable = 17
NumberList = [i for i in range(limit + 1)]
oddNumberList = []

for counter in range(1, len(NumberList), 2):
    element = float(counter ** degree)
    oddNumberList.append(element)
# print(oddNumberList)

sumOddNumber = 0
for el in oddNumberList:
    condition = float(el / number)
    if condition == int(condition):
        sumOddNumber += el
        # print(el)

print(sumOddNumber)

for counter in range(1, len(NumberList), 2):
    element = float((counter + variable) ** degree)
    oddNumberList.append(element)
# print(oddNumberList)

sumOddNumber = 0
for el in oddNumberList:
    condition = float(el / number)
    if condition == int(condition):
        sumOddNumber += el
    # print(el)

print(sumOddNumber)




