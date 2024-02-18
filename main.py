import smtplib, csv
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

hostID = "debsoc.cuiet@chitkara.edu.in"
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(hostID, "tolv epml halp jhsz")

def _send_email(rec, recMail, imgbin, imgfileName):

    style = """
<style>
body {
font-family: "Roboto";
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
We hope this email finds you filled with the same enthusiasm that brought you to our remarkable workshop. It's with immense pleasure that we announce the conclusion of this thought-provoking event, and we're thrilled to share some fantastic news with you.
<br>
<br>
<b>Drumroll, please! 🥁</b>
<br>
<br>
<b>🎉 Congratulations! 🎉</b>
<br>
<br>
We are delighted to present you with your well-deserved participation certificate which not only symbolises your active involvement in the workshop but also acknowledges your commitment to intellectual exploration and meaningful dialogue. Please find your certificate attached to this email.
<br>
<br>
<b>What's Next: 🚀</b>
<br>
<br>
While the event might have concluded, the conversations don't have to end. Stay connected with us for updates on upcoming debates, events, workshops, and more engaging discussions. Your voice matters, and we're excited to see how you continue to contribute to shaping meaningful conversations.
<br>
<br>
<b>Spread the Word: 📢</b>
<br>
<br>
Did the workshop inspire you? Do you think your friends missed out on something exceptional? Encourage them to join our future events by sharing your accomplishments on your social media platforms and don’t forget to tag us. Let's build a community of thoughtful individuals who are passionate about making a difference.
<br>
<br> - Follow us on Instagram <a href="https://www.instagram.com/debsoc_chitkara/">@debsoc_chitkara</a>
<br> - Check out our Linkedin page <a href="https://www.linkedin.com/company/debsoc-cuiet/">@debsoc-cuiet</a>
<br> - For more information, visit www.thedebatingsociety.com
<br>
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
    message["Subject"] = "Congratulations! Your Participation Certificate for Articulatia: Crafting Confident Communicators 🏆"

    message["From"] = hostID
    message["To"] = recMail
    image = MIMEImage(imgbin, name=os.path.basename(imgfileName))

    message.attach(MIMEText(mainBody, 'html'))
    message.attach(image)

    s.sendmail(hostID, recMail, message.as_string())
    print(f"Name: {rec}\nEmail: {recMail}\nImg: {imgfileName}\n\n")

# with open("1.png", "rb") as f:
#     rb = f.read()
#     _send_email("DEBATING SOCIETY", hostID, rb, "1.png")

ticker = 27

with open('mail.csv', 'r') as f:
    participantList = csv.reader(f)
    for i in participantList:
        try:
            with open(f"{ticker}.png", "rb") as img:
                img_binary = img.read()
                _send_email(i[1], i[2], img_binary, f"{ticker}.png")
                img.close()
            ticker += 1
        except Exception as e:
            print(e)
            break


s.quit()