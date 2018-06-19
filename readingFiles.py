import json
import urllib2

def read8():
    destFile = open('A:\\python_exp\\csvIdResult.csv','a')
    fields = "Body, User Id, id, Title\n"
    destFile.write(fields)
    destFile.close()
    obj=open('A:\python_exp\ids.txt','r')
    for line in obj:
        line = line.replace('\n','')
        activity8(line)
    obj.close()
    
def activity8(line):
    url = 'https://jsonplaceholder.typicode.com/posts/'
    url = url + line
    json_data =  json.load(urllib2.urlopen(url))
    destFile = open('A:\\python_exp\\csvIdResult.csv','a')
    body = json_data['body']
    body =body.replace("\n"," ")
    uid = json_data['userId']
    id = json_data['id']
    title = json_data['title']
    row = str(body) +","+ str(uid) +","+str(id) +","+str(title)+"\n"
    destFile.write(row)
    destFile.close()
     
read8()