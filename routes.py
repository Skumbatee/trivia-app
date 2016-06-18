from flask import Flask,url_for,request,render_template
from app import app

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
		#read form data 
		questions= AnswerQuestions(request.form['title'],request.form['question'],request.form['answer'])

		#store data in db 
		db.session.add(questions)
		db.session.commit()



		return render_template('Createdquestion.html',question = question) 
	else:
		return '<h2>Invalid request</h2>'

# server/question/<title>
@app.route('/question/<title>',methods=['GET','POST'])
def question(title):
	if request.method == "GET":
		#send user the form
		question  = 'Question here'
		#read question from data store
		return render_template(AnswerQuestion.html,question = question)

	elif request.method == "POST":
		#user has attempted to answer.Check if they are correct
		submittedAnswer = request.form['submittedAnswer']

		#Read answer from data Store

		answer = "Answer"

		if submittedAnswer == answer:
			return render_template('Correct.html')

		else:
			return render_template ('Incorrect.html',submittedAnswer =submittedAnswer, answer =answer)



	else:
		return '<h2>Invalid request</h2>'

