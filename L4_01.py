'''1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трёх уроков.
'''


import math
import timeit


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


NUMBER_EXECUTIONS = 1
TEST_VALUE = 1000

time1 = timeit.timeit(f'no_eratosthenes({TEST_VALUE})',
                      setup='from __main__ import no_eratosthenes',
                      number=NUMBER_EXECUTIONS)

time2 = timeit.timeit(f'eratosthenes({TEST_VALUE})',
                      setup='from __main__ import eratosthenes',
                      number=NUMBER_EXECUTIONS)

print(f'Программа без использования алгоритма «Решето Эратосфена» быстрее \
программы с использованием алгоритма «Решето Эратосфена» в \
{round(time2 / time1, 2)} раз'
      )