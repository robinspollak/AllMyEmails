import imaplib,email
import cPickle as pickle
from keys import username,password
from classes import *
def email_from_raw(uid_):
    result, data = mail.uid('fetch',uid_,'(RFC822)')
    raw = data[0][1]
    working_email = email.message_from_string(raw)
    attributes = [working_email['From'],working_email['To'],\
    working_email['Subject'],working_email['Date']]
    for index in range(len(attributes)):
    	if attributes[index] == None:
    		return None #mark emails missing fields for removal later
    	else:
    		attributes[index] = attributes[index].decode('utf-8')
    return myEmail(*attributes)

url = 'imap.gmail.com'
mail = imaplib.IMAP4_SSL(url)
mail.login(username, password)
mail.select('inbox')
result, data = mail.uid('search', None, "ALL") # search and return uids instead
uids = data[0].split()
progress_counter = 0
num_emails = len(uids)
print num_emails
with open('email-data.pkl','wb') as output:
    for working_email in uids:
        print (float(progress_counter)/num_emails)
        pickle.dump(email_from_raw(working_email),output,-1)
        progress_counter+=1

