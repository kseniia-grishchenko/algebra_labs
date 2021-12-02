from itertools import zip_longest
import copy as cp


class LongNumber:
    def __init__(self, s):
        self.digits = []
        c = 1
        self.BASE = 10
        try:
            if s[0] == '-':
                c = -1
                s = s[1:]
            for i in s:
                self.digits.append(c * int(i))
        except TypeError:
            s = str(s)
            if s[0] == '-':
                c = -1
                s = s[1:]
            for i in s:
                self.digits.append(c * int(i))
        except IndexError:
            pass

    def __str__(self):
        return self.is_negative() * '-' + ''.join([str(abs(i)) for i in self.digits])

    def is_zero(self):
        for i in self.digits:
            if i != 0:
                return False
        return True

    def revert(self):
        self.digits = [-i for i in self.digits]

    def get_reversed_digits(self):
        return list(reversed(self.digits))

    def is_negative(self):
        for i in self.digits:
            if i < 0:
                return True
            if i > 0:
                return False
        return False

    def sign(self):
        if self.is_negative():
            return LongNumber(-1)
        else:
            return LongNumber(1)

    def abs(self):
        return self.sign() * self

    def normalize(self):
        d = self.digits
        for i in range(len(d) - 1, -1, -1):
            self.digit_normalize(i)
        while len(self.digits) > 0 and self.digits[0] == 0:
            self.digits.pop(0)

    def digit_normalize(self, pos):
        c = 1
        if self.is_negative():
            c = -1
        if pos > 0:
            self.digits[pos - 1] += c * (c * self.digits[pos] // self.BASE)
            self.digits[pos] = c * (c * self.digits[pos] % self.BASE)
        elif self.digits[0] >= self.BASE:
            self.digits = [c * (c * self.digits[0] // self.BASE)] + self.digits
            self.digits[1] = c * (c * self.digits[1] % self.BASE)

    def __add__(self, other):
        s = reversed([
            a + b
            for a, b in zip_longest(
                reversed(self.digits),
                reversed(other.digits),
                fillvalue=0
            )])
        ret = LongNumber(list(s))
        if ret.is_zero():
            return LongNumber('0')
        ret.normalize()
        return ret

    def __sub__(self, other):
        subtract = cp.copy(other)
        subtract.revert()
        return self + subtract

    def __mul__(self, other):
        a, b = self.get_reversed_digits(), other.get_reversed_digits()
        ret = LongNumber('0')
        for i in range(len(a)):
            term = [0] * i + [a[i] * j for j in b]
            term.reverse()
            to_add = LongNumber(term)
            to_add.normalize()
            ret += to_add
        ret.normalize()
        return ret

    def __lt__(self, other):
        status = False
        for a, b in zip_longest(
                reversed(self.digits),
                reversed(other.digits),
                fillvalue=0
        ):
            if a < b:
                status = True
            if a > b:
                status = False
        return status

    def __gt__(self, other):
        status = False
        for a, b in zip_longest(
                reversed(self.digits),
                reversed(other.digits),
                fillvalue=0
        ):
            if a < b:
                status = False
            if a > b:
                status = True
        return status

    def __eq__(self, other):
        if not len(self.digits) == len(other.digits):
            return False
        a, b = self.get_reversed_digits(), other.get_reversed_digits()
        for i in range(len(a)):
            if not a[i] == b[i]:
                return False
        return True

    def __le__(self, other):
        return not self > other

    def __floordiv__(self, other):
        a = self.abs()
        zero = LongNumber('0')
        res = LongNumber('0')
        if not (self * other).is_negative():
            while a >= zero:
                a -= other.abs()
                res += LongNumber('1')
            return res - LongNumber('1')
        else:
            while a > zero:
                a -= other.abs()
                res += LongNumber('1')
            return res * LongNumber('-1')

    def __mod__(self, other):
        return self - (self // other) * other

    def __pow__(self, other):
        ret = LongNumber('1')
        i = LongNumber('0')
        if self.is_zero():
            return LongNumber('1')
        elif other.is_zero():
            return LongNumber('1')
        else:
            while not i == other:
                ret *= self
                i += LongNumber('1')
            return ret

    def sqrt(self):
        x = self
        if self == LongNumber('0'):
            return LongNumber('0')
        precise_enough = False
        while not precise_enough:
            old_x = x
            x = (x + self // x) // LongNumber('2')
            if (old_x - x) <= LongNumber('1'):
                precise_enough = True
        return x

    def sum_by_mod(self, other, mod):
        mod1 = self % mod
        mod2 = other % mod

        sum = mod1 + mod2
        sum_mod = sum % mod
        return sum_mod

    def sub_by_mod(self, other, mod):
        mod1 = self % mod
        mod2 = other % mod

        subtraction = mod1 - mod2
        sub_mod = subtraction % mod
        return sub_mod

    def mul_by_mod(self, other, mod):
        mod1 = self % mod
        mod2 = other % mod

        mul = mod1 * mod2
        mul_mod = mul % mod
        return mul_mod

    def div_by_mod(self, other, mod):
        mod1 = self % mod
        mod2 = other % mod

        res_mod = mod1 // mod2
        mod_mod = res_mod % mod
        return mod_mod

    def mod_by_mod(self, other, mod):
        mod1 = self % mod
        mod2 = other % mod

        res_mod = mod1 % mod2
        mod_mod = res_mod % mod
        return mod_mod

    def pow_by_mod(self, other, mod):
        mod1 = self % mod
        mod2 = other % mod

        res_mod = pow(mod1, mod2)
        mod_mod = res_mod % mod
        return mod_mod


    @staticmethod
    def GCD(n1, n2):
        while min(n1, n2) > LongNumber('0'):
            if n1 >= n2:
                n1 %= n2
                continue
            if n2 > n1:
                n2 %= n1
                continue
        return max(n1, n2)

    @staticmethod
    def GCD_n(*args):
        res = args[0]
        for a in args:
            res = LongNumber.GCD(res, a)
        return res

