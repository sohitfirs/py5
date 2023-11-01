# Задание 1

s1 = str(input())
print(s1, s1[::-1])
if s1 == s1[::-1]:
    print('YES')
else:
    print('NO')

# Задание 2

s2 = str(input())
if len(s2) > 1000:
    print('ERROR')

s2 = s2.strip()
s2 = s2.split(' ')

s3 = list('')

for i in range(len(s2)):
    if s2[i] != '':
        str(s3.insert(i, s2[i]))

print(' '.join(s3))
