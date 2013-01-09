import re
import optparse
def get_filename():
	p=optparse.OptionParse()
	p.add_option('-f',action='store',dest='filename',help='the directory u want monitoring')
	opt,args=p.parse_args()
	if None==opt.filename:
		p.error('Need a file!')
	else:
		filename=opt.filename
	return filename

filename=get_filename()

rc=re.compile(r'\w+\.(?:com\.cn|net\.cn|gov\.cn|org\.cn|com|cn|edu|gov|org|cc|net|tk|biz|info|me)$',re.I)
line_num=1

try:
	for line in open(filename):
		print rc.search(line).group()
		line_num +=1
except AttributeError:
	print "\n Error:\n line_num :%\n domain_name:%s" %(str(line_num),line)
	raise SystemExit
