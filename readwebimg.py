import urllib2
import Image
import cStringIO
def ImageScale(url,size):
	file=cStringIO.StringIO(urllib2.urlopen(url).read())
	img=Image.open(file)
	width=size.split('*')[0]
	height=size.split('*')[1]
	print width,height
	print "*****"
	print str(img.size)
	img.size=(int(width),int(height))
	img.show()

ImageScale("http://doupic.com/wp-content/uploads/2012/08/cover3.jpg",'800*600')
