
# coding: utf-8

# In[1]:

import itchat
import smtplib
from email.mime.text import MIMEText
from itchat.content import TEXT


# In[2]:

# login
#itchat.auto_login(enableCmdQR=2)


# In[3]:

# listen to the message and send back
#send_msg(msg='Text Message', toUserName=None)


# In[ ]:




# In[4]:

# function: send email
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


# In[ ]:




# In[6]:


@itchat.msg_register(TEXT, isGroupChat=True)
def print_content(msg):
    flag = False
    if (msg['Text'][:3] == '#机会'):
        itchat.send(msg='A', toUserName=msg['FromUserName'])
        email_type = '机会'
        flag = True
    if (msg['Text'][:3] == '#经验'):
        itchat.send(msg='B', toUserName=msg['FromUserName'])
        email_type = '经验'
        flag = True
    if (msg['Text'][:3] == '#测试'):
        itchat.send(msg='这是一条自动信息', toUserName=msg['FromUserName'])
    #if (msg['Text'][:2] == '#邮箱'):
    #    itchat.send(msg='请按照“邮箱me@senlyu.com”的形式发送', toUserName=msg['FromUserName'])
    #    email_list.append(msg[3:])
    if (flag):
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



