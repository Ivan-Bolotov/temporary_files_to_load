a = input()
if '.' not in a:
   print(int(a, 6))
   exit()
cel, drob = a.split('.')
cel = int(cel, 6)
if '(' not in a:
   drob = int(drob, 6) / 6 ** len(drob)
   print(cel + drob)
   exit()
pp = drob[:drob.find('(')]
p = drob[drob.find('(') + 1: -1]
if pp == '':
   drob = int(p, 6) / (6 ** len(p) - 1)
else:
   drob = (int(pp + p, 6) - int(pp, 6)) / (6 ** len(pp + p) - 6 ** len(pp))
print(cel + drob)
 
