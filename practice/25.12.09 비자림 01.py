age = int(input("나이를 입력해주세요"))
num1 = "무료"
num2 = "1500원"
num3 = "3000원"
if age< 7 or 64 < age:
    print(f"{num1}입니다")
elif 25>age >6:
    print(f"{num2}입니다")
elif 24< age < 65:
    print(f"{num3}입니다")