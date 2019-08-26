from flask import Flask, flash, render_template



# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def default():
   return render_template('index.html')

@app.route('/main.html')
def main():
   return render_template('main.html')

@app.route('/audio.html')
def audio():
   return render_template('audio.html')

@app.route('/pensamiento.html')
def pensamiento():
   return render_template('pensamiento.html')

@app.route('/acerca.html')
def acerca():
   return render_template('acerca.html')

@app.route('/terms_and_conditions.html')
def terms():
   return render_template('terms_and_conditions.html')


@app.route('/privacy_policy.html')
def privacy():
   return render_template('privacy_policy.html')

@app.route('/masaliento1.html')
def masaliento1():
   return render_template('masaliento1.html')