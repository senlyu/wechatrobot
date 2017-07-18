
# coding: utf-8

# In[7]:

import itchat
import smtplib
from email.mime.text import MIMEText
from itchat.content import TEXT


# In[8]:

# login
#itchat.auto_login(enableCmdQR=2)


# In[9]:

# listen to the message and send back
#send_msg(msg='Text Message', toUserName=None)


# In[ ]:




# In[10]:

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




# In[11]:


@itchat.msg_register(TEXT, isGroupChat=True)
def print_content(msg):
    flag = False
    if (msg['Text'][:3] == '#机会'):
        itchat.send(msg='已经将以上信息发送到邮箱，标签机会', toUserName=msg['FromUserName'])
        email_type = '机会'
        flag = True
    if (msg['Text'][:3] == '#经验'):
        itchat.send(msg='已经将以上信息发送到邮箱，标签经验', toUserName=msg['FromUserName'])
        email_type = '经验'
        flag = True
    if (msg['Text'][:3] == '#测试'):
        itchat.send(msg='这是一条自动信息', toUserName=msg['FromUserName'])
    if (msg['Text'][:3] == '#介绍'):
        itchat.send(msg='我是Sam的小号机器人，我才刚诞生很不完善，我目前的工作是为Sam处理微信信息碎片化的问题,同时也向大家开放。目前只有一个功能，将机会信息和经验信息，转发到邮箱。还麻烦学长学姐同学们，有分享的信息，用特殊字开头，目前仅有：#机会，#经验，邮箱信息查询输入#邮箱', toUserName=msg['FromUserName'])
    if (msg['Text'][:3] == '#邮箱'):
        itchat.send(msg='邮箱是bapm_career_faq@163.com,密码是100hartford,其中有两个标签，对应两个不同内容，大家可以在转发到自己的邮箱来管理', toUserName=msg['FromUserName'])
    #    email_list.append(msg[3:])
    if (msg['Text'][:3] == '#帮助'):
        itchat.send(msg='如需要帮助，如果想一起做这个小玩意，请联系我，阿森Ｓam，第一次做这样的东西，多多包涵', toUserName=msg['FromUserName'])
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



