x = 10
y = 'Luiz'

z = x
x = y
y = z

print(f'x={x} e y={y}')

x = 10
y = 'Luiz'

x, y = y, x

print(f'x={x} e y={y}')

x = 10
y = 'Luiz'
z = 'Otavio'

x, y, z = z, x, y

print(f'x={x} e y={y} e z={z}')
