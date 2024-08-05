str2 = "Hello Good rning , WeAre Learning Pytho Programming"
# output = "Hello rning WeAre Pytho"
output= "" # "Hello rning WeAre "
word_list = str2.split(" ")
for word in word_list:
    if len(word) == 5:
        output = output + word + " "
    else:
        continue

print("result :", output)