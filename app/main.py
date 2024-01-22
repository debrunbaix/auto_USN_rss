import feedparser
from time import sleep, localtime, strftime
from mail_front_script import create_mail_content
from send_mail_script import sendmail

article_file = "article.txt"
log_file = "log.txt"

article_to_send = []

def write_in_file(text, file):
    with open(file, 'a') as file_to_write:
        file_to_write.write(text + '\n')

def check_article_sent_status(article):
    with open(article_file, 'r') as file:
        file_content = file.read()
        article_title = article.title
        if article_title in file_content:
            return True
        else:
            write_in_file(article_title, article_file)
            print(f'Article {article.title} added.')
            write_in_file(f'Article {article.title} added.', log_file)
            return False

def update_rss_article():
    url = "https://ubuntu.com/security/notices/rss.xml"
    blog_feed = feedparser.parse(url)
    all_posts = blog_feed.entries

    return all_posts

def main():
    all_posts = update_rss_article()

    for post in all_posts: article_to_send.append(post) if not check_article_sent_status(post) else None

    if len(article_to_send) != 0:
        mail_content = create_mail_content(article_to_send)
        sendmail(mail_content)
    else:
        time_string = strftime("%m/%d/%Y, %H:%M:%S", localtime())
        print(f'No mail send at : {time_string}')
        write_in_file(f'No mail send at : {time_string}', log_file)

while True:
    main()
    article_to_send = []
    sleep(3600)
