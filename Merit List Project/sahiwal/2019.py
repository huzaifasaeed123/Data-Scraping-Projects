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
        response = http.request('POST',url,fields={
	        "class": "3",
	        "year": "2019",
	        "sess": "1",
	        "rno": rnum,
	        "commit": "GET+RESULT"})
        #print(response.data)
        soup = BeautifulSoup(response.data,'html.parser')


        #print(soup.text)
        if 'BIOLOGY' in soup.text:
            table = soup.findAll('table')[2] #
            td_tags = table.select('td')

            #print(table)
           # for (i, item) in enumerate(td_tags, start=0):
               # print(i, item)

            rn = rnum
            name = (f'{td_tags[11].text}').replace("\n",'')
            fname = (f'{td_tags[13].text}').replace("\n",'')
            
            #print(name)
            urdu = int((f'{td_tags[27].text}'))
            eng = int((f'{td_tags[34].text}'))
            isl = int((f'{td_tags[41].text}'))
            phy = int((f'{td_tags[48].text}'))
            chem = int((f'{td_tags[55].text}'))
            bio = int((f'{td_tags[62].text}'))
            phy1= int(phy+phy+15+(round(phy*15/85)))
            chem1 = int(chem + chem + 15 + (round(chem * 15 / 85)))
            bio1 = int(bio + bio + 15 + (round(bio * 15 / 85)))
            elec = bio1+phy1+chem1
            marks=urdu+urdu+eng+eng+isl+isl+phy1+chem1+bio1
            markspi = int((f'{td_tags[69].text}'))
            totalmarks=marks+ ( round(3/100*markspi))
            bar()
            row = [rn,name,fname,totalmarks,elec]
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

with alive_bar(380001-300001) as bar:
    with ThreadPoolExecutor(max_workers=40) as executor:
        for i in range(400002,460397):
            sleep(0.1)
            processes.append(executor.submit(download_file, f'https://www.bisesahiwal.edu.pk/allresult/route.php',i))


for task in as_completed(processes):
    print(task.result())
    if type(task.result()) is not str:
        #print(task.result())
        with open('results_2020(Sahiwal).csv','a',newline='') as new:
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