price = 0

# 1. 도민/국가유공자 인가?
answer = input("제주도민 또는 국가유공자인가요?(예/아니오)")
if answer == "예":
  price = 0
else :
  # 2. 군인인가?
  answer = input("군인인가요?(예/아니오)")
  if answer == "예":
    # 군인이면서 나이가 65세 이상인 경우
    price = 1500
    answer= input("65세 이상이신가요?")
    if answer =="예":
        price=0
  else :
    # 3. 나이에 따라 분류
    age = int(input("몇살인가요?"))
    if 0 <= age <= 6:
      price = 0
    elif 7 <= age <= 24:
      price = 1500
    elif 25 <= age <=64:
      price = 3000
    elif age >= 65:
      price = 0

if price == 0:
  print("무료입니다.")
else:
  

  print(f"{price}원 입니다.")
  # 거스름돈 계산
  answer= int(input("현금을 투입해주세요"))
  final=int(answer-price)
  print(f"거스름돈은{final}원 입니다")