#sets
s31 = {}
s3 = set()
print(type(s31))

#accessing sets:
a = {"rajini kanth","lime","red"}
for role in a:
    print(role)

#discard
s = {18,7,33,45,23,46}
s.discard(50)
print(s)
s = {18,7,33,45,23,46}
s.pop()
print(s)

a = {1,2,3,4}
b = {3,4,5,6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#sort
