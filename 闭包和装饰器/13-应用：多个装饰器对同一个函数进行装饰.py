def set_func_1(func):
	def call_func():
		return "<h1>" + func() + "</h1>"
	return call_func


def set_func_2(func):
	def call_func():
		return "<td>" + func() + "</td>"
	return call_func


@set_func_1
@set_func_2
def get_str():
	return "win"


print(get_str())
