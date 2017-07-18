
# coding: utf-8

# In[73]:

import itchat
import smtplib
import pickle
from email.mime.text import MIMEText
from itchat.content import TEXT






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
    #server.login(fromaddr,"qwer1234")
    server.set_debuglevel(1)
    #for toaddrs in email_list:
    server.sendmail(fromaddr, 'resembleblue@gmail.com', msg.as_string())
    
    server.quit()

send_email('1','nothing')
# In[53]:

#test email add
#add_email('jobs@senlyu.com')


# In[55]:

#test email delete
#delete_email('123@123.com')


# In[96]:

#show_email()



# In[13]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:







# In[ ]:



