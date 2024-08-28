# Python file program to get all odd and even length words in two lists

open_file = open('odd_even_file')
words = open_file.read().split()
even = []
odd = []

for word in words:
    if len(word) % 2 == 0:
        even.append(word)
    else:
        odd.append(word)

print("Words having even length:", even) # Words having even length: ['This', 'is', 'This', 'is', 'This', 'is', 'Canada', 'This', 'is', 'This', 'is', 'Africa', 'This', 'is', 'This', 'is', 'This', 'is']
print("Words having odd length:", odd) # Words having odd length: ['Line1', ':', 'India', 'Line2', ':', 'America', 'Line3', ':', 'Line4', ':', 'Australia', 'Line5', ':', 'Line6', ':', 'Korea', 'Line7', ':', 'Germany', 'Line8', ':', 'China']