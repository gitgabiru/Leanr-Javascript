n = int(input())

for i in range(n):
 s = input()
 s = s.lower()
 print(s)
 lista = []
 c = False
 if s[0] == 'p' or s[0] == 'b':
  c = False
else:
  if(s.count('p') == 0 and s.count('b') == 0):
   c = True
  else: 
   for i in s:
    lista.append(i)
   for i in range(1, len(lista)):
    if lista[i-1] == 'm':
     if lista[i] == 'b' or lista[i] == 'p':
      c = True
 if c:
  print('Certa')
 else:
  print('Errada')
 lista = []