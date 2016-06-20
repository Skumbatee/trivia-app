from flask import Flask,url_for,request,render_template
from app import app
import redis

#making redis connection
r =redis.StrictRedis(host="localhost",port=6379,db=0,charset="utf-8",decode_responses=True)

#server/
@app.route('/')
def hello():
	createLink = "<a href='" + url_for('create') + "'>Create a question </a>"
	return """<html>
					<head>
						<title>Home</title>
					</head>
					<body>
						""" + createLink + """
					</body>
				</html>"""



#server/create

@app.route('/create',methods=['GET','POST'])
def create():
	if request.method == 'GET':
		#send the user the form
		return render_template('CreateQuestions.html')
	elif request.method == 'POST':
		#read form data and save it
		title = request.form ['title']
		question= request.form ['question']
		answer = request.form ['answer']

		#store data in data store
		#key will be whatever title they typed in : Question
		r.set(title+':question',question)
		r.set(title+':answer',answer)


		return render_template('Createdquestion.html', question=question)
	else:
		return '<h2>Invalid request</h2>'

# server/question/<title>
@app.route('/question/<title>',methods=['GET','POST'])
def questions(title):
	if request.method == "GET":
		#send user the 
		#read question from data store

		question  = r.get(title+':question')
		
		return render_template('AnswerQuestion.html',question = question)

	elif request.method == "POST":
		#user has attempted to answer.Check if they are correct
		submittedAnswer = request.form['submittedAnswer']

		#Read answer from data Store

		answer = r.get(title+':answer')

		if submittedAnswer == answer:
			return render_template('Correct.html')

		else:
			return render_template ('Incorrect.html',submittedAnswer =submittedAnswer, answer =answer)



	else:
		return '<h2>Invalid request</h2>'