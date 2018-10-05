# HelpYourself
**Mixed set of things that can help accomplish certain specific tasks.**

## Contents

* Image compression


## Image compression
1. **'imgCompression.py'** -- *Compress JPEG files by utilizing python's Pillow library.*
- Assuming python3 and Pillow is already installed, copy file to folder containing images.
- Edit 'quality' parameter to the level of compression needed. Ideal value between 65 to 80 is fine.
- Run the script.
- Compressed images are stored in a folder called 'compressedImages' in the same folder where the script is present.
NOTE: A line with reference to PNG is present. It's only to handle incase files with PNG format are encountered in the folder while running the script.

2. **'tinify.py'** -- *Compress PNG/JPEG files using tinify API. The optimization is done automatically by the API.*
- With python3 installed, run `pip install tinify`
- Place your API key inside the file. (Go to https://tinypng.com/developers. Key will be sent to your email.)
- Make sure the path your image folder is provided correctly. Also the folder should contain only JPEG/PNG as any other format would result in an error.
- Run the script.
NOTE: For free users, the number of images you can upload for compression is limited(500/month at the time of writing this.)

