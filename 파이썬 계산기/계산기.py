import time

def How_to_use():
    print("자체제작 계산기입니다.")
    time.sleep(1)
    print("자릿수가 너무 큰 경우 오버플로우가 발생합니다.")
    time.sleep(1)
    print("초기화를 원하시면 C, 종료를 원하시면 Q를 누르세요.")
    time.sleep(1)
    print("초기화나 종료는 기호칸에서 입력하셔야 합니다.")

How_to_use()
    
while True:
    default_value = 0
    입력 = float(input("숫자 : ")) # 0에서 숫자를 적어서 사용하는 방법
    default_value += 입력
    while True:
        기호 = str(input("기호 : ")) # 기호를 받음
        if 기호 == "+": # 만약 기호가 더하기면
            custom_value = float(input("숫자 : "))
            if -99999999999999999 < custom_value < 99999999999999999:
                default_value += custom_value
                print("값 :",default_value)
            else:
                print("잘못된 숫자입니다.")
        elif 기호 == "-": # 만약 기호가 빼기면
            custom_value = float(input("숫자 : "))         
            if -99999999999999999 < custom_value < 99999999999999999:
                default_value -= custom_value
                print("값 :",default_value)
            else:
                print("잘못된 숫자입니다.")
        elif 기호 == "*" or 기호 == "X" or 기호 == "x": # 만약 기호가 곱하기면
            custom_value = float(input("숫자 : "))
            if -99999999999999999 < custom_value < 99999999999999999:
                default_value *= custom_value
                print("값 :",default_value)
            else:
                print("잘못된 숫자입니다.")
        elif 기호 == "/": # 만약 기호가 나누기면
            custom_value = float(input("숫자 : "))
            if -99999999999999999 < custom_value < 99999999999999999:
                default_value /= custom_value
                print("값 :",default_value)
            else:
                print("잘못된 숫자입니다.")
        elif 기호 == "**" or 기호 == "^": # 만약 기호가 제곱이면
            custom_value = float(input("숫자 : "))
            if -99999999999999999 < custom_value < 99999999999999999:
                default_value **= custom_value
                print("값 :",default_value)
            else:
                print("잘못된 숫자입니다.")
        elif 기호 == "%": #만약 기호가 퍼센트면
            default_value = default_value / 100
            print("값 : " + str(default_value))
        elif 기호 == "C": 
            print("값을 0으로 초기화 합니다.")
            default_value = 0
        elif 기호 == "Q":
            break
        else:
            print("잘못된 입력입니다.")
    break
