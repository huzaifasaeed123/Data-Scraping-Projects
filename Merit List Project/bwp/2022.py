from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time,sleep
from bs4 import BeautifulSoup
import urllib3,csv
from alive_progress import alive_bar


http = urllib3.PoolManager()


# with open('exc.txt')as new:
#    lines = [line.rstrip() for line in new]


def download_file(url,rnum):
    try:
        response = http.request('POST',url,fields={
	        "__LASTFOCUS": "", 
	        "__EVENTTARGET": "",
	        "__EVENTARGUMENT": "",
	        "__VIEWSTATE": "qnkhP9mRVLq9dKkE7tsho2JRnpWpYH3ShtH+BZLiF0QdKMua9uQdBIlNW+iGON+Kbj0Bd2QssK9B54OgaF3FxcLApg1o38DTJ7JXCoZxZEm21T0rCMAYFkRcWcDTb2XV53R8OpAbwLWiotUe3ekYZQCxJEoSBBPUyPf0F5kGhJhPGmW1O+4SyC/fuf2x3RIk3BNOuYDqWcK59lBr77aN5AW9FpuRtxqE5Q5kUQRQOzk1ZQpu68OHSjaLVwRjRufYf6jesQuSfjK8270zYAYIg5IOeoTwPETREl2lfzHVxR1B0ScQaJ4FPB2gihdI4e0EFNcsBcy0tEZPcJ6Ve/pW36VBB6tFiCuFHlgge0DeDcw27J+STVmk+L/zcbv7tq5yhMgJUwRtHbESUiSFfN3sGipLveHcYdiVOlz+L/sPNJ8=",
            "ctl00$ContentPlaceHolder1$txtHSSCPIRollNo": rnum,
            "ctl00$ContentPlaceHolder1$btnHSSCAPI": "View Result",
            "ctl00$ContentPlaceHolder1$txtHSSCName": "",
             "__VIEWSTATEGENERATOR": "23871942",
            "__VIEWSTATEENCRYPTED": "",
	       	"__EVENTVALIDATION": "dAb0Nvs9keaId9kEYX+R1seFvkRobKJFkVrE0ar8njEXvqmy+cR5gTY9HAsyvOS/3Kz+02A/sR4xPLFGBAQultPJCR5b6Y6o2HY+Ta/ZiVmtvgMThNjR61Dvy1pveHlTerBF1VvgkvRSil6+pxxFsy51jKFWIGSmBlmPRcHEUy5sbll+ICoVd4WWYFBQUrFYBouk0xUhtPE8tGH1ZbxVwg=="})
        #print("Huzaifa")
        #print(response.data)
        soup = BeautifulSoup(response.data,'html.parser')


       # print(soup.text)
        if 'BIO' in soup.text:
            table = soup.find('table') #
            td_tags = table.select('td')

            # for (i, item) in enumerate(td_tags, start=0):
            #    print(i, item)

            name = (f'{td_tags[9].text}')
            fname = (f'{td_tags[11].text}')
            rn = int((f'{td_tags[5].text}'))
            phy = int((f'{td_tags[66].text}'))
            chem = int((f'{td_tags[74].text}'))
            bio = int((f'{td_tags[82].text}'))

            marks2 = bio+phy+chem
            marks = int((f'{td_tags[84].text}'))
            bar()
            print(rn,name,fname,marks,marks2)
            row = [rn,name,fname,marks,marks2]
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

with alive_bar(639328-500000) as bar:
    with ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(500000,639328):
            sleep(0.01)
            processes.append(executor.submit(download_file, f'http://221.120.217.252/Applications/indexHSSC_PII.aspx',i))


for task in as_completed(processes):
    print(task.result())
    if type(task.result()) is not str:
        #print(task.result())
        with open('result2023bwp.csv','a',newline='') as new:
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