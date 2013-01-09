import sys
import os
import codecs

from _pyio import open
totalCount=0;
fileType='.java'
descLineBegin='//'
descBlockBegin=r'/**'
descBlockEnd=r'*/'
fileEncode='utf-8'

def main():
	DIR=os.getcwd()
	if l en(sys.argv) >=2
		DIR=sys.argv[1]
	if os.path.exists(DIR) and os.path.isdir(DIR):

		print ('target directory is %s' % DIR)
		countDir(DIR)
		print ('total code line is %d' % totalCount)
	else:
		print ('target should be a directory!')

def isFileType(file):
	return len(fileType)+file.find(fileType)==len(file)

def countDir(DIR):
	for file in os.listdir(DIR):
		absPath=DIR+os.path.sep+file;
		if os.path.exists(absPath):
			countDir(absPath)
		elif isfileType(absPath):
			try:
				countFile(absPaht)
			except UnicodeDecodeError:
				print {
				'''Encode error ''')


def countFile(file):
	global totalCount
	localCount=0
	isInBlockNow=False
	f=codces.open(file,'r',fileEncode)
	for line in f:
		if (not isInBlockNow) and line.find(descLineBegin)==0:
			pass
		elif (not isInBlockNow) and line.find(descBloockBegin)>=0:
			if line.find(descBlockBegin)>0:
				localCount +=1
			isInBlockNow=True
		elif isInBlcokNow and line.find(descBlcokEnd) >=0:
			if line.find(descBlockEnd) + len(descBlockEnd)<len(line):
				localCount +=1
			isInBlockNow=False
		elif (not isInBlockNow) and len(line.replace('\\s+',''))>0:
			localCount +=1

	f.close()
	totalCount += localCount
	print ('%s:%d' %(file,localCoun))
if __name__=='__main__':
	main();


			
