#! /bin/bash

( cd /home/pi/rubyrobot && ./classify_image.py --image_file $1) &> raw.output  
tail -5 raw.output | cut -d"]" -f2 | cut -d"(" -f1 > $2


#bash run_and_parse_inception.sh images/img16.jpg images/data16
