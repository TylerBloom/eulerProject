#! /usr/bin/python

import fileinput
import math

sum = 0
total = 0

for one in range(201):
	total += one*1
	for two in range(101):
		total += two*2
		if total > 200:
			total -= two*2
			break
		for five in range(41):
			total += five*5
			if total > 200:
				total -= five*5
				break
			for ten in range(21):
				total += ten*10
				if total > 200:
					total -= ten*10
					break
				for twenty in range(11):
					total += twenty*20
					if total > 200:
						total -= twenty*20
						break
					for fifty in range(5):
						total += fifty*50
						if total > 200:
							total -= fifty*50
							break
						for oneHund in range(3):
							total += oneHund*100
							if total > 200:
								total -= oneHund*100
								break
							for twoHund in range(2):
								total += twoHund*200
								if total == 200:
									sum += 1
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
