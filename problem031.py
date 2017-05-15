#! /usr/bin/python

import fileinput
import math

sum = 0
total = 0

for one in range(201):
	total += one*1
	for two in range(101):
		total += two*2
		for five in range(41):
			total += five*5
			for ten in range(21):
				total += ten*10
				for twenty in range(11):
					total += twenty*20
					for fifty in range(5):
						total += fifty*50
						for oneHund in range(3):
							total += oneHund*100
							for twoHund in range(2):
								total += twoHund*200
								if total == 200:
									sum += 1
									print sum
								total -= twoHund*200
							total -= oneHund*100
						total -= fifty*50
					total -= twenty*20
				total -= ten*10
			total -= five*5
		total -= two*2
	total -= one*1
	print one

print sum
