from flask import Flask,jsonify 
from flask_restful import Resource, Api, request, reqparse, abort      
import smtplib
from email.message import EmailMessage
from datetime import datetime
import time

app = Flask(__name__)
@app.route("/",methods=["GET"])
def home():
    str="<h1>Welcome!! this is a mailing Rest Api</h1>" + "<h2>Format of post method : - <p>https://mailhelp.herokuapp.com/?emailid=\"To whom you want to send the mail\"&cc=\"To whom you want to add in cc field (',' seperated n no. of email ids can be used)\"&bcc\"To whom you want to add in bcc field (',' seperated n no. of email ids can be used)\"&subject=\"Subject of the mail\"&message=\"Body of mail\"</p></h2><br><h2>Json format : - <br>{<br>'emailid':\"To whom you want to send the mail\",<br> 'cc':\"To whom you want to add in cc field (',' seperated n no. of email ids can be used)\",<br> 'bcc':\"To whom you want to add in bcc field (',' seperated n no. of email ids can be used)\",<br> 'subject':\"Subject of the mail\"&message=\"Body of mail\",<br>'message':\"Body of mail\"<br>}<br></h2>"
    return str



@app.route("/",methods=["GET", "POST"])
def hello_world():
    msg = EmailMessage()
    msg['Subject']=str(request.args.get('subject'))
    msg['From']="hackathonviit@gmail.com"
    msg['To']=str(request.args.get('emailid'))
    print(str(request.args.get('emailid')))
    #cc="ameybobade1103@gmail.com,pmacoe.it@gmail.com"
    msg['Cc'] = (str(request.args.get('cc'))).split(',')
    msg['Bcc'] = (str(request.args.get('bcc'))).split(',')
    # msg['Bcc'] = bcc.split(',')
    msg.set_content(str(request.args.get('message')))

    StartYear = request.args.get('syear')
    StartMonth = request.args.get('smonth')
    StartDate = request.args.get('sdate')
    StartTimehour = request.args.get('shour')
    StartTimemin = request.args.get('smin')
    EndYear = request.args.get('eyear')
    EndMonth = request.args.get('emonth')
    EndDate = request.args.get('edate')
    EndTimehour = request.args.get('ehour')   
    EndTimemin = request.args.get('emin')
    Summary = request.args.get('summary')
    Description = request.args.get('description')
    string="BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VEVENT\nDTSTART:"+str(StartYear)+str(StartMonth)+str(StartDate)+"T"+str(StartTimehour)+str(StartTimemin)+"000\nDTEND:"+str(EndYear)+str(EndMonth)+str(EndDate)+"T"+str(EndTimehour)+str(EndTimemin)+"000\nUID:ameybobade@gmail.com\nSUMMARY:"+Summary+"\nDESCRIPTION:"+Description+"\nEND:VEVENT\nEND:VCALENDAR"
    
    with open('invite.ics', 'w') as my_file:
        my_file.writelines(string)

    
    file = open('invite.ics', 'r')
    if file:
        file_data = file.read()
        file_name = file.name
        print(file_name)
        # msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        msg.add_attachment(file_data, subtype='octet-stream', filename=file_name)
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("hackathonviit@gmail.com", "viithackathon")             
            smtp.send_message(msg)
        result={
            "Status" : "Sent",
            "Time" : time.asctime( time.localtime(time.time()) )
        }
        
    except:
        result={
            "Status" : "Error in Authentication",
            "Time" : time.asctime( time.localtime(time.time()) )
        }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    # app.run(debug=True)

# file = open('sbc.txt', 'r')
# This will print every line one by one in the file
# for each in file:
#     print (each)