from flask import Flask, render_template, request, url_for, redirect, make_response
import os, random, json
from flask_wtf.csrf import CSRFProtect
from articles import get_name_article, article_save


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'lemon wedges'


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        input_dict = {# 'username': request.cookies.get('username'),
                      'header': request.form['header'],
                      'signature': request.form['signature'],
                      'body': request.form['body']
                      }
        print(input_dict)
        print(request.cookies)
        # with open('./file', 'w') as article:
        #     article.write(str(json.dumps(input_dict)))
        article_name = get_name_article(input_dict['header'])
        article_save(article_name, input_dict)
    else:
        return render_template('form.html')
    return render_template('form.html'), input_dict


@app.route('/articles', methods=['POST', 'GET'])
def page():
    with open('./file', 'r') as article_file:
        raw_article = json.loads(article_file.read())
        print(type(raw_article))
    return render_template('page.html',
                           header=raw_article['header'],
                           signature=raw_article['signature'],
                           body=raw_article['body'])


def plus_one(x):
    return x + 1


if __name__ == "__main__":
    app.run()
