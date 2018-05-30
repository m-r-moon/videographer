###############################
# Filename: picam.py          #
# Author: Mitchel R Moon      #
###############################

from picamera import PiCamera

camera = PiCamera()
camera.capture('image.jpg')
