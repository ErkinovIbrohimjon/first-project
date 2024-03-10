bir = float(input('birinchi sonni kiriting: '))
ikki = float(input('ikkinchi sonni kiriting: '))
tanlash = input("qanday amal bajarishni tanlang( + - * /): ")
if tanlash == "+":
    result = bir + ikki
    print(round(result, 3))
elif tanlash == "-":
    result = bir - ikki
    print(round( result, 3))
elif tanlash == "*":
    result = bir * ikki
    print(round( result, 3))
elif tanlash == "/":
    result = bir / ikki
    print(round(result, 3))
else:
    print(f'"{tanlash}" bunday amal qilib bolmaydi!!!')
