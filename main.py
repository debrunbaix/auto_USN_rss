import feedparser
from time import sleep
from mail_front_script import create_mail_content
from send_mail_script import sendmail

article_file = "article.txt"

# article_date = blog_feed.entries[0].published

article_to_send = []

def check_article_sent_status(article):
    with open(article_file, 'r') as file:
        file_content = file.read()
        article_title = article.title
        if article_title in file_content:
            return True
        else:
            with open(article_file, 'a') as file_to_write:
                file_to_write.write(article_title + '\n')
                print(f'Article {article.title} added.')
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
        print('No mail send')

while True:
    main()
    sleep(3600)