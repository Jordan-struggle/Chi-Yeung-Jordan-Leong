import math 

#1.a 
a= 3
b= 4 
c= math.sqrt(a**2+b**2)
print (c)

#1.b
c= 7
a=5
b=math.sqrt(c**2-a**2)
print(format(b, ".2"))

#2
p=365
o=300
q= (300/365)
print ("The accuracy is ", format(q, ".2%"))

#3
tp=2
fp=2
fn=11
tn=985
accuracy = ((tp+tn)/(tp+tn+fp+fn))
print ("To calculate the accuracy this is a good model and the accuracy is", accuracy)

#4
x1= 0
x2= 4
y1= 1
y2= 4
k= ((y2-y1)/(x2-x1))
print("k value is", k, "\nwhile using the k value lets plug one of the coordinates that being (4,4) into the function")
y=4
x=4
m=(y/x)
print("The m value is", m , )
print ("The function is y=", k, "x+", m, sep="")

#5
xp1 = 3
xp2 = -2
yp1 = 4
yp2 = 5
d = math.sqrt((xp1 - xp2)**2 + (yp1 - yp2)**2)
print (format(d, ".2"))

#6
l1= 2
k2=1
j3=4
h1=3
g2=1
f3=0
d= math.sqrt((l1-h1)**2+ (k2-g2)**2 + (j3-f3)**2)
print (format(d, ".3"))