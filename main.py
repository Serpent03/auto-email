import smtplib
import csv
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

hostID = "debsoc.cuiet@chitkara.edu.in"
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(hostID, "bqty jiuf dmjb prmh")


def newline():
    return "<br><br>"

def style_text(text, bold=False, italics=False):
    msg = text
    if italics:
        msg = f"<i>{msg}</i>"
    if bold:
        msg = f"<b>{msg}</b>"
    return msg


def _send_email(rec, recMail, imgbin, imgfileName):

    style = """
<style>
body {
font-family: "Arial";
font-size: 16px;
}
b {
font-size: 22px;
}
</style>
"""
    mainBody = f"""
        {style}
<!DOCTYPE html>
<title>Text Example</title>
<div class="container">
<p>Dear {rec},</p>
<br>
We hope this email finds you filled with the same enthusiasm that brought you to our group discussion competition. It's with immense pleasure that we announce the conclusion of this thought-provoking event, and we're thrilled to share some fantastic news with you.
{newline()}
{style_text("Drumroll, please! 🥁", bold=True)}
{newline()}
{style_text("🎉 Congratulations! 🎉", bold=True)}
{newline()}
We are delighted to present you with your well-deserved participation certificate which not only symbolises your active involvement but also acknowledges your commitment to intellectual exploration and meaningful dialogue. Please find your certificate attached to this email.
{newline()}
{style_text("What's Next: 🚀", bold=True)}
{newline()}
While the event might have concluded, the conversations don't have to end. Stay connected with us for updates on upcoming debates, events, workshops, and more engaging discussions. Your voice matters, and we're excited to see how you continue to contribute to shaping meaningful conversations.
{newline()}
{style_text("Spread the Word: 📢", bold=True)}
{newline()}
Did the group discussion inspire you? Do you think your friends missed out on something exceptional? Encourage them to join our future events by sharing your accomplishments on your social media platforms and don’t forget to tag us. Let's build a community of thoughtful individuals who are passionate about making a difference.
{newline()}
- Follow us on Instagram <a href="https://www.instagram.com/debsoc_chitkara/">@debsoc_chitkara</a>
<br>
- Check out our Linkedin page <a href="https://www.linkedin.com/company/debsoc-cuiet/">@debsoc-cuiet</a>
{newline()}
<p>Best regards,</p>
<div>Ashwin Kumar
<br>
President
<br>
The Debating Society
<br>
CUIET | Chitkara University</div>
</div>
"""

    message = MIMEMultipart("")
    message["Subject"] = "Congratulations! Your Participation Certificate for Finding Common Ground"

    message["From"] = hostID
    message["To"] = recMail
    image = MIMEImage(imgbin, name=os.path.basename(imgfileName))

    message.attach(MIMEText(mainBody, 'html'))
    message.attach(image)

    s.sendmail(hostID, recMail, message.as_string())
    print(f"Name: {rec}\nEmail: {recMail}\nImg: {imgfileName}\n\n")


def _debug(rec, recMail, imgbin, imgFileName):
    print(rec, recMail, imgFileName)


ticker = 1
resend = []

with open('mail.csv', 'r') as f:
    participantList = csv.reader(f)
    for i in participantList:
        try:
            _name = i[0]
            _email = i[1]
            with open(f"{ticker}.png", "rb") as img:
                img_binary = img.read()
                _send_email(_name, _email, img_binary, f"{ticker}.png")
                # _debug(_name, _email, img_binary, f"{ticker}.png")
                img.close()
        except Exception as e:
            print(e)
            resend.append(ticker)
            # break
        ticker += 1

print(resend)
s.quit()
