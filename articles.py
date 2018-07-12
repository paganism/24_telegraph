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


def article_save(article_name, article_data):
    with open('articles/%s' % article_name, 'w') as article_file:
        article_file.write(str(json.dumps(article_data)))


if __name__ == "__main__":
    print(get_name_article('the last day'))
