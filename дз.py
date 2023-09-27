a = int(input())
b = int(input())
c = int(input())

d=b**2 - 4*a*c
if d<0:
    print ("Решений нет")
elif d==0:
    print ("1 корень - ", -b/(2*a))
else:
    print ("Первый корень - ", (-b + d ** 0.5) / (2 * a))
    print ("Второй корень - ", (-b - d ** 0.5) / (2 * a))