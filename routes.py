from flask import Flask,url_for,request,render_template
from app import app,AskQuestions,db

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
		quiz = AskQuestions(request.form['question'],request.form['title'],request.form['answer']) 
		# if not db.session.query(AskQuestions).filter(AskQuestions.question == question).count():
		# 	quiz = AskQuestions(question)
		# 	db.session.add(quiz)
		# 	db.session.commit()
		# 	return render_template('Createdquestion.html')
		# return render_template('CreateQuestions.html')
		# # AskQuestions(request.form['title'],request.form['question'],request.form['answer'])
		print quiz
		#store data in db 
		db.session.add(quiz)
		db.session.commit()

		return render_template('Createdquestion.html', quiz=quiz)
	else:
		return '<h2>Invalid request</h2>'

# server/question/<title>
@app.route('/question/<title>',methods=['GET','POST'])
def questions(title):
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