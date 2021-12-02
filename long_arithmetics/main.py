from LongNumber import LongNumber
from LongComparison import LongComparison
from SystemLongComparison import SystemLongComparison
from algorithms import *

# # Basic arithmetic operations
# k1 = LongNumber('105')
# k2 = LongNumber('101')
# k3 = LongNumber('-4')
# module = LongNumber('3')
#
# sum = k1 + k2
# print(k1, '+', k2, '=', sum)
#
# sub = k1 - k2
# print(k1, '-', k2, '=', sub)
#
# mul = k1 * k2
# print(k1, '*', k2, '=', mul)
#
# div = k1 // k2
# print(k1, '//', k2, '=', div)
# #
# mod = k1 % k2
# print(k1, '%', k2, '=', mod)
#
# pow = pow(k1, k2)
# print(k1, '^', k2, '=', pow)
#
# less_than = k1 < k2
# print(k1, 'is less than', k2, less_than)
#
# greater_than = k1 > k2
# print(k1, 'is greater than', k2, greater_than)
#
# less_or_equal = k1 <= k2
# print(k1, 'is less or equal than', k2, less_or_equal)
#
# greater_or_equal = k1 >= k2
# print(k1, 'is greater or equal than', k2, greater_or_equal)
#
# equal = k1 == k2
# print(k1, 'is equal to', k2, equal)
#
# whole_of_sqrt = k1.sqrt()
# print('whole of sqrt is', whole_of_sqrt)
#
# sum_by_mod = k1.sum_by_mod(k2, module)
# print(k1, '+', k2, 'by mod', module, ' =', sum_by_mod)
#
# sub_by_mod = k1.sub_by_mod(k2, module)
# print(k1, '-', k2, 'by mod', module, ' =', sub_by_mod)
#
# mul_by_mod = k1.mul_by_mod(k2, module)
# print(k1, '*', k2, 'by mod', module, ' =', mul_by_mod)
#
# div_by_mod = k1.div_by_mod(k2, module)
# print(k1, '//', k2, 'by mod', module, ' =', div_by_mod)
#
# mod_by_mod = k1.mod_by_mod(k2, module)
# print(k1, '%', k2, 'by mod', module, ' =', mod_by_mod)
#
# pow_by_mod = k1.pow_by_mod(k2, module)
# print(k1, '^', k2, 'by mod', module, ' =', pow_by_mod)
#
#
# # Solving system of comparisons
# a1 = LongNumber('13')
# b1 = LongNumber('7')
# m1 = LongNumber('24')
#
# a2 = LongNumber('8')
# b2 = LongNumber('5')
# m2 = LongNumber('75')
#
# c1 = LongComparison(a1, b1, m1)
# c2 = LongComparison(a2, b2, m2)
#
# s = SystemLongComparison([c1,c2])
# answer = s.solve()
# print('x = ', answer[0], '(mod', answer[1], ')')

n1 = 8051
factorization = pollard_factorization(n1)
print('Pollard factorization: ', factorization)

n2 = 36
euler = phi(n2)
print('Euler function: ', euler)

n3 = 6
mobius = mobius(n3)
print('Mobius function: ', mobius)

a1 = 9
p1 = 5
legendre = legendre(a1, p1)
print('Legendre symbol: ', legendre)

a2 = 7
n4 = 15
jacobi = jacobi(a2, n4)
print('Jacobi symbol: ', jacobi)

a3 = 2
b = 1
m = 5
x = baby_step_giant(a3, b, m)
print('Baby step giant step algorithm: ', x)

a4 = 223
n5 = 17
cipolla = cipolla(a4, n5)
print("Cipolla's algorithm: ", cipolla)

n = 4
is_prime = miller_rabin(n)
print("Miller-Rabin test: ", is_prime)