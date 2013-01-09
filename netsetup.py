import os
import random,re
g='gateway 192.168.1.'
rand=random.randint(1,3)
test='wwww.baidu.com'
commaind='/etc/init.d/networking restart'
GW="%s%d" %(g,rand)
PingTest='ping -c 3' + tset
try:
	result=os.system(PingTest)
	print result
	if reslut!=0:
		data=open('/etc/network/interfaces').read()
		data=re.sub('gateway 192.168.1.*',GW,data)
		open('/etc/network/interfaces','wb').write(data)
		os.system(command)
		os.system(command)
except:
	pass
