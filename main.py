from flask import Flask, render_template, request, url_for

app = Flask(__name__)
count_foto = 1


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


@app.route('/carousel', methods=['GET', 'POST'])
def carousel():
    global count_foto
    if request.method == 'POST':
        request.files['photo'].save(f'static/img/img{count_foto}.png')
        count_foto += 1
    return render_template('carousel.html', q=count_foto)


@app.route('/training/<prof>', methods=['GET', 'POST'])
def training(prof):
    return render_template('training.html', prof=prof, title=prof)


@app.route('/list_prof/<num>', methods=['GET', 'POST'])
def list_prof(num):
    sp = 'инженер-исследователь, пилот, строитель, экзобиолог, врач, инженер по терраформированию, климатолог, ' \
         'специалист по радиационной защите, астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог,' \
         ' оператор марсохода, киберинженер, штурман, пилот дронов'.split(', ')
    return render_template('list_prof.html', num=num, title='Список профессий', sp=sp)


@app.route('/answer', methods=['GET', 'POST'])
@app.route('/auto_answer', methods=['GET', 'POST'])
def answer():
    sl = {'Фамилия': 'Андреев',
          'Имя': 'Никита',
          'Образование': 'Начальное',
          'Профессия': 'рабочий учёный инженер',
          'Пол': 'мужской',
          'Мотивация': 'Быть полезным',
          'Готовы остаться на марсе?': 'True'}
    return render_template('answer.html', sl=sl)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
