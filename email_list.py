import pickle
with open('email_list.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)
    email_list = data['email_list']
print(len(email_list))



