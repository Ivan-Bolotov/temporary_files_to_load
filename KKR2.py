def NOD(n,m):
   if m == 0: return n
   return NOD(m, n % m)
n, m = map(int, input().split())
R = ''
if n * m < 0 or n < 0: #проверка на минусы
   if n * m > 0:
       n = -n
       m = -m
   else:
       R = '-'
       n = abs(n)
       m = abs(m)
if m == 0:
   print('Деление на ноль')
   exit()
def pp(n):
   s = ''
   while n:
       s = str(n % 3) + s
       n //= 3
   return s
if n % m == 0: 
   print(pp(n//m))
   exit()
if n > m:
   nd = NOD(n, m)
   n //= nd
   m //= nd
   R += pp(n//m) + '.'
   n = n % m
else:
   R += '0.'
L = [n]
while n != 0:
   n *= 3
   R += str(n // m)
   n = n % m
   if n in L:
       R = R[: R.find('.') + L.index(n) + 1] + '(' + R[R.find('.') + L.index(n) + 1:] + ')'
       break
   else:
       L.append(n)
print(R)
