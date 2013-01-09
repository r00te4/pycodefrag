import sys,getopt
opts,args=getopt.getopt(sys.argv[1:],"hi:o:")
opts,args=getopt.getopt(sys.argv[1:],"hi:o:",["version","file="])
input_file=""
output_file=""
for op,value in opts:
	if op=="-i":
		input_file=value
	elif op=="-o":
		output_file=value
	elif op=="-h":
		useage()
		sys.exit()

