import collections
d = dict()
j=0
f=[]
marks= [('John', ('Physics', 80)), ('Daniel', ('Science', 90)), ('John', ('Science', 95)),
              ('Mark', ('Maths', 100)), ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]
d=dict()
for student in marks:

    if student[0] in list(d.keys()):
        ([d [student[0]].append(student[1])])
    else:
        d.update({student[0]: [student[1]]})
print("{")
for person in d:
   print (person, ":", sorted(d[person]))
print("}")