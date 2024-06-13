from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
import urllib3,csv
import requests
http = urllib3.PoolManager()


#with open('rollnoabove950marks.txt')as new:
#    lines = [line.rstrip() for line in new]
session = requests.Session()

def download_file(url,rnum):
    try:
        response = http.request('POST',url,fields={
	        "__LASTFOCUS": "",
	        "__EVENTTARGET": "",
	        "__EVENTARGUMENT": "",
	        "__VIEWSTATE": "/wEPDwUKLTQwNzY1NTc5NGQYAQUJdHh0Rm9ybU5vDw88KwAHAGRkGSu1ocIe/P1YRzJp8VpOgmK9cpjdOoCcsj0xn4Wsbg0=",
	        "__VIEWSTATEGENERATOR": "CA0B0334",
	        "rdlistCourse": "HSSC",
	        "txtFormNo": rnum,
	        "ddlExamType": "2",
	        "ddlExamYear": "2022",
	        "Button1": "View+Result"})
        print("Huzaifa")
        final_url=response.url
        #final_response=http.request('GET',final_url)
        #print(response.data)
        soup = BeautifulSoup(response.data,'html.parser')
        print(response.data)
        print(soup.text)
        name = soup.find("label",id="Name")
        name1=name.text
        #yrname=soup.select(id='Name')
        #print(yrname)
        print(name1)
        if 'Biology' in soup.text:
            name = soup.find("Student Name").text
            print(name+"Usama")
            print(" ")
            rn = soup.find(id='ContentPlaceHolder1_lblRollNoValue').text
            fname = soup.find(id='lblFatherName').text
            print(name)
            table = soup.find('table') # get desired table
            td_tags = table.select('td')
            print("Huzaifa2")

            for (i, item) in enumerate(td_tags, start=0):
                print(i, item)
                print("Huzaifa2")
            phy=int((f'{td_tags[29].text}'))
            chem=int((f'{td_tags[35].text}'))
            bio=int((f'{td_tags[41].text}'))
            print(phy+ "physics")
            marks = phy+bio+chem
            row = [rn,name,fname,marks]
            print(row)
            return row
        else:
            print("Huzaifanot match")
            math = rnum
            return math
    except:
        pass
    


start = time()

processes = []
count = 0

with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(522287,522288):
        processes.append(executor.submit(download_file, f'http://result.biselahore.com/',i))

# old http://result.biselahore.com/

for task in as_completed(processes):
    if type(task.result()) is not str:
        print(task.result())
        with open('results_202221.csv','a',newline='') as new:
            count +=1
            print(count)
            res_writer = csv.writer(new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            try:
                res_writer.writerow(task.result())
            except:
                pass
    else:
        with open('maths.txt','a')as fail:
            fail.write(f'{task.result()}\n')

print(f'Time taken: {time() - start}')