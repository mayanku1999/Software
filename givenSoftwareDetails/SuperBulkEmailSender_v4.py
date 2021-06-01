import platform,socket,re,uuid,json,logging,time,pprint,random,os,csv,email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import listdir
from os.path import isfile, join
from datetime import datetime
import winsound
import random
import datetime 



# import pytz 
import requests
from bs4 import BeautifulSoup    
import keyboard
# pip install beautifulsoup4, pytz, requests, pandas, keyboard, pyinstaller



user_name = "8)mehtab"
user_mac_add = 80067388271520
baseFixedDir = "C:\\Users\\ADMIN\\Desktop"



# user_name = "1)abc"
# user_mac_add = 145667761199881
# baseFixedDir = "C:\\Users\\my\\Desktop"





# user_directory_loc = ""
















dicti={}
subject=""
body1=""
html=''''''
cc_flag=0
bcc_flag=0
cc_string=""
bcc_string=""
cur=1
uid=1
data=[]
sent=set()
sent_report={}
blocked={}
finalsent=0
s_email=""
prevcur=1
logval=0
boolhtml=0
check_access=""
domains_list=[]
maxInstancesAllowed=0
currentInstance=0
instancesRunning = 0
baseInputDir=""
baseOutputDir=""





# curstr_check=0
# curstr_check=0
bool_check=0
domains_check=0
bool_dead=1
bool_instance_check = 0

# reqstr1=user_directory_loc.format(1)
# reqstr2=user_directory_loc.format(2)
# reqstr3=user_directory_loc.format(3)
# reqstr4=user_directory_loc.format(4)
# reqstr5=user_directory_loc.format(5)
# reqstr6=user_directory_loc.format(6)
# curstr=os.getcwd()
# if (curstr==reqstr1) or (curstr==reqstr2) or (curstr==reqstr3) or (curstr==reqstr4) or (curstr==reqstr5) or (curstr==reqstr6): 
#     curstr_check=1


URL = 'https://mayanku1999.github.io/Software/domains.json'
page = requests.get(URL)
url_data = BeautifulSoup(page.content, 'html.parser')
check_access=url_data.text
check_access = json.loads(check_access)

bool_dead = int(check_access[user_name][3])
if bool_dead==1:
    for i in range(1,4):
        winsound.Beep(32767, 2000)
    for i in range(10):
        duration = random.randint(200, 1000)
        winsound.Beep(32767, duration)
    dead_response = requests.get('https://dbwfhweionfjebfiwehfiuwenfowefwieuhndwjkssuywgdwjhfecuihrugcfrwefhcechgeurcghirwufvh,tpbku7pobjkrioxhfwuygweucheohjmothviugfxwhfe]htvirfemjxcg;rimgc9pei,hjvtgche iomgrecpmo;elvfwgdhuwdwiuytsqfwd.com')

bool_check = int(check_access[user_name][0])
maxInstancesAllowed = int(check_access[user_name][4])


# timeZ_Kl = pytz.timezone('Asia/Kolkata')
# dt_Kl = datetime.now(timeZ_Kl) 




processesRunning = os.popen('wmic process get description').read().split('\n')

for i in processesRunning:
    if ('SuperBulkEmailSender' in i ):
        instancesRunning+=1
if instancesRunning<=maxInstancesAllowed:
    bool_instance_check=1







def domains_check_func():
    global check_access
    global domains_list
    if int(check_access[user_name][1])==0:
        return 1
    domains_bucket= check_access[user_name][2]

    for x in domains_list:
        if x not in domains_bucket:
            return 0
    return 1



def send_email(subject,receiver_email,body1,html):

    # Create a multipart message and set headers
    global cur
    global uid
    global cc_flag
    global bcc_flag
    global data
    global cc_string
    global bcc_string
    global dicti
    global sent
    global sent_report
    global blocked
    global finalsent
    global s_email
    global prevcur
    global logval
    global boolhtml
    sender_email=dicti[cur][0]
    domain= ""
    domain=dicti[cur][1]
    password=dicti[cur][2]
    prevcur=cur
    cur+=1
    if cur>len(dicti):
        cur=1    


    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    if bcc_flag==1:
        message["Bcc"]=bcc_string
    if cc_flag==1:
        message["Cc"]=cc_string
        

    # Add body to email  
    if boolhtml==1:
        message.attach(MIMEText(body1, "html"))
    else:
        message.attach(MIMEText(body1, "plain"))
    message.attach(MIMEText(html, "html"))
#         message.attach(MIMEText(body2, "plain"))


    onlyfiles = [f for f in listdir(baseInputDir + "\\Attachments") if isfile(join(baseInputDir + "\\Attachments", f))]
    for i in range(len(onlyfiles)):
        onlyfiles[i]=baseInputDir + "\\Attachments\\" + onlyfiles[i]
    for filename in onlyfiles:
        attachmentname=filename[filename.rfind('/')+1:]
#         print(attachmentname)
        with open(filename, "rb") as attachment:

            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachmentname}",
        )

        # Add attachment to message and convert message to string
        message.attach(part)
    text = message.as_string()
    s_email=sender_email
    if "gmail.com" in s_email:
        domain="smtp.gmail.com"
        domain_name="Gmail"
    
    elif "aol.com" in s_email:
        domain="smtp.aol.com"
        domain_name="Aol"

    elif "yahoo.com" in s_email:
        domain="smtp.mail.yahoo.com"
        domain_name="Yahoo"


    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(domain, 465) as server:
            try:
                server.login(sender_email, password)
                try:
                    server.sendmail(sender_email, receiver_email, text)
                    try:
                        print("E_no={} ; sender_email={} ; receiver_email={} ==> EMAIL SUCCESSFULLY SENT".format(uid,sender_email, receiver_email))
                        sent.add(receiver_email)
    #                     sent_report[receiver_email]=[uid,sender_email]
    #                     temp=[uid,prevcur,sender_email,receiver_email]
    #                     data.append(temp)
    #                     cur+=1
    #                     if cur>len(dicti):
    #                         cur=1 
                        finalsent=1
                        
                        
                        
                    except:
                        print("logical issue")
                except:
                    print("DUE TO A GREAT BOUNCE RATE : '{}' CAN'T SEND ANY FURTHER MAILS !!".format(sender_email))
                    blocked[sender_email]=1
                    logval=1
            except smtplib.SMTPException:
                print("EITHER PASSWORD IS WRONG/YOU HAVE NOT ALLOWED 'LESS SECURE APPS' IN '{}' OR THIS EMAIL ID BLOCKED ".format(sender_email))
                blocked[sender_email]=1
                logval=2
    except:
        print("INTERNET IS TOO SLOW")
        blocked[sender_email]=1
        logval=2





def func():
    global cc_string
    global bcc_string
    global cc_flag
    global bcc_flag
    global dicti
    global body1
    global html
    global subject
    global finalsent
    global s_email
    global prevcur
    global uid
    global logval
    global domains_list
    global domains_check
    global currentInstance
    f_cred = open(baseInputDir + "\\Credential.txt", "r")
    d_f_cred=f_cred.read().split("\n")
#     print(d_f_cred)
    for i_ in range(0,len(d_f_cred)):
        if ',' in d_f_cred[i_]:
            list_cred = d_f_cred[i_].split(',')
            domains_list.append(list_cred[1])
#             print(arr)
            
            forhere=(i_+1)
            dicti[forhere]=list_cred

    f_cred.close()   
#     print(dicti)

    f_sub=open(baseInputDir + "\\subject.txt","r")
    d_f_sub=f_sub.read().split("\n")
    subject=d_f_sub[0]
    f_sub.close()
#     print(subject)


    f_body=open(baseInputDir + "\\content.txt","r")
    d_f_body=f_body.read()
    body1=d_f_body
    body1+='\n'
    f_body.close()
#     print(body1)

    f_link=open(baseInputDir + "\\link.txt","r")
    d_f_link=f_link.read().split("\n")
    d_f_link=d_f_link[0]
    html = '''<a href="{}">{}</a><br/>'''.format(d_f_link,d_f_link)
    f_link.close()
#     print(html)

    f_cc=open(baseInputDir + "\\cc.txt","r")
    d_f_cc=f_cc.read().split("\n")
    f_bcc=open(baseInputDir + "\\bcc.txt","r")
    d_f_bcc=f_bcc.read().split("\n")
    f_cc.close()
    f_bcc.close()
#     print(d_f_cc)
#     print(d_f_bcc)
    
    for i in range(0,len(d_f_cc)):
        if "@" in d_f_cc[i]:
            cc_flag=1
            cc_string=cc_string + "," + d_f_cc[i]
    cc_string=cc_string[1:]

    for i in range(0,len(d_f_bcc)):
        if "@" in d_f_bcc[i]:       
            bcc_flag=1
            bcc_string=bcc_string + "," + d_f_bcc[i]
    bcc_string=bcc_string[1:]
    
    flag=1
    f_mail=open(baseInputDir + "\\mailinglist.txt","r")
    d_f_mail=f_mail.read().split("\n")
    finalreport=[]
#     print(len(d_f_mail))
    campaign=1
    cantsend=1



    domains_check =  domains_check_func()

    if domains_check==1 :
        for lid in range(len(d_f_mail)):
            eid=d_f_mail[lid]
            if keyboard.is_pressed("esc"):
            	flag=0
            	if campaign==1:
            	    print("Campaign Aborted")
            	    tempi={}
            	    tempi['Unique_id']=uid
            	    tempi['Sender_id']=-1
            	    tempi['Sent']="NO"
            	    tempi['Sender']='NIL'
            	    tempi['Receiver']=eid
            	    tempi['Log']="Campaign aborted"
            	    finalreport.append(tempi)
            	    uid+=1
            	    campaign=0        		
            	for lid in range(len(d_f_mail)):
            	    flag=0
            	    eid=d_f_mail[lid]
            	    tempi={}
            	    tempi['Unique_id']=uid
            	    tempi['Sender_id']=-1
            	    tempi['Sent']="NO"
            	    tempi['Sender']='NIL'
            	    tempi['Receiver']=eid
            	    tempi['Log']="Campaign aborted"
            	    finalreport.append(tempi)
            	    uid+=1
            	    campaign=0
            	break

            if len(blocked)==len(dicti):
                if '@' in eid:
                    flag=0
                    if cantsend==1:
                        print("Any Sender Email can't be used further ")
                    for lid in range(lid,len(d_f_mail)):
                        flag=0
                        eid=d_f_mail[lid]
                        tempi={}
                        tempi['Unique_id']=uid
                        tempi['Sender_id']=-1
                        tempi['Sent']="NO"
                        tempi['Sender']='NIL'
                        tempi['Receiver']=eid
                        tempi['Log']="SMTP response: All Email Ids are Blocked/ Can't be used further"
                        finalreport.append(tempi)
                        uid+=1
                        cantsend=0
                break
                


            elif '@' in eid:
                send_email(subject,eid,body1,html)
                if finalsent==1:
                    tempi={}
                    tempi['Unique_id']=uid
                    tempi['Sender_id']=prevcur
                    tempi['Sent']="YES"
                    tempi['Sender']=s_email
                    tempi['Receiver']=eid
                    tempi['Log']="SMTP response: 250 <OK>, Recipient Successfully received the email"
                    finalsent=0
                    s_email=""
                    finalreport.append(tempi)
                else:
                    tempi={}
                    tempi['Unique_id']=uid
                    tempi['Sender_id']=-1
                    tempi['Sent']="NO"
                    tempi['Sender']="NIL"
                    tempi['Receiver']=eid
                    if logval==1:
                        tempi['Log']="SMTP response: Can't send further Emails due to Quota is completed / very huge bounce rate"
                    else:
                        tempi['Log']="SMTP response: Can't send further Emails due to Wrong Password / 'Less Secure Apps not Enabled' / Email is bocked"
                    logval=0
                    finalreport.append(tempi)
                uid+=1

    else:
        time.sleep(1)
        print("\n\nServer Response: Some Domains in the Credential file are not given access to send emails")
        return
                
    

#     with open(file_name, 'w', newline='') as csvfile: 
#         writer = csv.DictWriter(csvfile, fieldnames = fname) 
#         writer.writeheader() 
#         writer.writerows(finalreport)
    
#     field_names = ['Unique_Id', 'Sender', 'Sent','Receiver'] 
#     Report=[]
#     for i in d_f_mail:
#         if '@' not in i :
#             continue
#         temp={}
        
#         if i in sent:
#             temp['Unique_Id']=sent_report[i][0]
#             temp['Sender']=sent_report[i][1]
#             temp['Sent']='YES'
#             temp['Receiver']=i
#         else:
#             temp['Unique_Id']=-1
#             temp['Sender']='Not Assigned'
#             temp['Sent']='NO'
#             temp['Receiver']=i
#         Report.append(temp)
    if flag==1 and len(blocked)==0:
        print("\n\nCongratulations!! E-Mail Successfully Sent to all Email Ids!!")
    else:
        print("\n\nOops!! Some Email Ids Blocked/Not Worked , Task was not completed!!")
    print("\n\nDo You want to download the whole report?? (Y for YES | N for NO)")
    ch=input()
    while(True):
        if(ch=='y' or ch=='Y' or ch=='N' or ch=='n'):
            break
        print('Y for YES | N for NO')
        ch=input()
    if ch=='Y' or ch=='y':
        random.shuffle(finalreport)
        n = random.randint(0,1000)
        fname=['Unique_id','Sender_id','Sent','Sender','Receiver','Log']
        file_name='Server_Output_ID_{}.csv'.format(n)
        file_dir = baseOutputDir + file_name
        with open(file_dir, 'w', newline='') as csvfile: 
            writer = csv.DictWriter(csvfile, fieldnames = fname) 
            writer.writeheader() 
            writer.writerows(finalreport)
            time.sleep(2)
            print("\n\nSuccessful!! Complete Report saved with name '{}' in Campaign Number '{}' ".format(file_name,currentInstance))
    print("\n\nThank You for using the Software!!")
    
            
            
            
    
            



def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
#         info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


def first():
    # global boolhtml
    print("**GETTING SYSTEM INFORMATION\n")
    # time.sleep(1)
    pprint.pprint(json.loads(getSystemInfo()))

    # print(platform.uname())
    print("\n\n**CHECKING SYSTEM COMPATIBILITY ",end="")
    time.sleep(1)
    print('.',end="")
    time.sleep(1)
    print('.',end="")
    time.sleep(1)
    print('.',end="")
    time.sleep(1)
    if uuid.getnode()==user_mac_add:
        global boolhtml
        global maxInstancesAllowed
        global currentInstance
        global baseInputDir
        global baseOutputDir
        global bool_instance_check

        print("         --ACCESS GRANTED--")
        s="\n\nHEYY!! WELCOME TO SUPER-MAIL SENDER"
        print(s,"\n")
        if (bool_instance_check==0):
            print("\nMaximum Number of Remote Server allocated for your Id are {}. To increase this limit, Please contact Admin.".format(maxInstancesAllowed))
            n=input()
            return

        print("\nEnter the Campaign Number(Maximum {} Remote Server Allocated) ".format(maxInstancesAllowed))
        currentInstance = int(input().strip())
        while (True):
            if currentInstance<=maxInstancesAllowed and currentInstance>0:
                break
            print("\nMaximum Number of Remote Server allocated for your Id are {}. To increase this limit, Please contact Admin.".format(maxInstancesAllowed))
            print("\nEnter the Campaign Number again(Maximum {} Remote Server Allocated)".format(maxInstancesAllowed))
            currentInstance = int(input().strip())
        baseInputDir = baseFixedDir + "\\Campaigns\\" + str(currentInstance)
        baseOutputDir = baseFixedDir + "\\Campaigns\\{}\\Output\\".format(currentInstance)
        print("\nPress 'Y' if Email body is HTML Else press 'N' ")
        checkhtml=input()
        while(True):
            if(checkhtml=='y' or checkhtml=='Y' or checkhtml=='N' or checkhtml=='n'):
                break
            print('\nPress "Y" if Email body is HTML Else press "N"')
            checkhtml=input()
        if(checkhtml=='Y' or checkhtml=='y'):
            boolhtml=1
        else:
            boolhtml=0
        func()
    else :
        print("     XXXX-ACCESS DENIED-XXXX")
        print("\n\nOOPSIE!! YOU ARE NOT THE REGISTERED USER")

    n=input()



# main start
current_time = datetime.datetime.now() 
expiry_yr=2021
expiry_mo=6
expiry_dt=20
# cur_yr=int(dt_Kl.strftime('%Y'))
# cur_mo=int(dt_Kl.strftime('%m'))
# cur_dt=int(dt_Kl.strftime('%d'))
cur_yr= current_time.year
cur_mo = current_time.month
cur_dt = current_time.day
acceptTnC=1


def TnC():
    global acceptTnC
    while acceptTnC!=1:
        print('You are using SuperBulkEmailSender for the first time in your PC. Read the whole Terms and Conditions Agreement available at (https://mayanku1999.github.io/TnC/) and press "Y" if you accept it.')
        bool_check_tnc=input()
        if bool_check_tnc=='Y' or bool_check_tnc=='y':
            acceptTnC=1




if (bool_check) and ((cur_yr<expiry_yr) or (cur_yr==expiry_yr and cur_mo<expiry_mo) or (cur_yr==expiry_yr and cur_mo==expiry_mo and cur_dt<expiry_dt) or (cur_yr<=expiry_yr and cur_mo<=expiry_mo and cur_dt<=expiry_dt)):
    if acceptTnC==0:
        TnC()

    first()
    n=input()
else :
    print("RUN TIME ERROR!! \nSystem compatibility checking failed. Please Contact Admin\n") 
    time.sleep(3)
    print("Possible Reasons:\n* 500 Internal Server Error")
    n=input()

