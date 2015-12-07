from classes import *
import cPickle as pickle
emails = []
def pickleLoader(pklFile):
    try:
        while True:
            yield pickle.load(pklFile)
    except EOFError:
        pass
with open('email-data.pkl','r') as my_input:
    for item in pickleLoader(my_input):
        emails.append(item)
with open('email-data2.pkl','r') as my_input:
    for item in pickleLoader(my_input):
        emails.append(item)
emails = [x for x in emails if x != None] #get rid of values that were missing 1 or more fields
email_subjects = map(lambda x: (x.subject).split(" "), emails)
word_dict={}
for index in range(len(emails)):
    for word in email_subjects[index]:
        word = word.lower()
        if word in word_dict:
            if emails[index] not in word_dict[word]:
                word_dict[word].append(emails[index])
        else:
            word_dict[word]=[emails[index]]
boring_words =['re:', 'your', 'to', 'for', '-','the', '', 'from', 'robin', 'and',\
'on', 'you', 'a', '[all_students]', 'pollak', 'in', 'of', 'is',\
'[student_information]', '[csmajors2018]', 'new', 'with', '[practice-scala]',\
'has', 'at','pm', 'this','been','2015', 'by', '[classof2018]','(#4)','60.3','(#5)','fwd:','have','up',\
'[what-is-a-dsl]','[project-ideas]','i','fa15','zoab','[instr','note]','(#10)','(#1)','[action']
word_dict = {key:value for key,value in word_dict.items() if key not in boring_words}
word_dict = {key:value for key,value in word_dict.items() if (len(key)>3 or key == 'cs' or key == 'pm')}
amount_dict = {keyword: len(value) for keyword,value in word_dict.items()}
top_keys = sorted(amount_dict, key=amount_dict.get, reverse=True)[:39]
word_dict = {key:value for key,value in word_dict.items() if (key in top_keys\
or key == "internship")}
amount_dict = {key:value for key,value in amount_dict.items() if (key in top_keys\
or key == "internship")}
with open('dictionary_data.pkl','wb') as output:
    pickle.dump(word_dict,output,-1)
    pickle.dump(amount_dict,output,-1)
