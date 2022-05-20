import logging

python30 =  [
	['lj','klla','k'],
	['ks','aii','qoo'],
	['ol',',,o']
]

for group in python30:
	#debug与info级别 默认是不被记录 所以没有打印出来，默认是打印warning error critical
	logging.debug('group={}'.format(group))
	for name in group:
		logging.debug(('name=:{}'.format(name)))

# logging.info(python30)

if type(python30) == dict:
	logging.warning('warning')

if type(python30) == list:
	logging.error('error')
	raise ValueError