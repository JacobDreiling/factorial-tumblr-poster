import sys
from tumblpy import Tumblpy
import FactorialScript

info= []#redacted

t= Tumblpy(info[0],info[1],info[2],info[3])

#temporary last range should be 8574 (inclusive)

for i in range(6101,6301):
	extras= ''
	if FactorialScript.interestings.count(i)==1:
		extras= input('{}\n\nenter extra tags for {}. (include a comma at the beginning)'.format(FactorialScript.coolFax[FactorialScript.interestings.index(i)],i))
	t.post('post', blog_url='allthefactorials.tumblr.com', params={'type':'text', 'state':'queue', 'title':str(i), 'body':FactorialScript.facScript(i), 'tags':'math,mathematics,big numbers,factorial'+extras})
