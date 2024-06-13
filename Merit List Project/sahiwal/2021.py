from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time,sleep


from bs4 import BeautifulSoup
import urllib3,csv
from alive_progress import alive_bar


http = urllib3.PoolManager()


#with open('rn950.txt')as new:
   # lines = [line.rstrip() for line in new]


def download_file(url,rnum):
    try:
        response = http.request('POST',url,fields={
	        "class": "4",
	        "year": "2020",
	        "sess": "1",
	        "rno": rnum,
	        "commit": "GET+RESULT"})
        #print(response.data)
        soup = BeautifulSoup(response.data,'html.parser')


        #print(soup.text)
        if 'BIOLOGY' in soup.text:
            table = soup.findAll('table')[2] #
            td_tags = table.select('td')

            print(table)
            for (i, item) in enumerate(td_tags, start=0):
                print(i, item)

            rn = int(f'{td_tags[4].contents[1].text}'.replace("Roll No. ",''))
            name = (f'{td_tags[8].text}').replace("\n",'')
            fname = (f'{td_tags[10].text}').replace("\n",'')
            
            #print(name)
            phy = int((f'{td_tags[80].text}'))
            chem = int((f'{td_tags[91].text}'))
            bio = int((f'{td_tags[102].text}'))

            marks1 = bio+phy+chem
            bar()
            marks = int((f'{td_tags[120].text}'))
            row = [rn,name,fname,marks,marks1]
            return row
        else:
            bar()
            math = rnum
            return math
    except:
        bar()
        failed = f'failed {rnum}'
        return rnum
    


start = time()

processes = []
count = 0

with alive_bar(370001-300001) as bar:
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(100001,100002):
            sleep(0.1)
            processes.append(executor.submit(download_file, f'https://www.bisesahiwal.edu.pk/allresult/route.php',i))


for task in as_completed(processes):
    print(task.result())
    if type(task.result()) is not str:
        #print(task.result())
        with open('sahiwal-2020.csv','a',newline='') as new:
            count +=1
            print(count)
            res_writer = csv.writer(new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            try:
                res_writer.writerow(task.result())
            except Exception as e:
                with open('exc.txt','a')as ex:
                    ex.write(f'{e}\n')
    else:
        with open('maths.txt','a')as fail:
            fail.write(f'{task.result()}\n')

print(f'Time taken: {time() - start}')