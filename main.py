from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return render_template('promotion.html')


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


@app.route('/astronaut_selection', methods=['GET'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template('astronaut_selection.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')