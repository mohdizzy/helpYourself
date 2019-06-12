import glob, os
import tinify

tinify.key = 'YOUR_APIKEY'
# Folder where your optimized images will be stored.
dirName = "tinifiedImages"
os.chdir("/PATH TO YOUR IMAGE DIRECTORY")

# Creates a separate folder with the name specified above. File names for all images is same as original.
# Folder containing optimized images will be created inside the source folder.
if not os.path.exists(dirName):
	os.mkdir(dirName)
	print("Directory " , dirName ,  " Created ")
else:
	print("Directory " , dirName ,  " already exists")

# tinify API is called to perform the optimization of all images present in the source folder.
# Ensure that source folder contains only JPEG or PNG formats otherwise an error will be thrown
for file in glob.glob("*.*"):
    source = tinify.from_file(file)
    source.to_file(os.getcwd()+"/tinifiedImages/"+file)

print("Tinify done")

