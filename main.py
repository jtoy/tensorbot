from drive_safe2 import *
from image import *


stopped = True;
turning = False;
THRESH = 25;
turnCount = 0;
maxTurnCount = 3;

while(1==1):
	print("driving!")

#	while True:
#		s = getAttention();
#        print "Speed "+str(s)
#        if s > 0:
#            break
#        setSpeed(0)
#        time.sleep(0.2)

	mind = 1000
	d=[]

	for i in range(len(TRIG)):
		d.append( distance(i));
		if d[i] < mind:
			mind = d[i]
		print(d[i]);

	print(d)
	print("Min d " + str(mind))

	if (mind<6 and stopped==True and turning==True):
		do('echo "backing up." | flite ')
		backward(255, 1)
	elif (turnCount > maxTurnCount):
		do('echo "backing up." | flite ')
		backward(255, 1);
		turnCount = 0;
	elif (mind>=THRESH and stopped==True):
		stopped=False;
		turning = False;
		gof();
		turnCount = 0
	elif (mind<THRESH and stopped==False):
		stopped=True;

	elif (mind<THRESH and stopped==True):
		if (turning==False):
			stop();
			turning=True
		else:
			turnCount+=1

		if random.randrange(0,2) == 1:
		#if d[2] > d[0]:
			do('echo "turning left." | flite ')
			left(255, 0.5);
		else:
			do('echo "turning right." | flite ')
			right(255, 0.5);

		time.sleep(0.3);
		stopped=True

        i=0
        read_data = 0
        with open('images/INDEX', 'r') as f:
        	read_data = int(f.read())

        i += read_data + 1;

        our_classify(i)
