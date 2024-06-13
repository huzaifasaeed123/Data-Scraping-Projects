from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
import urllib3,csv
from alive_progress import alive_bar

http = urllib3.PoolManager()


#with open('rollnoabove950marks.txt')as new:
#    lines = [line.rstrip() for line in new]


def download_file(url,rnum):
    try:
        response = http.request('POST',url,fields={"year":"2020","class":"12","rno":rnum})
        soup = BeautifulSoup(response.data,'html.parser')


        #print(soup.text)
        if 'BIOLOGY' in soup.text:
            span = soup.find_all("span")
            rn =  span[1].text
            name =  span[3].text
            fname=  span[4].text

            table = soup.find('table') # get desired table
            td_tags = table.select('td')

            for (i, item) in enumerate(td_tags, start=1):
                print(i, item)

            phy=int((f'{td_tags[63].text}'))
            chem=int((f'{td_tags[74].text}'))
            bio=int((f'{td_tags[85].text}'))
            marks1 = phy+bio+chem
            marks = int((f'{td_tags[98].text}'))
            row = [rn,name,fname,marks,marks1]


            bar()
            return row
            
        else:
            bar()
            math = rnum
            return math
    except:
        pass
    


start = time()

processes = []
count = 0

with alive_bar(254774-10000) as bar:
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(100001, 254774):
            processes.append(executor.submit(download_file, f'http://www.bisegrw.edu.pk/result-card-matric.html',i))


for task in as_completed(processes):
    if type(task.result()) is not str:
        print(task.result())
        with open('results_2020(grw).csv','a',newline='') as new:
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