import sys
if sys.version_info >= (3, 0):
	import imp
	imp.reload(sys)
else:
	reload(sys)
	sys.setdefaultencoding('utf8')
sys.dont_write_bytecode = True

from pixivpy3 import *

### change _USERNAME,_PASSWORD first!
_USERNAME = "globaluser"
_PASSWORD = "password"

def search_works(api):
	# PAPI.works
	#json_result = api.works(46363414)
	#print(json_result)
	#illust = json_result.response[0]
	#print(">>> %s, origin url: %s" % (illust.caption, illust.image_urls['large']))

	# PAPI.search_works
	json_result = api.search_works("五航戦 姉妹", page=1, per_page=1, mode='text')
	total = json_result.pagination.total

	print(json_result)
	#illust = json_result.response[0]
	#print(">>> %s origin url: %s" % (illust.title, illust.image_urls['large']))


def main():
	api = PixivAPI()
	api.login(_USERNAME, _PASSWORD)
	search_works(api)

if __name__ == '__main__':
	main()
