from smtplib import SMTP


s = SMTP('localhost', 8025)
s.sendmail('anne@macascript.com', ['bart@macascript.com'], """\
From: anne@macascript.com
To: bart@macascript.com
Subject: A test
testing
""")
s.quit()