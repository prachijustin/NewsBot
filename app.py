from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from utils import fetch_reply

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    print(request.form)
    msg = request.form.get('Body')
    sender = request.form.get('From')

    # Create reply
    resp = MessagingResponse()
    #resp.message("You said: {}".format(msg)).media('https://lh3.googleusercontent.com/proxy/ogwfaF0iwa05OnTNQFyD0rZ384sAN74p5xwJE6qfJmrEFcmgxlXo4zg22lrlaLcaS_hp9pFCu8s8QZ-GgDy37DxWVOHpq2B4IV35vb4wgHBWfJiYqI_AVARVMaguPane4Raedg=w530-h212-p-rw')
    resp.message(fetch_reply(msg, sender))
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
