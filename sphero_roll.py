#sudo pip install kulka

import time
from kulka import Kulka
from random import randint

with Kulka('00:06:66:47:37:C7') as kulka:
	while True:
		kulka.roll(60 , randint(0, 359))
		time.sleep(.5)		

