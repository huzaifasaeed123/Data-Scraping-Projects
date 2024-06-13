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
	       
	        "rollNo": rnum,
	})
        #print(response.data)
        soup = BeautifulSoup(response.data,'html.parser')
        
       # print(soup.text)
        if 'BIOLOGY' in soup.text:
            # name = soup.find(id='lblNameValue').text
            # rn = soup.find(id='lblRollNoValue').text
            # fname = soup.find(id='lblFatherValue').text
            # marks = soup.find(id='lblNotification').text #lblNotification
            #print(name,rn,fname)
            table = soup.find_all('table') # get desired table
            table2=table[1]
            td_tags = table2.select('td')
            name=(f'{td_tags[4].text}')
            fname=(f'{td_tags[6].text}')
            rn=(f'{td_tags[2].text}')
            parts = rn.split(':')
            rn1 = int(parts[1].strip())
            marks=(f'{td_tags[8].text}')
            print(name,fname,rn1,marks)
            table3=table[3]
            td_tags2=table3.select('td')

            # #
            # for (i, item) in enumerate(td_tags2, start=0):
            #    print(i, item)
           
            bio1=int((f'{td_tags2[57].text}'))
            bio2=int((f'{td_tags2[62].text}'))
            bioP=int((f'{td_tags2[63].text}'))
            bio=bio1+bio2+bioP
            che1=int((f'{td_tags2[47].text}'))
            che2=int((f'{td_tags2[52].text}'))
            cheP=int((f'{td_tags2[53].text}'))
            che=che1+che2+cheP
            phy1=int((f'{td_tags2[37].text}'))
            phy2=int((f'{td_tags2[42].text}'))
            phy3=int((f'{td_tags2[43].text}'))
            phy=phy1+phy2+phy3
            print(bio)
            marks1 = phy+bio+che
            print(name,rn,fname,marks,marks1)
            row = [rn1,name,fname,marks,marks1]
            return row
        else:
            math = url[-6:]
            return math
    except:
        pass
    


start = time()

processes = []
count = 0
with alive_bar(579999-562001) as bar: #579982  562001
    with ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(576462,579999): #576462
            processes.append(executor.submit(download_file, f'https://portal.fbise.edu.pk/fbise-conduct/result/Result-link-hssc2.php?rollNo={i}',i))
#http://www.bisefsd.edu.pk/InterResults.aspx   old

for task in as_completed(processes):
    if type(task.result()) is not str:
        print(task.result())
        with open('results_2023federal.csv','a',newline='') as new:
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