age= int(input("나이를 입력해주세요"))
price = 0
if 6<age<25:
    price = 1500
elif 24<age<65:
    price = 3000
print(f"{price}원 입니다")