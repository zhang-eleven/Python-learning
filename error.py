try:
	print('try...')
	r = 10 / int('a')
	print ('result:',r)
except ZeroDivisionError as e:
	print ('ZeroDivisionError:',e)
except ValueError as e:
	print ('ValueError',e)
finally:
	print ('finally...')
print ('END')

##### division line #####

def foo(s):
	return 10/int(s)
	
def bar(s):
	return foo(s)*2
	
def main():
	try:
		bar('0')
	except Exception as e:
		print ('Error:',e)
	finally:
		print ('finally..')

##### division line #####


import logging

def foo(s):
	return 10 / int(s)
	
def bar(s):
	return foo(s)*2
	
def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
main()

print ('END')

##### division line #####

class FooError(ValueError):
	pass
	
def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid values:%s'%s)
		logging.exception(FooError)
	return 10 / n
	
foo('0')

##### division line #####

def foo(s):
	n = int(s)
	if n == 0:
		raise ValueError('invlid value:%s'%s)
	return 10 / n

def bar():
	try:
		foo('0')
	except ValueError as e:
		print ('ValueError!')
		raise

bar()
