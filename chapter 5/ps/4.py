s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations?

print(len(s))

# answer is 2 because python treats 20 == 20.0