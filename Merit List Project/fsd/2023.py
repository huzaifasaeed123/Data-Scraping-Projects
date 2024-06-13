from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
import urllib3,csv
from alive_progress import alive_bar
http = urllib3.PoolManager()


#with open('rollnoabove950marks.txt')as new:
#   lines = [line.rstrip() for line in new]


def download_file(url,rnum):
    try:
        response = http.request('POST',url,fields={
	       
	        "RollNo": rnum,
	})
        #print(response.data)
        soup = BeautifulSoup(response.data,'html.parser')
        
       # print(soup.text)
        if 'BIOLOGY' in soup.text:
            name = soup.find(id='lblNameValue').text
            rn = soup.find(id='lblRollNoValue').text
            fname = soup.find(id='lblFatherValue').text
            marks = soup.find(id='lblNotification').text #lblNotification
            #print(name,rn,fname)
            table = soup.find('table') # get desired table
            td_tags = table.select('td')
            #
            # for (i, item) in enumerate(td_tags, start=0):
            #    print(i, item)
            phy=int((f'{td_tags[39].text}'))
            chem=int((f'{td_tags[47].text}'))
            bio=int((f'{td_tags[55].text}'))
            marks1 = phy+bio+chem
            print(name,rn,fname,marks,marks1)
            row = [rn,name,fname,marks,marks1]
            return row
        else:
            math = url[-6:]
            return math
    except:
        pass
    


start = time()

processes = []
count = 0
with alive_bar(438203-400000) as bar:
    with ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(400000,438203):
            processes.append(executor.submit(download_file, f'http://iresult.bisefsd.edu.pk/ResultDetails.aspx?RollNo={i}',i))
#http://www.bisefsd.edu.pk/InterResults.aspx   old

for task in as_completed(processes):
    if type(task.result()) is not str:
        print(task.result())
        with open('results_2023Latest.csv','a',newline='') as new:
            count +=1
            print(count)
            res_writer = csv.writer(new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            try:
                res_writer.writerow(task.result())
            except Exception as e:
                pass
    else:
        with open('maths.txt','a')as fail:
            fail.write(f'{task.result()}\n')

print(f'Time taken: {time() - start}')