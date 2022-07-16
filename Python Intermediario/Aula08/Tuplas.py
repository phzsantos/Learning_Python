t1 = (1,2,3, 'a', 'Paulo Henrique')

print(t1)
for item in t1:
    print(item)


t1 = 1, 2, 3
# t1 = 1   inteiro
# t1 = 1,  tupla 

print(t1)
for item in t1:
    print(item)


t1 = 1, 2, 'Paulo', 4
t2 = 6, 7, 8
t3 = t1 + t2

n1, n2, n3, *_, n4, n5 = t3

print(n4, n5, _)


t1 = (1,2 ,'Paulo',4,5) * 20

print(t1)


t1 = 1,2,3,4,5
t1 = list(t1)
t1[1] = 3000
print(t1)
t1 = tuple(t1)
print(t1)