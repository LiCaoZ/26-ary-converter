# 26 进制转换器

tmp = str(input("在这里键入字母\n"))
length = len(tmp)
tmp = tmp.replace('a', '1 ').replace('b', '2 ').replace('c', '3 ').replace('d', '4 ').replace('e', '5 ').replace('f', '6 ').replace('g', '7 ').replace('h', '8 ').replace('i', '9 ').replace('j', '10 ').replace('k', '11 ').replace('l', '12 ').replace('m', '13 ').replace('n', '14 ').replace('o', '15 ').replace('p', '16 ').replace('q', '17 ').replace('r', '18 ').replace('s', '19 ').replace('t', '20 ').replace('u', '21 ').replace('v', '22 ').replace('w', '23 ').replace('x', '24 ').replace('y', '25 ').replace('z', '26 ').rstrip()
tmp = tmp.split(' ' , length)

result = 0

i = 0

o = length - 1

while i < length:
    cal = int(tmp[i]) * 26 ** o
    result = result + cal
    i = i + 1
    o = o - 1
    continue

print(result)
