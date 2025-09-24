l = [10,20,30,40,50]
for i in l:
     print(i)
biodata ={
     "name":"sairam",
     "roll no":"g0",
     "branch":"csm",
     "place":"maisamgudda",
     "role":"backend developer"
 }
for i in biodata:
     print(i)
for i in biodata.keys():
        print(i)
for i in biodata.items():
     print(i)

#nested dictionary

students = {
     "s1":('name':'farhan','roll no':'g0')
     "s2":('name':'dhanush','roll no':'f5')
     "s3":('name':'sidhartha','roll no':'f0')
}
print(students["s1"]['name'])
print(students["s2"]['name'])
print(students["s3"]['name'])
print(students["s1"]['roll no'])
print(students["s2"]['roll no'])
print(students["s3"]['roll no'])
