from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time,sleep
from bs4 import BeautifulSoup
import urllib3,csv
from alive_progress import alive_bar


http = urllib3.PoolManager()


#with open('rn950.txt')as new:
#    lines = [line.rstrip() for line in new]


def download_file(url,rnum):
    try:
        response = http.request('POST',url,fields={"RNO": rnum})
        #print(response.data)
        soup = BeautifulSoup(response.data,'html.parser')


        #print(soup.text)
        if 'BIOLOGY' in soup.text:
            table = soup.findAll('table')
            table1 = table[1]
            table2 = table[2]
            td_tags1 = table1.select('td')
            td_tags2 = table2.select('td')

            # print(table)
            # print(td_tags1)
            # for (i, item) in enumerate(td_tags2, start=0):
            #     print(i, item)

            rn = int(f'{td_tags1[1].text}')
            name = (f'{td_tags1[5].text}')
            fname = (f'{td_tags1[9].text}')
            
            print(rn,name,fname)
            phy = int((f'{td_tags2[36].text}'))
            chem = int((f'{td_tags2[42].text}'))
            bio = int((f'{td_tags2[48].text}'))
#
            marks1 = bio+phy+chem
            marks = int((f'{td_tags2[54].text}'))
            bar()
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

with alive_bar(429816-400001) as bar:
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(400001,429816):
            sleep(0.1)
            processes.append(executor.submit(download_file, f'https://www.bisedgkhan.edu.pk/RESULT_IINT_200023/index.php',i))
#https://www.bisedgkhan.edu.pk/RESULT_INT20020/index.php      prev

for task in as_completed(processes):
    print(task.result())
    if type(task.result()) is not str:
        #print(task.result())
        with open('result2003latest.csv','a',newline='') as new:
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