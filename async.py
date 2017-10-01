import threading


TASK_QUEUE = []
THREAD_START = False


def async_decorator(func):
	""" async decorator """
	def func_wrapper(target, call_back):
		thread = threading.Thread(target=func, args=(target, call_back,))
		TASK_QUEUE.append(thread)
		import atexit
		atexit.register(event_loop)

	return func_wrapper


def event_loop():
	if not TASK_QUEUE:
		return

	if THREAD_START:
		return
	else:
		global THREAD_START
		THREAD_START = True

	# start the async task
	for task in TASK_QUEUE:
		task.start()

	# wait until finished
	for task in TASK_QUEUE:
		task.join()
