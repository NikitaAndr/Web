from flask import Flask, render_template, request, url_for
from data import db_session
from data.users import User
from data.Jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

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


def add_all():
    db_sess = db_session.create_session()
    users = (User(surname='Scott',
                  name='Ridley',
                  age=21,
                  position='captain',
                  speciality='research engineer',
                  address='module_1',
                  email='scott_chief@mars.org'),
             User(surname='Andreev',
                  name='Nikita',
                  age=15,
                  position='team_lid',
                  speciality='None',
                  address='module_2',
                  email='Nikita@mars.org'),
             User(surname='Pastuhov',
                  name='Oleg',
                  age=30,
                  position='director',
                  speciality='teacher',
                  address='module_200',
                  email='Pastuhov@mars.org'),
             User(surname='Jp',
                  name='Python',
                  age=150,
                  position='Main',
                  speciality='Jp',
                  address='None',
                  email='python@mars.org'),
             )
    for user in users:
        db_sess.add(user)
    db_sess.commit()


def first_job():
    job = Jobs(team_leader=1,
               job='deployment of residential modules 1 and 2',
               work_size=15,
               collaborators='2, 3',
               is_finished=False)
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    db_session.global_init("db/blogs.db")
