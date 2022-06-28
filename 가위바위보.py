# 가위바위보
import random, time

k = ["가위", "바위", "보"]
print("가위바위보 게임을 시작합니다.")
hand = input("무엇을 내시겠습니까?")
computer = random.choice(k)

while hand not in k:
    print("입력이 이상합니다.")
    hand = input("무엇을 내시겠습니까?")

print("1초후 결과가 나옵니다.")
time.sleep(1)

if computer == "가위":
    print("컴퓨터는 가위를 택했습니다.")
    if hand == "가위":
        print("비기셨네요!")
    elif hand == "바위":
        print("이겼습니다!")
    elif hand == "보":
        print("지셨습니다!")

elif computer == "바위":
    print("컴퓨터는 바위를 택했습니다.")
    if hand == "가위":
        print("지셨습니다!")
    elif hand == "바위":
        print("비겼습니다!")
    elif hand == "보":
        print("이겼습니다!")

else:
    print("컴퓨터는 보를 택했습니다.")
    if hand == "가위":
        print("이겼습니다!")
    elif hand == "바위":
        print("지셨습니다!")
    else:
        print("비겼습니다!")

