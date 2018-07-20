import os, datetime, re, json


def get_name_article(header):
    cur_date = datetime.datetime.now()
    month = cur_date.month
    day = cur_date.day
    header = re.sub('[/\'"#.!@`]', '', header)
    header = re.sub(' ', '-', header)
    article_slug = '%s-%s-%s' % (header, month, day)
    counter = 0
    if os.path.exists('article/%s.json' % article_slug):
        counter+=1
        art_name = '%s-%s' % (article_slug, counter)
    return article_slug


def article_save(header, signature, body, article_slug, token):
    article = {'header': header,
               'signature': signature,
               'body': body,
               'token': token
               }
    with open('article/%s.json' % article_slug, 'w') as article_file:
        json.dump(article, article_file)


def get_article(article_name):
    with open('article/%s.json' % article_name, 'r') as article_file:
        return json.loads(article_file.read())


if __name__ == "__main__":
    pass
