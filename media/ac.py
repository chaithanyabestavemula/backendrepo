import json
f=open('assess','r')
r=f.readlines()
p=r[0]
y=json.loads(p)
avg=[]
total=[]
c=0
mtot,ctot,ptot,tot=0,0,0,0
#--------------------------------------------------------------
det={}
for i in range(len(y)):
    det[y[i].get('name')]=y[i]
for i in sorted(det.keys()):
    print(det.get(i))
#----------------------------------------------------------------------
for i in range(len(y)):
    mtot+=y[i].get('mathmarks')
    ctot+=y[i].get('chmarks')
    ptot+=y[i].get('phymarks')

tot+=mtot+ctot+ptot
avg.append(mtot//3)
avg.append(ctot//3)
avg.append(ptot//3)
print("avg marks in each subject",avg)
print("avg total marks",tot//3)
for i in range(len(y)):
    mto=y[i].get('mathmarks')
    cto=y[i].get('chmarks')
    pto=y[i].get('phymarks')
    total.append(mto+cto+pto)
    if mto>avg[0] and pto<avg[2]:
        print(" students who scored above average scores in maths but below average in physics:",y[i].get('name'))
    if mto>avg[0] and cto>avg[1] and pto>avg[2]:
        c+=1
print("total marks of each student:",total)
for i in range(len(total)):
    if total[i]>tot//3:
        print("students who scored greater than avg tot marks:",y[i].get('name'))
for i in range(len(total)):
    if total[i]>0.1*(tot//3)+tot//3:
        print("students scored 10%above avg totmarks:",y[i].get('name'))
    elif total[i]>=(tot//3)-0.1*(tot//3):
        print("students scored 10% below avg totmarks:",y[i].get('name'))
print("Number of students who scored above average in all the 3 subjects:",c)
--------------------------------------------------------------

