###############################
# Filename: timelapse.py      #
# Author: Mitchel R Moon      #
###############################

import os
import time

FRAMES = 1000
FPS_IN = 10
FPS_OUT = 24
TIMEBETWEEN = 6
FILMLENGTH = float(FRAMES / FPS_IN)

frameCount = 0
while frameCount < FRAMES:
  imageNumber = str(frameCount).zfill(7)
  os.system("raspistill -o image%s.jpg"%(imageNumber))
  frameCount += 1
  # allow at least 6 s for a photo
  time.sleep(TIMEBETWEEN - 6)

os.system("avconv -r %s -i image%s.jpg -r %s -vcodec libx264 -crf 20 -g 15 -vf crop=2592:1458,scale=1280:720 timelapse.mp4"%(FPS_IN,'%7d',FPS_OUT)))
