# Usage #
 ---

- This script is for watermarking an entire directory of images ( .jpgs | .pngs )
- Run the script in the directory that you want to watermark like this:
    ``python main.py -w [watermark] -p [position] [-NTSC] [-EQG] [-EQC] [-MF]``    

- watermark - The text you want to watermark on the images
- position - ul : upper left , ur - upper right , ll - lower left , lr - lower right
- NTSC - Converts color image(s) to the National Television System Committee's standard for color to grayscale images
- EQG - Converts color image(s) to NTSC grayscale then equalizes the images intensities using histograms
- EQC - Converts color image(s) to YCRCB and equalizes the images intensities using historgrams (converts it back to RGB afterwards)
- MF - Converts color image(s) to NTSC grayscale then applies a median filter to smooth the image.

- This will make a folder called 'Watermarked' and copy the new watermarked images into it, preserving original images
