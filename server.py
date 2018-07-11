from flask import Flask, render_template, request, url_for
import os
import json


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        input_dict = {'username': request.cookies.get('username'),
                      'header': request.form.get('header'),
                      'signature': request.form.get('signature'),
                      'body': request.form.get('body')
                      }
        print(input_dict)
        print(request.cookies)
        with open('./file', 'w') as article:
            article.write(str(json.dumps(input_dict)))
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


if __name__ == "__main__":
    app.run()
