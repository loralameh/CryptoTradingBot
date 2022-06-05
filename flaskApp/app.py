from flask import Flask, render_template, url_for
import os
app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER
@app.route("/")
@app.route("/home")
def home():
    profile1 = os.path.join(app.config['UPLOAD_FOLDER'], 'profile1.jpg')
    profile2 = os.path.join(app.config['UPLOAD_FOLDER'], 'profile2.jpg')
    return render_template('home.html',profile1 = profile1,profile2 = profile2)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/predictions")
def predictions():
    twitter_pic = os.path.join(app.config['UPLOAD_FOLDER'], 'twitter.png')
    return render_template('predictions.html', title='Predictions',twitter_pic=twitter_pic)


if __name__ == '__main__':
    app.run(debug=True)