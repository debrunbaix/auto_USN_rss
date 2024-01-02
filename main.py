import feedparser
from date_script import convert_article_date, get_today_date
from mail_front_script import create_mail_content
from send_mail_script import sendmail

url = "https://ubuntu.com/security/notices/rss.xml"
article_file = "article.txt"

blog_feed = feedparser.parse(url)

article_date = blog_feed.entries[0].published

all_posts = blog_feed.entries
posts_number = len(all_posts)

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

def write_mail_content(article):
    article_to_send.append(article)

def select_article(today_date, all_posts):

    # target_date_str = "2023-12-19"
    # target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()
    target_date = today_date

    for post in all_posts:
        post_date = convert_article_date(post.published)
        if post_date == target_date :
            if not check_article_sent_status(post):
                write_mail_content(post)

def main():
    today = get_today_date()

    select_article(today, all_posts)    

    if len(article_to_send) != 0:
        mail_content = create_mail_content(article_to_send)
        sendmail(mail_content)
    else:
        print('No mail send')
main()