from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
import urllib3, csv

http = urllib3.PoolManager()


# with open('rollnoabove950marks.txt')as new:
#   lines = [line.rstrip() for line in new]


def download_file(url, rnum):
    try:
        response = http.request('POST', url, fields={

            "rollNo": rnum,

            "session":2022,
        })
            # print(response.data)
                soup: BeautifulSoup = BeautifulSoup(response.data, 'html.parser')

        # print(soup.text)
        if 'Student' in soup.text:
            name = soup.find(id='name').text
        rn = soup.find(id='cnic').text
        marks = soup.find(id='omarks').text
                # print(name,rn,fname)
                # table = soup.find('table') # get desired table
                # td_tags = table.select('td')
                #

        row = [rn, name, marks]
        return row
        else:
        math = url[-6:]
        return math

except:
pass

start = time()

processes = []
count = 0

with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(3310267033647, 3310267033649):
        processes.append(executor.submit(download_file, f'https://www.pmc.gov.pk/Results/MDCAT2022', i))

for task in as_completed(processes):
    if type(task.result()) is not str:
        print(task.result())
        with open('pmc.csv', 'a', newline='') as new:
            count += 1
            print(count)
            res_writer = csv.writer(new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            try:
                res_writer.writerow(task.result())
            except Exception as e:
                pass
    else:
        with open('maths.txt', 'a') as fail:
            fail.write(f'{task.result()}\n')

print(f'Time taken: {time() - start}')