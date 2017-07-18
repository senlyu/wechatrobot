
# coding: utf-8

# In[6]:


import itchat
import smtplib
from email.mime.text import MIMEText


# In[7]:


# login
#itchat.auto_login(enableCmdQR=2)


# In[8]:


# listen to the message and send back
#send_msg(msg='Text Message', toUserName=None)


# In[9]:


def send_email(email_type,email_content):
    fromaddr = "us@senlyu.com"
    toaddrs  = "bapm_career_faq@163.com"

    subject = email_type
    content = email_content
    text_subtype = 'plain'
    msg = MIMEText(content, text_subtype)
    msg['Subject']= subject
    msg['From']   = fromaddr


    print("Message length is", len(msg))

    server = smtplib.SMTP_SSL('smtp.zoho.com',465)
    server.login(fromaddr,"qwer1234")
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()


# In[10]:


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    if (msg['Text'][:2] == '机会'):
        itchat.send(msg='A', toUserName=msg['FromUserName'])
        email_type = '机会'
    if (msg['Text'][:2] == '经验'):
        itchat.send(msg='B', toUserName=msg['FromUserName'])
        email_type = '经验'
    email_content = msg['Text']
    send_email(email_type,email_content)

itchat.auto_login(hotReload=True)
itchat.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:








# In[ ]:




