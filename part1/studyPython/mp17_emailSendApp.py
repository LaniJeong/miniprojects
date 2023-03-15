# 이메일 보내기 앱
import smtplib  # 메일 전송 프로토콜
from email.mime.text import MIMEText

send_email = 'swimming0426@naver.com'
send_pass = '0000' 

recv_email = 'jsm0734@kakao.com'

smtp_name = 'smtp.naver.com'
smtp_port = 587     # 포트 번호

text = '''기현의 솔로앨범 voyager 1주년 입니다.
많은 관심 부탁드립니다.
'''

msg = MIMEText(text)
msg['Subject'] = 'voyager 1주년'
msg['From'] = send_email  # 보내는 메일
msg['To'] = recv_email    # 받는 메일
print(msg.as_string())

mail = smtplib.SMTP(smtp_name, smtp_port)   # SMTP
mail.starttls()             # 전송계층보안 시작
mail.login(send_email, send_pass)
mail.sendmail(send_email, recv_email, msg=msg.as_string())
mail.quit()
print('전송완료!')
