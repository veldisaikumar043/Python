# DOWNLOADING A HTML
# import urllib.request
# try:
#     url=urllib.request.urlopen("https://www.python.org/")
#     content=url.read()
#     url.close()
# except urllib.error.HTTPError:
#     print("the webpage is not found")
#     exit()
# # open('python.html', 'wb').write(url.read())
# f=open('python.html','wb')
# f.write(content)
# f.close()

# DOWNLOADING A IMAGE
# import urllib.request
# url = "https://assets.stickpng.com/images/5848152fcef1014c0b5e4967.png"
# urllib.request.urlretrieve(url,"hello.png")
#                     OR
# import urllib.request
# try:
#     url=urllib.request.urlopen("https://www.python.org/static/img/python-logo.png")
#     content=url.read()
#     url.close()
# except urllib.error.HTTPError:
#     print("the webpage is not found")
#     exit()
# f=open('python.png','wb')
# f.write(content)
# f.close()

# EMAIL SENT
# import smtplib
# from email.mime.text import MIMEText
# body="this is a text email. how are you"
# msg=MIMEText(body)
# msg['From']="abc43@gmail.com"
# msg['To']="abc43@gmail.com"
# msg['Subject']="hello"
# server=smtplib.SMTP('smtp.gmail.com',587)
# server.starttls()
# server.login("abc43@gmail.com","abc@123")
# server.send_message(msg)
# print("Mail sent")
# server.quit()

# TO CREATE A SERVER
# import socket
# host='localhost'
# port=4000
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind((host,port))
# print("server listening on port : ",port)
# s.listen(1)
# c,addr=s.accept()
# print("connection from : ",str(addr))
#
# c.send(b"hello, how are you")
# c.send("bye".encode())

# TO CREATE A CLIENT
# import socket
# s=socket.socket()
# s.connect(("localhost",4000))
# msg=s.recv(1024)
# while msg:
#     print("Received : ",msg.decode())
#     msg=s.recv(1024)
# s.close()