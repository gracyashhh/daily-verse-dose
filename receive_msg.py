from flask import Flask,request,render_template
from twilio.twiml.messaging_response import MessagingResponse
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sms',methods=['GET','POST'])
def msg_reply():
    resp=MessagingResponse()
    user=request.form.get('From')
    resp.message(f"Great job smarty pants {user}")
    return str(resp)

if __name__=="__main__":
    app.run(debug=True)