import shutil
import os
import os.path
src="d:\\tmp\\pytest\\myfile1.txt"
dst="d:\\tmp\\pytest\myfile2.txt"
dst2="d:\\tmp\\pytest2"

dir1=os.path.dirname(src)
print ("dir1 %s " % dir1)
if (os.path.exists(src)==False):
	#os.makedirs(dir1)
	print "making dir"
f1=open(src,"w")
f1.write("line a \n")
f1.write("line b \n")
f1.close()

shutil.copyfile(src,dst)
#shutil.copyfile(src,dst2)
f2=open(dst,"r")
for line in f2:
	print (line)
f2.close()


try:
	srcDir="d:\\tmp\\pytest"
	dstDir="d:\\tmp\\pytest2"
	shutil.copytree(srcDir,dstDir)

#except (Exception as err):
#	print (err)
except Exception as err:
	print "nothing"
	print (err)


"""
shuttil.copyfile()
os.path.exists()
shutil.copytree()
"""
