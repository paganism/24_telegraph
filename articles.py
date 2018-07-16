import os, datetime, re, json


def get_name_article(header):
    cur_date = datetime.datetime.now()
    month = cur_date.month
    day = cur_date.day
    header = re.sub('[/\'"#.!@`]', '', header)
    header = re.sub(' ', '-', header)
    art_name = '%s-%s-%s' % (header, month, day)
    counter = 0
    if os.path.exists('articles/%s' % art_name):
        counter+=1
        art_name = '%s-%s' % (art_name, counter)
    return art_name


def article_save(header, signature, body, article_name, token):
    article = {'header': header,
               'signature': signature,
               'body': body,
               'token': token
               }
    with open('article/%s.json' % article_name, 'w') as article_file:
        json.dump(article, article_file)


def get_article(article_name):
    with open('article/%s.json' % article_name, 'r') as article_file:
        return json.loads(article_file.read())


if __name__ == "__main__":
    pass
