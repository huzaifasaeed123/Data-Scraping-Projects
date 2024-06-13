from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
import urllib3,csv

http = urllib3.PoolManager()


def download_file(url,rnum):
    try:
        response = http.request('POST',url,fields={
            "rollNo": rnum,

            "session": 2022,
        })
        soup = BeautifulSoup(response.data,'html.parser')
        
        #print(soup.text)
        if 'Student' in soup.text:
            name = soup.find(id='name').text
            rn = soup.find(id='cnic').text
            marks = soup.find(id='omarks').text
            #print(name,rn,fname)
            table = soup.find('table') # get desired table
            td_tags = table.select('td')

            #for (i, item) in enumerate(td_tags, start=0):
            #    print(i, item)
            #phy=int((f'{td_tags[29].text}'))
            #chem=int((f'{td_tags[35].text}'))
            #bio=int((f'{td_tags[41].text}'))
            #marks = soup.find(id='ContentPlaceHolder1_lblNotification').text
            #marks1 = phy+bio+chem
            row = [rn,name,marks]
            return row
        else:
            math = url[-6:]
            return math
    except:
        pass
    


start = time()

processes = []
count = 0

with ThreadPoolExecutor(max_workers=4) as executor:
    for i in range(3310267033648, 3310267033649):
        processes.append(executor.submit(download_file, f'https://www.pmc.gov.pk/Results/ResultsInfo?rollNo=3310267033648&session=2022',i))


for task in as_completed(processes):
    if type(task.result()) is not str:
        print(task.result())
        with open('pmc.csv','a',newline='') as new:
            count +=1
            print(count)4
            res_writer = csv.writer(new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #res_writer.writerow(task.result())
    else:
        with open('maths.txt','a')as fail:
            fail.write(f'{task.result()}\n')

print(f'Time taken: {time() - start}')