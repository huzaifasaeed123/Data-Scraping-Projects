from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time, sleep
import tkinter
from bs4 import BeautifulSoup
import urllib3, csv
from alive_progress import alive_bar
import tkinter as tk
from tkinter import filedialog

http = urllib3.PoolManager()


# print('Roll number file...\n')
# rnfile= filedialog.askopenfilename()
#
# with open(rnfile)as new:
#    lines = [line.rstrip() for line in new]

def download_file(url, rnum):
    try:
        response = http.request('POST', url, fields={
            "rno": rnum,
            "session": "cyNmMzIwdzRzZ2kxMjAyM3Ay", #cyNmMzE5dzRzZ2kxMjAyMnAy
            "appear_level": "cyNmMzIwdzRzZ3BhcnQy"})
        #print(response.data)
        soup = BeautifulSoup(response.data, 'html.parser')

        #print(soup.text)
        if 'Biology' in soup.text:
            table = soup.find('table')  #
            td_tags = table.select('td')

            # for (i, item) in enumerate(td_tags, start=0):
            #     print(i, item)

            name = (f'{td_tags[6].text}').replace("\n", "")
            fname = (f'{td_tags[8].text}').replace("\n", "")
            rn = int((f'{td_tags[4].text}'))

            phy = int((f'{td_tags[65].text}'))
            chem = int((f'{td_tags[74].text}'))
            bio = int((f'{td_tags[83].text}'))

            marks1 = bio + phy + chem
            marks = (f'{td_tags[87].text}')
            bar()
            print(name)
            row = [rn, name, fname, marks, marks1]
            return row
        else:
            bar()
            math = rnum
            return math
    except:
        bar()
        failed = f'failed {rnum}'
        return failed


start = time()

processes = []
count = 0

threadcount = int(input("Enter number of threads:\n"))

with alive_bar(540265 - 500001) as bar:
    with ThreadPoolExecutor(max_workers=threadcount) as executor:
        for i in range(500001, 540265):
            sleep(0.01)
            processes.append(executor.submit(download_file, f'https://web.bisemultan.edu.pk/ajax/res2.php', i))
#https://web.bisemultan.edu.pk/ajax/res2.php prev
for task in as_completed(processes):
    print(task.result())
    if type(task.result()) is not str:
        # print(task.result())
        with open('result2023.csv', 'a', newline='') as new:
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