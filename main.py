# 26 进制转换器

tmp = str(input("在这里键入字母\n"))
length = len(tmp)
tmp = tmp.replace('a', '1 ').replace('b', '2 ').replace('c', '3 ').replace('d', '4 ').replace('e', '5 ').replace('f', '6 ').replace('g', '7 ').replace('h', '8 ').replace('i', '9 ').replace('j', '1 0').replace('k', '1 1').replace('l', '1 2').replace('m', '1 3').replace('n', '1 4').replace('o', '1 5').replace('p', '1 6').replace('q', '1 7').replace('r', '1 8').replace('s', '1 9').replace('t', '2 0').replace('u', '2 1').replace('v', '2 2').replace('w', '2 3').replace('x', '2 4').replace('y', '2 5').replace('z', '2 6').rstrip()
tmp = tmp.split(' ' , length)

result = 0

i = length - 1

if length == 1:
    result = int(tmp[0])
else:
    while i > 0:
        cal = int(tmp[i]) * 26 ^ i
        result = result + cal
        i = i - 1
        if i == 0:
            break

print(result)
