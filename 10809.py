alphabet = [chr(i) for i in range(97,123)]

str1 = input()

for i in alphabet:
    print(str1.find(i), end = ' ')