import re


def main():
	email = input("请输入一个邮箱地址:")
	# 如果在正则表达式中需要用到某些普通字符，如 . ？等，需要转义
	ret = re.match(r"[a-zA-Z_0-9]{4,20}@(163|126)\.com$", email)
	if ret:
		print("%s符合要求..." % email)
	else:
		print("%s不符合要求..." % email)


if __name__ == '__main__':
	main()
