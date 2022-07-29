mean_diffs = np.zeros(256)
key_guess = []
numtraces = 500

for subkey in tnrange(0,16, desc="Total Progress"):
	for kguess in tnrange(256, desc= "Attacking Subkey {subkey}", leave =False):
		one_list = []
		zero_list = []

		for trace_no in range(numtraces):
			if(intermediate(textin_array[trace_no][subkey], kguess) & 1):
				one_list.append(trace_array[trace_no])
			else:
				zero_list.append(trace_array[trace_no])

		one_avg = np.asarray(one_list).mean(axis=0)
		zero_avg = np.asarray(zero_list).mean(axis=0)
		mean_diffs[kguess] = np.max(abs(one_avg - zero_avg))

	guess = np.argsort(mean_diffs)[-1]
	key_guess.append(guess)
	clear_output(wait=True)
	display(key_guess)

	