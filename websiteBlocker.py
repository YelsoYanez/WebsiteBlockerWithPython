import time
from datetime import datetime as dt
'''This program will block url written in the python list, just at a url an python will block
the url by telling the hosts manager to block the url, also the program writes the url to block and once time go by,
the code will remove the url from host file to be able to acces the url again.
'''
hosts_temp="hosts"
host_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 12) < \
    dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 13):
        print("Working hours....")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
        print("Fun Hours.....")
    time.sleep(5)
