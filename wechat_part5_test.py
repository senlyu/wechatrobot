
# coding: utf-8

# In[24]:

import itchat
import smtplib
import pickle
from email.mime.text import MIMEText
from itchat.content import TEXT


# In[ ]:




# In[2]:

# login
#itchat.auto_login(enableCmdQR=2)


# In[3]:

# listen to the message and send back
#send_msg(msg='Text Message', toUserName=None)


# In[25]:

with open('email_list_test.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)
    email_list = data['email_list']


# In[40]:

# function: send email
def send_email(email_type,email_content):
    fromaddr = "me@senlyu.com"

    subject = email_type
    content = email_content
    text_subtype = 'plain'
    msg = MIMEText(content, text_subtype)
    msg['Subject']= subject
    msg['From']   = fromaddr


    print("Message length is", len(msg))

    server = smtplib.SMTP('localhost',25)
    #server.login(fromaddr,password)
    server.set_debuglevel(1)
    for toaddrs in email_list:
        server.sendmail(fromaddr, toaddrs, msg.as_string())
    
    server.quit()


# In[27]:

def add_email(new_email):
    # An arbitrary collection of objects supported by pickle.
    email_list.append(new_email)
    data = {
        'email_list' : email_list
    }

    with open('email_list_test.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(data, f)


# In[28]:

def delete_email(new_email):
    email_list.remove(new_email)
    data = {
        'email_list' : email_list
    }

    with open('email_list_test.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
        pickle.dump(data, f)


# In[29]:

def show_email():
    result = ''
    for ele in email_list:
        result = result + ele + ';'
    return result


# In[53]:

#test email add
#add_email('jobs@senlyu.com')


# In[33]:

#test email delete
#delete_email('')


# In[36]:

#show_email()


# In[37]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:


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
        itchat.send(msg='我是Sam的小号机器人，我才刚诞生很不完善，我目前的工作是为Sam处理微信信息碎片化的问题，大家也可以使用。目前只有一个功能，将机会信息和经验信息，转发到邮箱。还麻烦学长学姐同学们，有分享的信息，用特殊字开头，目前仅有：#机会，#经验，邮箱信息查询输入#邮箱', toUserName=msg['FromUserName'])
    if (msg['Text'][:3] == '#邮箱'):
        itchat.send(msg='邮箱可以通过#添加邮箱，#删除邮箱，#显示列表，来管理，邮箱从us@senlyu.com发出，发出的邮件以“机会”或“经验”为标题，内容为整个消息，大家可以在自己邮箱设置tag来管理。举个例子，今天我发布了信息如下：#经验OPT经验。那么在邮箱列表里的邮箱会收到一封来自us@senlyu.com，以“经验”为标题，以“#经验OPT经验”为内容的邮件', toUserName=msg['FromUserName'])
    #    email_list.append(msg[3:])
    if (msg['Text'][:5] == '#添加邮箱'):
        add_email(msg['Text'][6:])
        itchat.send(msg='已添加'+msg['Text'][6:], toUserName=msg['FromUserName'])
    if (msg['Text'][:5] == '#删除邮箱'):
        delete_email(msg['Text'][6:])
        itchat.send(msg='已删除'+msg['Text'][6:], toUserName=msg['FromUserName'])
    if (msg['Text'][:5] == '#显示列表'):
        itchat.send(msg=show_email(), toUserName=msg['FromUserName'])   
    if (msg['Text'][:3] == '#帮助'):
        itchat.send(msg='如需要帮助，如果想一起改进这个小玩意，请联系我，阿森Ｓam，第一次做这样的东西，多多包涵', toUserName=msg['FromUserName'])
    if (msg['Text'][:3] == '#测试邮箱'):
        itchat.send(msg='已经将以上信息发送到邮箱，标签经验', toUserName=msg['FromUserName'])
        email_type = '经验'
        email_content = msg['Text']
        send_email(email_type,email_content)
    if (flag):
        email_content = msg['Text']
        send_email(email_type,email_content)
    
    

itchat.auto_login(hotReload=True)
itchat.run()


# In[12]:




# In[23]:




# In[13]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:







# In[ ]:



