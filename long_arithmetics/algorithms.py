from random import randint
from LongNumber import LongNumber


def pollard_factorization(N):
    random_x = randint(1, N - 2)
    x = LongNumber(str(random_x))
    y = LongNumber('1')
    counter = LongNumber('0')
    n = LongNumber(str(N))
    stage = LongNumber('2')
    sub = x - y
    d = LongNumber.GCD(n, sub.abs())
    while d <= LongNumber('1'):
        if counter == stage:
            y = x
            stage *= LongNumber('2')
        x = (x * x + LongNumber('3')) % n
        counter += LongNumber('1')
        sub = x - y
        d = LongNumber.GCD(n, sub.abs())
    root = LongNumber.GCD(n, sub.abs())
    return root


def phi(N):
    res = LongNumber(str(N))
    i = LongNumber('2')
    n = LongNumber(str(N))
    while i * i <= n:
        if n % i == LongNumber('0'):
            while n % i == LongNumber('0'):
                n //= i
            res -= res // i
        else:
            i += LongNumber('1')
    if n > LongNumber('1'):
        res -= res // n
    return res


def is_prime(n):
    if n < LongNumber('2'):
        return False
    i = LongNumber('2')
    while i < n + LongNumber('1'):
        if i * i <= n and n % i == LongNumber('0'):
            return False
        i += LongNumber('1')
    return True


def mobius(N):
    n = LongNumber(str(N))
    if n == LongNumber('1'):
        return 1
    p = LongNumber('0')
    i = LongNumber('1')
    while i < n + LongNumber('1'):
        if n % i == LongNumber('0') and is_prime(i):
            if n % (i * i) == LongNumber('0'):
                return 0
            else:
                p = p + LongNumber('1')
        i += LongNumber('1')
    if p % LongNumber('2') == LongNumber('0'):
        return 1
    else:
        return -1


def legendre(A, P):
    a = LongNumber(str(A))
    p = LongNumber(str(P))
    a %= p
    if a == LongNumber('0'):
        return LongNumber('0')
    elif p == LongNumber('3'):
        if a == LongNumber('0'):
            return LongNumber('0')
        elif a == LongNumber('1'):
            return LongNumber('1')
        else:
            return LongNumber('-1')
    else:
        x = LongNumber('0')
        while x < p:
            if (x * x) % p == a:
                return LongNumber('1')
            x += LongNumber('1')
        return LongNumber('-1')


def jacobi(A, N):
    a = LongNumber(str(A))
    n = LongNumber(str(N))
    t = LongNumber('1')
    while a != LongNumber('0'):
        while a % LongNumber('2') == LongNumber('0'):
            a //= LongNumber('2')
            r = n % LongNumber('8')
            if r == LongNumber('3') or r == LongNumber('5'):
                t = LongNumber('-1') * t
        a, n = n, a
        if a % LongNumber('4') == n % LongNumber('4') == LongNumber('3'):
            t = LongNumber('-1') * t
        a %= n
    if n == LongNumber('1'):
        return t
    else:
        return LongNumber('0')


def baby_step_giant(a, b, m):
    n = int(m ** 2 + 1)
    a_n = 1
    for i in range(n):
        a_n = (a_n * a) % m
    value = [0] * m
    cur = a_n
    for i in range(1, n + 1):
        if value[cur] == 0:
            value[cur] = i
        cur = (cur * a_n) % m

    cur = b
    for i in range(n + 1):
        if value[cur] > 0:
            ans = value[cur] * n - i
            if ans < m:
                return ans
        cur = (cur * a) % m
    return -1


def cipolla(A, P):
    a = LongNumber(str(A))
    p = LongNumber(str(P))
    if legendre(a, p) != LongNumber('1') or a == LongNumber('0'):
        return LongNumber('0')
    elif p == LongNumber('2'):
        return p
    elif p % LongNumber('4') == LongNumber('3'):
        return pow(int(str(a)), (int(str(p)) + 1) // 4, int(str(p)))

    s = p - LongNumber('1')
    i = LongNumber('0')
    while s % LongNumber('2') == LongNumber('0'):
        s //= LongNumber('2')
        i += LongNumber('1')

    n = LongNumber('2')
    while legendre(n, p) != LongNumber('-1'):
        n += LongNumber('1')

    x = LongNumber(str(pow(int(str(a)), (int(str(s)) + 1) // 2, int(str(p)))))
    b = LongNumber(str(pow(int(str(a)), int(str(s)), int(str(p)))))
    g = LongNumber(str(pow(int(str(n)), int(str(s)), int(str(p)))))
    r = i

    while True:
        k = b
        m = LongNumber('0')
        while m < r:
            if k == LongNumber('1'):
                break
            k = LongNumber(str(pow(int(str(k)), 2, int(str(p)))))
            m += LongNumber('1')

        if m == LongNumber('0'):
            return x

        gs = pow(int(str(g)), 2 ** (int(str(r)) - int(str(m)) - 1), int(str(p)))
        gs = LongNumber(str(gs))
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def miller_rabin(n, k=5):
    if n < 2:
        return False
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d // 2
    for i in range(k):
        rand = randint(2, n - 1)
        x = pow(rand, d, n)
        if x == 1 or x == n - 1:
            continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True
