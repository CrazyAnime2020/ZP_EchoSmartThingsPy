import os
import echopy_app
import echopy_doc
import echopy_smartthings as myApp
import smartthings_lib as st
import smartthings_settings as settings
import logger
from flask import Flask, render_template, Response, send_from_directory, request, current_app, redirect, jsonify, json
from flask_mail import Mail, Message


app = Flask(__name__)
mail=Mail(app)

app.config.update(
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = settings.mail_username,
	MAIL_PASSWORD = settings.mail_password
	)
mail=Mail(app)

@app.route("/")
def home():
	return echopy_doc.main_page.format(settings.full_root_url)


@app.route(settings.url_root)
def main():
	return echopy_doc.main_page.format(settings.full_root_url)

@app.route("/nest/")
def nest():
	return echopy_doc.nest_page.format(settings.full_root_url)

@app.route(settings.url_root + "/email_test")
def email():
	msg = Message(
			  'Hello',
		   sender='alexa@zpriddy.com',
		   recipients=
			   ['me@zpriddy.com'])
	msg.body = "This is the email body"
	mail.send(msg)
	return "Sent"


@app.route(settings.url_root + "/EchoPyAPI",methods = ['GET','POST'])
def apicalls():
	if request.method == 'POST':
		data = request.get_json()
		print "POST"
		sessionId = myApp.data_handler(data)
		return sessionId + "\n"

@app.route(settings.url_root + "/auth",methods = ['GET','POST'])
def auth():
	if request.method == 'GET':
		return echopy_doc.auth_page

	if request.method == 'POST':
		alexaId=request.form['AlexaID']
		clientId=request.form['SmartThingsClientID']
		clientSecret=request.form['SmartThingsClientSecret']
		clientEmail=request.form['Email']
		#userId = myApp.getUserIdFromAlexaId(alexaId)

		auth_uri = myApp.STAlexaAuth(alexaId,clientId,clientSecret)
		return redirect(auth_uri)


@app.route(settings.url_root + "/oauth2/<path:alexaId>",methods = ['GET'])
def authcode(alexaId):

	code = request.args.get('code')
	userId = myApp.getUserIdFromAlexaId(alexaId)

	if st.smartThingsToken(alexaId, userId,code):

		print "authed..."
		#print st.stData.getUser(userId).getClientInfo().token

		myApp.genNewAlexaId(userId,100)

	return redirect("/alexa")


@app.route(settings.url_root + "/samples",methods = ['GET','POST'])
def samples():
	if request.method == 'GET':
		return echopy_doc.samples_page.format(settings.full_root_url)

	if request.method == 'POST':
		try:
			alexaId=request.form['AlexaID']
			userId = myApp.getUserIdFromAlexaId(alexaId)
			samples = st.getSamples(userId)
			myApp.genNewAlexaId(userId,100)
			return echopy_doc.samples_results.replace('RESULTS',samples.replace('\n','&#13;&#10;')).format(settings.full_root_url)
		except:
			return echopy_doc.samples_results.replace('RESULTS',"AN ERROR HAS ACCRUED").format(settings.full_root_url)





def run_echopy_app():
	import SocketServer
	#SocketServer.BaseServer.handle_error = close_stream
	SocketServer.ThreadingTCPServer.allow_reuse_address = True
	echopy_app.run(app)



if __name__ == "__main__":
	st.smartThingsMongoDBInit()
	logger.init_logging()
	myApp.data_init()
	run_echopy_app()
