def collatz(number):
    if number % 2 == 0:
        print(int(number // 2))
        return int(number // 2)
    else:
        print(int(3 * number + 1))
        return int(3 * number + 1)
print('Введите целое число: ')
try:
    res = int(input())
except ValueError:
    print('Введите целое число')
while res != 1:
    res = collatz(res)