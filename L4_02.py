'''2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
'''


import math


def no_eratosthenes(i):
    '''Без использования алгоритма «Решето Эратосфена»
    '''

    prime = [2]
    number = 3
    while len(prime) < i:
        flag = True
        for j in prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            prime.append(number)
        number += 1
    return prime[-1]


def eratosthenes(i):
    '''Используя алгоритм «Решето Эратосфена»
    '''

    i_max = prime_counting_function(i)
    prime = [_ for _ in range(2, i_max)]

    for number in prime:
        if prime.index(number) <= number - 1:
            for j in range(2, len(prime)):
                if number * j in prime[number:]:
                    prime.remove(number * j)
        else:
            break
    return prime[i - 1]


def prime_counting_function(i):

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


user_number = int(input('Введите номер по счету простого числа: '))
print(no_eratosthenes(user_number))

print('Алгоритм 1 без использования алгоритма «Решето Эратосфена»')
print(
    f'{no_eratosthenes(user_number)} - {user_number} \
по счёту простое число'
)

print('Алгоритм 2 с использованием алгоритма «Решето Эратосфена»')
print(
    f'{eratosthenes(user_number)} - {user_number} по счёту простое число'
)