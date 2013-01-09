import urllib
proto,rest=urllib.splittype("http://www.baidu.com/11/12.htm")
proto,rest=urllib.splittype("ftp://www.baidu.com:9090/11/12.htm")
host,rest=urllib.splithost(rest)
print host
host,port=urllib.splitport(host)
if port is None:
	port=80
print port
