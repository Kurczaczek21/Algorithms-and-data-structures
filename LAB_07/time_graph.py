import csv
import matplotlib.pyplot as plt

if __name__ == '__main__':
	INPUT_FILE = 'C:\\PY prog\\LAB_07\\times_data.csv'
	OUTPUT_FILE = 'graph.png'
	Ns, naive_times, rabin_karp_times = [], [], []

	# read from csv file
	with open(file=INPUT_FILE, newline='') as file:
		lines = csv.reader(file, delimiter=',', quotechar='|')
		next(lines)  # skip the header
		for row in lines:
			Ns.append(int(row[0]))
			naive_times.append(float(row[1]))
			rabin_karp_times.append(float(row[2]))

	# add plots
	plt.plot(Ns, naive_times, color='c', label='naive algorithm',  marker='o', markersize=6, linestyle='dotted')
	plt.plot(Ns, rabin_karp_times, color='r', label='Rabin - Karp algorithm', marker='o', markersize=6, linestyle='dotted')

	plt.title('times of algorithms depending on matrix size')
	plt.legend()
	plt.ylabel('time [s]')
	plt.xlabel('matrix size [N x N]')
	plt.savefig(OUTPUT_FILE, bbox_inches='tight')