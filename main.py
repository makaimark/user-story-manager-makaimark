from flask import Flask, request, render_template

from models import *

app = Flask(__name__)

@app.route('/story')
def story():
    return render_template('form.html')

@app.route('/story', methods=['POST'])
def handle_data():
    user_story = UserStory.create(story_title = request.form['story_title'],
                            user_story=request.form['user_story'],
                            acceptance_criteria=request.form['acceptance_criteria'],
                            business_value = request.form['business_value'],
                            estimation = request.form['estimation'],
                            status=request.form['status'])
    return "Uploaded to the database"

@app.route('/')
@app.route('/list')
def list_data():
    query = UserStory.select()
    return render_template('list.html', user_stories = query)

if __name__ == '__main__':
    app.run()
