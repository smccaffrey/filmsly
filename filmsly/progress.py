import sys

class progressBar():

	def __init__ (self):
		return

	def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
		"""
		Call in a loop to create terminal progress bar
		params:
			iteration   - Required  : current iteration (Int)
			total       - Required  : total iterations (Int)
			prefix      - Optional  : prefix string (Str)
			suffix      - Optional  : suffix string (Str)
			decimals    - Optional  : positive number of decimals in percent complete (Int)
			length      - Optional  : character length of bar (Int)
			fill        - Optional  : bar fill character (Str)
		"""
		percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
		filledLength = int(length * iteration // total)
		bar = fill * filledLength + '-' * (length - filledLength)
		print('\r%s |%s| %s%% %s' % ('Test:', bar, percent, suffix), end = '\r')
		# Print New Line on Complete
		if iteration == total: 
			print()

	def otherProgressBar(self, iteration, total, label = '', end_label = '', fill = '█'):
		percent = ("{0:." + str(1) + "f}").format(100 * (iteration / float(total)))
		filledLength = int(50 * iteration // total)
		bar = fill * filledLength + '-' * (50 - filledLength)

		print('\r%s |%s| %s%% %s' % (label, bar, percent, end_label), end = '\r')
		if iteration == total:
			print()
		#print("\r %s %s ... %d %%" % (label, 'Progress', iteration), end = '\r')
		#sys.stdout.write("\r %s %s ... %d %%" % (label, 'Progress', iteration, prefix))
