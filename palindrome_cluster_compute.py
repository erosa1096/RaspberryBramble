# executed on each node before any jobs are scheduled
def setup(data_file):
    # read data in file to global variable
    global words, bounds
	words = []
	bounds = []

    f = open(data_file, 'r').read()  # read file in to memory; data_file can now be deleted
    i = 0
	nextUpper = 'A'
	nextLower = 'a'
	for line in f:
		
		#ord()#turns char to ascii value
		#chr()#turns number to ascii character
		words.append(line.split('\n'))
		if(words[i][0] == nextUpper || words[i][0] == nextLower)
		{
			nextUpper++
			nextLower++
			bounds.append(i)
		}
		i += 1
		
	
    return 0
	
def cleanup():
    global words, bounds
    del words, bounds

	
# function 'compute' is distributed and executed with arguments
# supplied with 'cluster.submit' below
def compute(bIndex):
    import time, socket
	global words,bounds
	pals = 0
	for(x = bounds[bIndex];)
	
		
    host = socket.gethostname()
    return (host, numPals)

if __name__ == '__main__':
    # executed on client only; variables created below, including modules imported,
    # are not available in job computations
    import dispy, sys, functools, random
    # if no data file name is given, use this file as data file
    data_file = sys.argv[1] if len(sys.argv) > 1 else sys.argv[0]
    cluster = dispy.JobCluster(compute, depends=[data_file],
                               setup=functools.partial(setup, data_file), cleanup=cleanup)
    # run 'compute' with 20 random numbers on available CPUs
    jobs = []
    for i in range(20):
        job = cluster.submit(random.randint(5,20))
        job.id = i # associate an ID to identify jobs (if needed later)
        jobs.append(job)
    # cluster.wait() # waits until all jobs finish
    for job in jobs:
        host, n = job() # waits for job to finish and returns results
        print('%s executed job %s at %s with %s' % (host, job.id, job.start_time, n))
        # other fields of 'job' that may be useful:
        # job.stdout, job.stderr, job.exception, job.ip_addr, job.end_time
    cluster.print_status()  # shows which nodes executed how many jobs etc.
