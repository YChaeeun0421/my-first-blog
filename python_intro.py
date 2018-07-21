if 5>2:
    print('5 is greater thant 2')
else :
    print('5 is not greater than 2')

#사용자함수만들기
def hi(name):
    if name == 'Leah':
        print('Hello! Leah')
    elif name == 'Yoo':
        print('hello yoo')
    else :
        print('hello stranger~')

value = 'hahah'
hi("Leah")
hi(value)

def hi2(name):
    print('Hi ' + name + '!')

hi2("Rachel")

#사용자로부터 입력받기
name3 = input('이름을 입력하세요:')
print('당신의 이름은 %s입니다.' % name3)
age = input('당신의 나이를 입력하세요')
print('당신의 나이는 %d입니다' % int(age))
print('당신의 이름은 %s이고, 나이는 %d입니다.' %(name3, int(age)))

#for 반복문
girls = ['Rachel', 'leah', 'monica', 'You']
for name4 in girls:
    hi2(name4)
    print('next!')
for i in range(1,6):
    print(i)
for i in range(0,3):
    print(girls[i])

#구구단
number2 = input('숫자를 입력하세요(구구단출력): ')
for i in range(1,10):
    mult = int(number2) * i
    print('%d * %d = %d' %(int(number2), i, mult))

#혈액형
data = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'AB', 'O']
result ={}
for blood_type in data:
    if blood_type in result:
        result[blood_type] += 1
    else:
        result[blood_type] = 1

print(result)