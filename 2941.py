# 크로아티아 알파벳
# replace 함수

c_alphabet = input()

alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alphabets:
    c_alphabet = c_alphabet.replace(i,'*')
print(len(c_alphabet))