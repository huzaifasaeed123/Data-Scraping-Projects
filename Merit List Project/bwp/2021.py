from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time,sleep
from bs4 import BeautifulSoup
import urllib3,csv
from alive_progress import alive_bar


http = urllib3.PoolManager()


with open('exc.txt')as new:
   lines = [line.rstrip() for line in new]


def download_file(url,rnum):
    try:
        response = http.request('POST',url,fields={
	        "__LASTFOCUS": "",
	        "__EVENTTARGET": "",
	        "__EVENTARGUMENT": "",
	        "__VIEWSTATE": "7i3Gve2P1sR4kmlebDeWLoNgE9tKr2OakBKXtOFoSwuu8rF+eYyL66JuyuD52AJvDM5UozCTh6sO6eQ2iL+GuvufpIGg0zqiGmNI+blOjDBzLOSz6uTnHG7cof5A8jeRFdXp+QHI5TQqomYRZHY8nkjDjK/UdcC4TQCJ5PEYWtB7zD4Hkz57PitvOR8zaoyc/SXawE1ywM90TmdcqR26jiUivWuOzl1MCe00whSfH0QEl9hwLm3gOad/KeMnO6JrJE8rMmFwEMaHVp73Usa5i+t7xtYLtaICoaZJVnD9eozOvKiODmZysXaldyOgLfJa3aUZRHJw3PKOU/skCQfCFAX+jhF5S0m2D7ah3rwfwnxaXrwBcpeE0BHgV48Qm7MwSo0zt+9tmXXc+OkA3QtRGukSi50HuIg1lffMzn+HSFXUwT8q8NtCu7fo6l+E4MvHJnZ/rxp+gqKSZtvmbdzVcQ==",
	        "ctl00$ContentPlaceHolder1$txtHSSCPIRollNo": rnum,
	        "ctl00$ContentPlaceHolder1$btnHSSCAPI": "View+Result",
	        "ctl00$ContentPlaceHolder1$txtHSSCName": "",
	        "__VIEWSTATEGENERATOR": "23871942",
	        "__VIEWSTATEENCRYPTED": "",
	        "__EVENTVALIDATION": "S0wnKD2BfHQ1GCk7WfaN0LPuA935ky0njqeM2P4KBCU7cOFJz9xNw7n+u4Cgw0+NILsY7W7QVIjurG0lXsB3gi5B0zIv47Tm3BJoRCgLtF43/jPmmVXtKgy1TarddOI0VnggOKlcVQXH/1+OrzL15eyILSK8lX+IRt5Ge0eaqP0qGyNZTq7/s4S5uIWs2COvvGN5/e3Styttpqx14GzTEg=="})
        #print(response.data)
        soup = BeautifulSoup(response.data,'html.parser')


        #print(soup.text)
        if 'BIO' in soup.text:
            table = soup.find('table') #
            td_tags = table.select('td')

            #for (i, item) in enumerate(td_tags, start=0):
            #    print(i, item)

            name = (f'{td_tags[9].text}')
            fname = (f'{td_tags[11].text}')
            rn = int((f'{td_tags[5].text}'))

            #phy = int((f'{td_tags[72].text}'))
            #chem = int((f'{td_tags[81].text}'))
            #bio = int((f'{td_tags[90].text}'))

            #marks = bio+phy+chem
            marks = int((f'{td_tags[92].text}'))
            bar()
            row = [rn,name,fname,marks]
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

with alive_bar(520966-500001) as bar:
    with ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(300001,300005):
            sleep(0.01)
            processes.append(executor.submit(download_file, f'http://221.120.217.252/Applications/indexHSSC_PII.aspx',i))


for task in as_completed(processes):
    print(task.result())
    if type(task.result()) is not str:
        #print(task.result())
        with open('resultstotal2021.csv','a',newline='') as new:
            count +=1
            print(count)
            res_writer = csv.writer(new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            try:
                res_writer.writerow(task.result())
            except Exception as e:
                with open('exc1.txt','a')as ex:
                    ex.write(f'{task.result()}\n')
    else:
        with open('maths.txt','a')as fail:
            fail.write(f'{task.result()}\n')

print(f'Time taken: {time() - start}')