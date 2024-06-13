from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
import urllib3,csv

http = urllib3.PoolManager()


#with open('rollnoabove950marks.txt')as new:
#    lines = [line.rstrip() for line in new]


def download_file(url,rnum):
    try:
        response = http.request('POST',url,fields={
	        "student_rno": rnum,
	        "submit": "Get Result"
	        })
        soup = BeautifulSoup(response.data,'html.parser')
        # print(soup.text)
        if 'BIOLOGY' in soup.text:
            # print("HuzaifaW")
            
            table = soup.find('table') # get desired table
            td_tags = table.select('td')

            print("Huzaifa2")
            for (i, item) in enumerate(td_tags, start=0):
                print(i, item)
            phy=int((f'{td_tags[67].text}'))
            chem=int((f'{td_tags[76].text}'))
            bio=int((f'{td_tags[85].text}'))
            name=(f'{td_tags[8].text}')
            fname=(f'{td_tags[11].text}')
            

            marks1=int((f'{td_tags[103].text}'))
            marks = phy+bio+chem
            board="Bise Lahore 2023"
            
            
            row = [board,rnum,name,fname,marks1,marks]
            #550056
            return row
        else:
            math = rnum
            return math
    except:
        pass
    


start = time()

processes = []
count = 0

with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(500001,550099):
        processes.append(executor.submit(download_file, f'https://www.biselahore.com/Res1stA23_12th.php',i))


for task in as_completed(processes):
    if type(task.result()) is not str:
        print(task.result())
        with open('Result2023lahore.csv','a',newline='') as new:
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