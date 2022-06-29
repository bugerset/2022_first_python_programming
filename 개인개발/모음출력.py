# solution 1
word = input("입력값 : ")
word_slice = []

if "a" in word:
    word_slice.append(word.index("a"))
if "e" in word:
    word_slice.append(word.index("e"))
if "i" in word:
    word_slice.append(word.index("i"))
if "o" in word:
    word_slice.append(word.index("o"))
if "u" in word:
    word_slice.append(word.index("u"))

word_slice.sort()

while "a" in word or "e" in word or "i" in word or "o" in word or "u" in word:
    print(word[0:word_slice[0]])
    break
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# solution 2
# word = input("입력값 : ")
# output_word = ""

# 모음 = "aeiou"

# for letters in word:
#     if letters not in 모음:
#         output_word += letters
#     if letters in 모음:
#         break

# print(output_word)
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# solution 3
sentence = input()
vowel = "aeiouAEIOU"

for i in sentence: 
    if i in vowel:
        break
    print(i, end="")