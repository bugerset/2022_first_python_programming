import time

print("싱글플레이가 아닌 멀티플레이를 권합니다.")
time.sleep(1)
print("3,6,9가 들어가는 숫자는 짝을 입력하시면 됩니다.")
time.sleep(1)
print("시작!")
for i in range(1,101):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        num = str(input("입력 : "))
        if num == "짝":
            continue
        elif int(num) != i:
            print("땡")
            break
        else:
            print("땡")
            break
    else:
        num = int(input("입력 : "))
        if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
            print("땡")
            break
        elif num != i:
            print("땡")
            break
