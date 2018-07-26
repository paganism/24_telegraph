from flask import Flask, render_template, request, url_for, redirect, make_response
import uuid, os
from flask_wtf.csrf import CSRFProtect
from articles import get_name_article, article_save, get_article


app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        if not request.cookies.get('token'):
            token = str(uuid.uuid4())
        else:
            token = request.cookies.get('token')
        header = request.form['header']
        signature = request.form['signature']
        body = request.form.get('body')
        article_name = get_name_article(header)
        article_save(header, signature, body, article_name, token)
        resp = make_response(redirect(url_for('show_posted_page', article=article_name)))
        resp.set_cookie('token', token)

    else:
        return render_template('form.html')
    return resp


@app.route('/<article>/', methods=['POST', 'GET'])
def show_posted_page(article):
    raw_article = get_article(article)
    if raw_article['token'] != request.cookies.get('token'):
        return render_template('read_only_page.html',
                        token=raw_article['token'],
                        header=raw_article['header'],
                        signature=raw_article['signature'],
                        body=raw_article['body'])
    if request.method == 'POST':
        token = raw_article['token']
        header = request.form['header']
        signature = request.form['signature']
        body = request.form['body']
        article_save(header, signature, body, article, token)
        return redirect(url_for('show_posted_page', article=article))

    return render_template('page.html',
                           token=raw_article['token'],
                           header=raw_article['header'],
                           signature=raw_article['signature'],
                           body=raw_article['body'])


if __name__ == "__main__":
    app.run()
