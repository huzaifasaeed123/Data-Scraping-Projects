from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
import urllib3, csv
from alive_progress import alive_bar

http = urllib3.PoolManager()


# with open('rollnoabove950marks.txt')as new:
#    lines = [line.rstrip() for line in new]


def download_file(url, rnum):
    try:
        response = http.request('POST', url, fields={"type": "5", 
                "rno": rnum,
                "class": "12",
                "year": "2023",
                "check": "2"
                })
        soup = BeautifulSoup(response.data, 'html.parser')

        #print(soup.text)
        if 'BIOLOGY' in soup.text:
            span = soup.find_all("b")
            rn = (f'{span[0].text}')
            name = (f'{span[2].text}')
            fname = (f'{span[3].text}')
            marks = (f'{span[6].text}')
           # print(rn)
            #print("Huzads"+rn,name,fname,marks)

            table = soup.find('table')  # get desired table
            td_tags = table.select('td')

            # for (i, item) in enumerate(td_tags, start=1):
            #     print(i, item)

            phy = ((f'{td_tags[63].text}'))
            chem = ((f'{td_tags[74].text}'))
            bio = ((f'{td_tags[85].text}'))
            marks1 = int(phy) + int(bio) + int(chem)
            row = [rn, name, fname,marks,marks1]
            print(rn,name,fname,marks,marks1)
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

with alive_bar(142820 - 101535) as bar:
    with ThreadPoolExecutor(max_workers=3) as executor:
        for i in range(101535, 142820):
            processes.append(executor.submit(download_file, f'https://result.bisegrw.edu.pk/result-card.html', i))
#https://result.bisegrw.edu.pk/result-card.html
# http://www.bisegrw.edu.pk/result-card-matric.html  old
for task in as_completed(processes):
    if type(task.result()) is not str:
        print(task.result())
        with open('resultgrw2023.csv', 'a', newline='') as new:
            count += 1
            print(count)
            res_writer = csv.writer(new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            try:
                res_writer.writerow(task.result())
            except Exception as e:
                with open('exc.txt', 'a') as ex:
                    ex.write(f'{e}\n')
    else:
        with open('maths.txt', 'a') as fail:
            fail.write(f'{task.result()}\n')

print(f'Time taken: {time() - start}')