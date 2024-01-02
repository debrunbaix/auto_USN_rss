content_start = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" type="text/css" hs-webfonts="true" href="https://fonts.googleapis.com/css?family=Lato|Lato:i,b,bi">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style type="text/css">
          h1{{font-size:56px;color:white}}
          h2{{font-size:28px;font-weight:900;color:A7D397}}
          h3{{color:white}}
          p{{font-weight:100;color:white}}
          td{{vertical-align:top}}
          #email{{margin:auto;width:600px;background-color:#414141}}
        </style>
    </head>
    <body bgcolor="#2D2727" style="width: 100%; font-family:Lato, sans-serif; font-size:18px;">
    <div id="email">
        <table role="presentation" width="100%">
            <tr>
                <td bgcolor="#8F43EE" align="center" style="color:#413543;">
                    <h1> Ubuntu Security News !</h1>
                </td>
    '''
content_end = """
    </div>
    </body>
    </html>
    """

def creating_artical_mail_content_structure(article, emailContent):
    content = f"""
                </table>
                <table role="presentation" border="0" cellpadding="0" cellspacing="10px" style="padding: 30px 30px 30px 60px;">
                    <tr>
                        <td>
                            <h2>{article.title}</h2>
                            <h3>{article.link}</h3>
                            <p>
                                {article.summary}
                            </p>
                        </td>
                    </tr>
                </table>
            """
    emailContent = str(emailContent) + str(content)
    return emailContent

def create_mail_content(article_list):
    emailContent = content_start
    for article in article_list:
        emailContent = creating_artical_mail_content_structure(article, emailContent)

    emailContent = emailContent + content_end
    return emailContent