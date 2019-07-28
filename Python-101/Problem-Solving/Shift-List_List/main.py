def shift_left(num_list, shift):
	# a = shift % len(num_list)
	# return seq[a:] + seq[:a]
	
    return(num_list[shift:]+num_list[:shift])
	

def shift_right(num_list, shift):
	# a = shift % len(num_list)
	# return seq[-a:] + seq[:-a]

	return(num_list[-shift:]+num_list[:-shift])
