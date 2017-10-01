from async import async_decorator


@async_decorator
def read_file(filename, call_back):
	with open(filename, 'r') as file_handler:
		res = file_handler.read()
		if res:
			return call_back(False, res)
		else:
			return call_back('Error', None)


@async_decorator
def get_html(url, call_back):
	import requests
	r = requests.get(url)
	if r.status_code == 200:
		return call_back(False, r.text)
	else:
		return call_back('Error', None)
