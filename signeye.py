from handtracking import detect_single_threaded
import threading 
from multiprocessing.pool import ThreadPool
pool = ThreadPool(processes=1)

def asa():
	g = detect_single_threaded.detectNcrop()
	return g

async_result = pool.apply_async(asa) # tuple of args for foo

# do some other stuff in the main process

return_val = async_result.get()
print(return_val)