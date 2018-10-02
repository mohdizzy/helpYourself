import os
import sys
from PIL import Image

def compressMeReturn(file, maxDim, verbose=False):
	filepath = os.path.join(os.getcwd(), file)
	oldsize = os.stat(filepath).st_size
	picture = Image.open(filepath)
	dim = picture.size
	dirName = "compressedImages"

	ratio = (maxDim/dim[0],maxDim/dim[1])

	if not os.path.exists(dirName):
		os.mkdir(dirName)
		print("Directory " , dirName ,  " Created ")
	else:
		print("Directory " , dirName ,  " already exists")
	
	picture.thumbnail((dim[0]*ratio,dim[1]*ratio), Image.ANTIALIAS)
	if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg','.png'):
		picture.save(os.getcwd()+"/compressedImages/"+file,"JPEG",optimize=True,quality=75)
	else:
		picture.save(os.getcwd()+"/compressedImages/"+file,"PNG",optimize=True,quality=75)  
	
	newsize = os.stat(os.path.join(os.getcwd(),os.getcwd()+"/compressedImages")).st_size
	percent = (oldsize-newsize)/float(oldsize)*100
	if (verbose):
		print "File compressed from {0} to {1} or {2}%".format(oldsize,newsize,percent)
	return percent

def main():
	maxDimension = 260
	verbose = False
	if (len(sys.argv)>2):
		if (sys.argv[2].lower()=="-v"):
			verbose = True

	pwd = os.getcwd()
	tot = 0
	num = 0
	for file in os.listdir(pwd):
		if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg','.png'):
			num+=1
			tot += compressMeReturn(file, int(maxDimension),verbose)
	print "Average Compression: %d" % (float(tot)/num)
	print "Done"

if __name__ == "__main__":
	main()
