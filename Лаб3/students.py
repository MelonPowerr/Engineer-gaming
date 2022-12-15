A={}
A["Misha"]={'мужчина', 'отличник'}
A["Sergey"]={'мужчина', 'тройки'}
A["Adel"]={'женщина', 'хорошист'}
A["Kate"]={'женщина', 'тройки'}
i1=i2=i3=i4=0
if 'отличник' in A["Misha"]:
    a="Misha"
    i1 = 1
if 'отличник' in A["Sergey"]:
    a="Sergey"
    i2 = 1
if 'отличник' in A["Adel"]:
    a="Adel"
if 'отличник' in A["Kate"]:
    a="Kate"

if 'хорошист' in A["Misha"]:
    b="Misha"
    i1 = 1
if 'хорошист' in A["Sergey"]:
    b="Sergey"
    i2 = 1
if 'хорошист' in A["Adel"]:
    b="Adel"
if 'хорошист' in A["Kate"]:
    b="Kate"
print(f"{a} и {b} молодцы!!!")
if i1==1:
    print(f"Мужчина есть -- Misha")
if i2==1:
    print(f"Мужчина есть -- Sergey")
if i1==0 and i2==0:
    print(f"Мужчин нет")