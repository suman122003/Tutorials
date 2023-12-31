# Tutorial 7 - Variables, Datatype & Typecasting
print ('\t Tutorial 7 :', 'https://youtu.be/z1-zfCvxybI', '\n')
var1='Kolkata'
var2=8
var3=9.8
print (type (var1), type (var2), type (var3))
var4=' rocks now'
print (var1 + var4)
x= '573'
y= '42'
print (int (x) + int (y))
print (5*str(int (x) + int (y)))
exit
print ('put value of x, the output will be 5x')
x= input ()
print (int(x)*5) #x is always taken as a str in input function. So in case of mathematical operation we need to convert str into int or float
exit
print ('\n')
print ('additive calculator, 2 numbers')
print ('enter 1st number')
x= input ()
print ('enter 2nd number')
y= input ()
print ('the addition is ', float(x)+float(y))
exit
