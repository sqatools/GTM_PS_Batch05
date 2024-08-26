# Python program to sort a dictionary using values

dict1 = {'d':14,'b':52,'a':13,'c': 1}

sorted_ = {key: value for key, value in
             sorted(dict1.items(), key=lambda item: item[1])}
print(sorted_) # {'c': 1, 'a': 13, 'd': 14, 'b': 52}