print("사전 프로그램 시작... 종료는 q를 입력")
dictionary = {}

while True:
    st = input("$ ")
    command = st[0]
    if command == "<":
        st = st[1:]
        inputStr = st.split(":")
        if len(inputStr) < 2:
            print("오류 발생")
        else:
            dictionary[inputStr[0].strip()] = inputStr[1].strip()
    elif command == ">":
        st = st[1:]
        inputStr = st.strip()
        if inputStr in dictionary:
            print(dictionary[inputStr])
        else:
            print("{}가 사전에 없습니다.".format(inputStr))
    elif command == "q":
        break
    else:
        print("입력 오류 발생")

print("사전 프로그램 종료")