name="Ashutosh"
lower_name=name.lower()
print(lower_name)
count_vowel=0

# for i in range(0,8):
#     if ch=="a" or ch=="e" or ch=="i" or ch=="o" or lower_name[i]=="u":
#         count_vowel+=1
# print(count_vowel)        

for ch in name:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        count_vowel+=1
print(count_vowel)  