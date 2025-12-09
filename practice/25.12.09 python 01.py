start = int(input("시작 수는?"))
end = int(input("끝 수는?"))
num = int(input("정수를 입력하세요:"))
result1 = (f"{num}는 {end}와 {start} 사이에 있다")
result2 = (f"{num}는 {end}와 {start} 사이에 없다")
if start < num < end:
    print(result1)
else:
    print(result2)