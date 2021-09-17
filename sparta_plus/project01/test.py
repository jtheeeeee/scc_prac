name ='홍길동'
age='30'
hello=f'제 이름은 {name}입니다. 나이는 {age}입니다.'
print(hello)

from datetime import datetime

today = datetime.now()
mytime = today.strftime('%Y년 %m월 %d일 %H시 %M분 %S초'.encode('unicode-escape').decode()
    ).encode().decode('unicode-escape')
filename = f'file-{mytime}'
print(filename)