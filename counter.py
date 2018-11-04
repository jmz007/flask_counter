from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'mycount'

@app.route('/')
def count():
	if "count" in session:
		session["count"] += 1
	else:
		session["count"] = 1
	print(session["count"])
	return render_template('index.html', count=session["count"])

@app.route('/reset')
def reset():
	session.clear()
	return redirect ('/')

@app.route('/add')
def add():
	session["count"] += 1
	return redirect ('/')

if __name__=="__main__":   
    app.run(debug=True)    