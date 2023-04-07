from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return "Миссия Колонизация Марса"


@app.route('/index/<title>', methods=['GET', 'POST'])
def index(title):
    return render_template('base.html', title=title)


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


@app.route('/carousel')
def carousel():
    return render_template('carousel.html')


@app.route('/training/<prof>', methods=['GET', 'POST'])
def training(prof):
    return render_template('training.html', prof=prof, title=prof)


@app.route('/list_prof/<num>', methods=['GET', 'POST'])
def list_prof(num):
    sp = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, климатолог, ' \
         'специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог,' \
         ' оператор марсохода, киберинженер, штурман, пилот дронов'.split(', ')
    return render_template('list_prof.html', num=num, title='Список профессий', sp=sp)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
