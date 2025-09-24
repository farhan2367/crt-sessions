#tuple 
coordinates = ("x","y")
My_tuple = (10,20,30)
print(My_tuple)
print(type(My_tuple))

#tuple with single element
a = 10
print(type(a))
b = [10]
print(type(b))
c = (10)
print(type(c))

#accessing elements:
a = (10,20,30,40)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
#slicing the tuple

a = (10,20,30,40)
print(a[1:3])
print(a[:2])
print(a[-1:-3])

#changing the value:
a[1] = 50
#append
#