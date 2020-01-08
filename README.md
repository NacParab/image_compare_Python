# image_compare_Python
This Repository contains a Python3 code for comparing two images of same size developed by Nachiket Parab. 

Special thanks to Olli-Pekks Heinisuo , the creator of [opencv-python](https://github.com/skvark/opencv-python).
Thanks to the  creators of [argparse](https://github.com/python/cpython/blob/master/Lib/argparse.py) and [numpy](https://github.com/numpy/numpy) as well.

## How to use image_compare_Python

Test case:
```python
python image_compare.py -n new_image.jpg -o old_image.jpg -t 10 -s 3
```

### The supported formats for the input image are those supported by OpenCV which are as follows:
* Windows bitmaps - *.bmp, *.dib (always supported)
* JPEG files - *.jpeg, *.jpg, *.jpe (see the Notes section)
* JPEG 2000 files - *.jp2 (see the Notes section)
* Portable Network Graphics - *.png (see the Notes section)
* Portable image format - *.pbm, *.pgm, *.ppm (always supported)
* Sun rasters - *.sr, *.ras (always supported)
* TIFF files - *.tiff, *.tif (see the Notes section)

### Note
* The function determines the type of an image by the content, not by the file extension.
* On Microsoft Windows OS and MacOSX, the codecs shipped with an OpenCV image (libjpeg, libpng, libtiff, and libjasper) are used by default. So, OpenCV can always read JPEGs, PNGs, and TIFFs. On MacOSX, there is also an option to use native MacOSX image readers. But beware that currently these native image loaders give images with different pixel values because of the color management embedded into MacOSX.
* On Linux, BSD flavors and other Unix-like open-source operating systems, OpenCV looks for codecs supplied with an OS image. Install the relevant packages (do not forget the development files, for example, “libjpeg-dev”, in Debian and Ubuntu) to get the codec support or turn on the OPENCV_BUILD_3RDPARTY_LIBS flag in CMake.
