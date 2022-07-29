key_guess = []
numtraces = trace_array.shape[0]

numpoints = trace_array.shape[1]
start_point = 450
end_point = 700

crys = np.zeros((16, 256, numpoints))
HW_matrix = np.zeros((numtraces, 256), dtype=np.uint8)

printable =[]

for subkey in tnrange(0, 16, desc="Attacking Subkey"):
	temp = []
	for kguess in tnrange(0, 256, desc="Generating Hamming Weights"):
		for trace_no in range(numtraces):
			iv = intermediate(textin_array[trace_no][subkey], kguess)
			HW_matrix[trace_no, kguess] = HW[iv]

		for point in range(start_point, end_point):
			hw = HW_matrix[:, kguess]
			trc = trace_array[:, point]
			crvs[subkey, kguess, point] = np.abs(linregress(hw, trc).slope)

		temp.append((kguess, np.max(crvs[subkey, kguess])))

	temp.sort(key = lambda x: -x[1])
	printable.append(temp)
	df = pd.DataFrame(printable).transpose()

	key_guess.append(crvs[subkey].max(axis=1).argmax())

	clear_output(wait=True)
	display(df.head().style.format(format_stat).apply(color_corr_key, axis=0))

	print(key_guess, known_keys[0], sep='\n')