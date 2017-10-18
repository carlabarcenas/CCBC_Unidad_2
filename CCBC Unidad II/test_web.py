from flask import Flask, render_template, request, redirect
from test_module import area, volumen

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='CCBC Unidad II')


@app.route('/exec_area', methods=['GET', 'POST'])
def execute() -> 'html':
    a = int(request.form['a'])
    b = int(request.form['b'])
    c = int(request.form['c'])
    title = 'This is the equation\'s result'
    result = area(a, b, c)
    return render_template('result.html',
                           the_title=title,
                           the_a=a,
                           the_b=b,
                           the_c=c,
                           the_result=result, )


if __name__ == '__main__':
    app.run('localhost', 5001, debug=True)
