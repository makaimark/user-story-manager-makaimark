from flask import *

from models import *

app = Flask(__name__)


@app.route('/story', methods=['GET'])
def story():
    empty_object = UserStory(story_title = "", user_story = "", acceptance_criteria = "", business_value = "100",
                             estimation = "0.5", status = "choose an option")
    return render_template('form.html', user_story = empty_object)


@app.route('/story', methods=['POST'])
def handle_data():
    user_story = UserStory.create(story_title = request.form['story_title'],
                            user_story=request.form['user_story'],
                            acceptance_criteria=request.form['acceptance_criteria'],
                            business_value = request.form['business_value'],
                            estimation = request.form['estimation'],
                            status=request.form['status'])
    return "Uploaded to the database"

@app.route('/story/<story_id>', methods=['POST'])
def update_data(story_id):
    data = UserStory.get(UserStory.id == story_id)
    data.update(story_title = request.form['story_title'],
                            user_story=request.form['user_story'],
                            acceptance_criteria=request.form['acceptance_criteria'],
                            business_value = request.form['business_value'],
                            estimation = request.form['estimation'],
                            status=request.form['status'])
    return "Updated"


@app.route('/story/<story_id>', methods=['GET'])
def show_data(story_id):
    data = UserStory.get(UserStory.id == story_id)
    return render_template("form.html", user_story = data)


@app.route('/delete/<story_id>', methods=['GET'])
def delete_data(story_id):
    data = UserStory.get(UserStory.id == story_id)
    data.delete_instance()
    return redirect('http://localhost:9876/list')


@app.route('/')
@app.route('/list')
def list_data():
    query = UserStory.select()
    return render_template('list.html', user_stories = query,  web2='http://localhost:9876/delete', web='http://localhost:9876/story')


if __name__ == '__main__':
    app.run()
