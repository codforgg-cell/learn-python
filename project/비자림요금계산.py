type = input("군인이나 국가 유공자이신가요?")
price = 0
if type == "yes":
    print(f"{price}원입니다")
type = input("제주도민이신가요")
if type == "yes":
    print(f"{price}원입니다")
age= int(input("나이를 입력해주세요"))

price = 0
if 6<age<25:
    price = 1500
elif 24<age<65:
    price = 3000
print(f"{price}원 입니다")s