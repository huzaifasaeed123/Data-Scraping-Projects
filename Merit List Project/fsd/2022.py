from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
import urllib3,csv

http = urllib3.PoolManager()


#with open('rollnoabove950marks.txt')as new:
#   lines = [line.rstrip() for line in new]


def download_file(url,rnum):
    try:
        response = http.request('POST',url,fields={
	        "__LASTFOCUS": "",
	        "__EVENTTARGET": "",
	        "__EVENTARGUMENT": "",
	        "__VIEWSTATE": "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",
	        "ctl00$ContentPlaceHolder1$ddlExam": "68",
	        "ctl00$ContentPlaceHolder1$txtRollNo": rnum,
	        "ctl00$ContentPlaceHolder1$btnResult": "+Get+Result",
	        "__VIEWSTATEGENERATOR": "B4A6998F",
	        "__EVENTVALIDATION": "Pxyw6iFMqNpyaR74kCEqgTxZRxZ5jUDYCTcWv1E3dcObzw14RiC9NRVmcfnM0mxKMWSLw9chNH41v0iRZzH+IfdtguUcsNACABxUKjZbJVovHgTTqckTMG8sSq4dIb9607iOcVuePnz2ZtpGuN9cwraPWeirBwadGHQLCtArLDe5g0hCwWl7e302JrG2VsIqKj9Tszf70VwfvmFeiwCtipKBeiRLWsFZL9ToiiA1gtkft7Z4lMLLMxxsYVZmmSU7BPMZ/s9xmFqjuJ+Kd9VsT0E7VD8vRStPd1pZ2R04U29uOEkgVZvCWhKQZL2kYNC7ak24PXDHmTnCBEq8CCtSpkG0U0rQW+Rw6pQSNs07IuV2o+jB7GDHMOpRitVlBXZw0H6QVd34/Gi5s42/94wbU9gZQ/wTi0axbFs7p2EhvapKrAMW0CVNxooUf1yE2ZLmRmSBgHw64jbqR49l7024cjkL0vMSDcnCwm63R1J8VzSYvFsByhVVvf6JMcKOK5qrosxj6aVQsxngfgGFcpvp33kLjl0Fsg7FBYXNMAt224g="})
        #print(response.data)
        soup = BeautifulSoup(response.data,'html.parser')
        
        #print(soup.text)
        if 'BIOLOGY' in soup.text:
            name = soup.find(id='ContentPlaceHolder1_lblNameValue').text
            rn = soup.find(id='ContentPlaceHolder1_lblRollNoValue').text
            fname = soup.find(id='ContentPlaceHolder1_lblFatherValue').text
            marks = soup.find(id='ContentPlaceHolder1_lblNotification').text
            #print(name,rn,fname)
            table = soup.find('table') # get desired table
            td_tags = table.select('td')
            #
            #for (i, item) in enumerate(td_tags, start=0):
            #    print(i, item)
            phy=int((f'{td_tags[29].text}'))
            chem=int((f'{td_tags[35].text}'))
            bio=int((f'{td_tags[41].text}'))
            marks1 = phy+bio+chem
            row = [rn,name,fname,marks,marks1]
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
    for i in range(401065,401066):
        processes.append(executor.submit(download_file, f'http://www.bisefsd.edu.pk/InterResults.aspx',i))


for task in as_completed(processes):
    if type(task.result()) is not str:
        print(task.result())
        with open('results_2022.csv','a',newline='') as new:
            count +=1
            print(count)
            res_writer = csv.writer(new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            try:
                res_writer.writerow(task.result())
            except Exception as e:
                pass
    else:
        with open('maths.txt','a')as fail:
            fail.write(f'{task.result()}\n')

print(f'Time taken: {time() - start}')