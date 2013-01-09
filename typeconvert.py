dic1={"name":"mcl","age":25,"sex":"male"}
for k,v in dic1.items():
	print " \" %s \" : %s \" " %(k,v)

str1="{'year':2011,'month':'Dec','date':'0913'}"
dic2=eval(str1)

print dic2

print 
"""
int(x[,base])
long(x[,base])
float(x)
complex(real[,image])
str(x)
repr(x)
eval(str)
tuple(s)
list(s)
chr(x)
unichr(x)
ord(x)
hex(x)
oct(x)
