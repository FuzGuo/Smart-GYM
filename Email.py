import smtplib
import random
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailVerificationSender:
    def __init__(self):
        self.mail_config = {
            "from": '1661391201@qq.com',  # QQ邮箱地址
            "pwd": 'twvsbfzmblelcjcf',  # QQ邮箱授权码
            "smtp": 'smtp.qq.com',  # QQ邮箱SMTP服务器
        }

    def generate_verification_code(self, size=6):
        """生成随机数字验证码，长度默认为6位"""
        numbers = '0123456789'
        return ''.join(random.choice(numbers) for _ in range(size))

    def send_verification_email(self, receiver_email):
        """发送验证邮件到指定的邮箱，并返回验证码"""
        verification_code = self.generate_verification_code()

        msg = MIMEMultipart('alternative')
        msg['Subject'] = Header('验证码', 'utf-8')
        msg['From'] = self.mail_config['from']
        msg['To'] = receiver_email

        # 邮件内容，包括验证码
        content = f"您的验证码是：{verification_code}"
        html_message = MIMEText(content, 'plain', 'utf-8')

        msg.attach(html_message)

        try:
            server = smtplib.SMTP(self.mail_config['smtp'])
            server.login(self.mail_config['from'], self.mail_config['pwd'])
            server.sendmail(self.mail_config['from'], [receiver_email], msg.as_string())
            server.quit()
            print('验证码已发送')
            return verification_code
        except Exception as e:
            print('发送邮件失败:', e)
            return None

# 使用示例
# if __name__ == "__main__":
#     email_sender = EmailVerificationSender()
#     receiver = '1661391201@qq.com'  # 收件人邮箱
#     code = email_sender.send_verification_email(receiver)
#     print("发送的验证码:", code)
