import sys

class progressBar:

	def __init__ (self):
		return

	def printProgressBar(self, iteration, total, label = '', end_label = '', fill = '█'):
		percent = ("{0:." + str(1) + "f}").format(100 * (iteration / float(total)))
		filledLength = int(50 * iteration // total)
		bar = fill * filledLength + '-' * (50 - filledLength)

		print('\r%s |%s| %s%% %s' % (label, bar, percent, end_label), end = '\r')
		if iteration == total:
			print()
		#print("\r %s %s ... %d %%" % (label, 'Progress', iteration), end = '\r')
		#sys.stdout.write("\r %s %s ... %d %%" % (label, 'Progress', iteration, prefix))
