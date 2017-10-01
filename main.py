#!/usr/bin/env python
# coding=utf-8
from iolib import read_file, get_html


# common call back
def cb(err, data):
	if err:
		print err

	print data[0:5]

# async task one
get_html(
	'https://csrgxtu.github.com',
	cb
)
print 'after async get_html'

# async task two
read_file(
	'/etc/hosts',
	cb
)
print 'after async read_file'

# event_loop()
print 'end of the main script'
