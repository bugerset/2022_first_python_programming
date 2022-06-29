import random, time

G_N = int(input("어떤 게임을 하시겠습니까? 1번은 가위바위보, 2번은 369, 3번은 행맨입니다. : ")) # 선택

if G_N == 1: # (n장)
    k = ["가위", "바위", "보"] # 리스트 생성 (n장)
    print("가위바위보 게임을 시작합니다.") # 안내
    hand = input("무엇을 내시겠습니까? : ") # 사용자의 선택 Input (n장)
    computer = random.choice(k) # 랜덤 선택
    while hand not in k: # 입력이 이상할 경우 while로 무한루프 (n장)
        print("입력이 이상합니다.")
        hand = input("무엇을 내시겠습니까? : ") 
    print("2초후 결과가 나옵니다.")
    time.sleep(2) # 바로 결과가 나오는 것보다 텀을 두고 결과를 내야 재미가 있을것 같아서 해보았습니다.
    if computer == "가위": # 컴퓨터가 가위일 경우
        print("컴퓨터는 가위를 택했습니다.")
        if hand == "가위":
            print("비기셨네요!")
        elif hand == "바위":
            print("이겼습니다!")
        elif hand == "보":
            print("지셨습니다!")
    elif computer == "바위": # 컴퓨터가 바위일 경우
        print("컴퓨터는 바위를 택했습니다.")
        if hand == "가위":
                print("지셨습니다!")
        elif hand == "바위":
                print("비겼습니다!")
        elif hand == "보":
                print("이겼습니다!")
    else: # 컴퓨터가 보자기일 경우

        print("컴퓨터는 보를 택했습니다.")
        if hand == "가위":
            print("이겼습니다!")
        elif hand == "바위":
            print("지셨습니다!")
        else:
            print("비겼습니다!")
elif G_N == 2:
    print("싱글플레이가 아닌 멀티플레이를 권합니다.")
    time.sleep(1)
    print("3,6,9가 들어가는 숫자는 x를 입력하시면 됩니다.")
    time.sleep(1)
    print("시작!")
    for i in range(1,101):
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            num = str(input("입력 : "))
            if num == "x":
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
elif G_N == 3:
    Hangman_image = [""" 
  -----
  |   |
  0   |
 /|\  |
 / \  |
      |
^^^^^^^^^^^
""", 
"""
  -----
  |   |
  0   |
 /|   |
 / \  |
      |
^^^^^^^^^^^
""",
"""
  -----
  |   |
  0   |
  |   |
 / \  |
      |
^^^^^^^^^^^
""",
"""
  -----
  |   |
  0   |
  |   |
 /    |
      |
^^^^^^^^^^^
""",
"""
  ------
  |   |
  0   |
  |   |
      |
^^^^^^^^^^^
""",
"""
  ------
  |   |
  0   |
      |
^^^^^^^^^^^
""",
"""
DONE
"""]

    word_list = ["banana", "apple", "goat", "experiment", "state", "benefit", "attitude", \
    "predator", "practice", "value", "concern", "reward", "mess", "match", "outcome", \
        "function", "device", "material", "peak", "crop", "proof", "fabric", "region" \
            "prey", "attempt", "impact", "spirit", "exposure", " range", "pioneer", \
                "rate", "injury", "conflict", "treasure", "illusion", "principle", \
                    "notion", "intake", "absence", "liver", "scope", "comment", \
                        "agent", "poverty", "textile", "wheel", "parrot", "position", \
                            "judgment"] # 단어장

    word_choice = random.choice(word_list) # 랜덤으로 하나 선택

    letters = "" # 빈칸
    alphabet = "qwertyuiopasdfghjklzxcvbnm" # 알파벳
    cnt = 0

    def game_start(): # 안내문 생성
        print("게임을 시작합니다.")
        print("6번의 실패가 생길경우 게임은 실패로 끝납니다.")
        print("같은 단어의 중복입력은 안됩니다.")

    game_start()

    while True:         
        success = True # 성공을 한다면 True로 종결
        print(Hangman_image[cnt])
        for x in word_choice: # 단어를 알파벳으로 분해
            if x in letters: # 알파벳이 입력한 단어에 있는 알파벳일 경우에 
                print(x, end=" ") # 알파벳으로 표현
            else: # 아니라면
                print("_", end=" ") # 밑줄로 표현
                success = False # 못맞춘 경우엔 False로 나타낸다

        print("틀린 횟수는 {}입니다.".format(cnt))

        if success: # 성공 
            print()
            print("성공!")
            print("정답은 {} 였습니다.".format(word_choice))
            break

        if cnt == 6: # 실패
            print("실패입니다.")
            print("정답은 {} 였습니다.".format(word_choice))
            break

        letter = input("입력 : ") # 입력

        if letter in letters: #중복이면 추가 X
            print("입력오류")

        if letter not in letters: # 알파벳이 중복이 아니라면,
            if len(letter) == 1 and letter in alphabet: # 알파벳이 하나고, 숫자가 아니라면
                letters += letter # 단어를 letters에 일단 추가
                if letter not in word_choice: 
                    cnt += 1
            else:
                print("잘못된 입력입니다.")
else:
    print("잘못된 입력입니다.")
