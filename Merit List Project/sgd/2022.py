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
	        "ctl00$ScriptManager1": "ctl00$ContentPlaceHolder1$UpdatePanel2|ctl00$ContentPlaceHolder1$BtnShowResults",
	        "ctl00$ContentPlaceHolder1$DDLExam": "2",
	        "ctl00$ContentPlaceHolder1$DDLExamYear": "2023-1",
	        "ctl00$ContentPlaceHolder1$DDLExamSession2": "1",
	        "ctl00$ContentPlaceHolder1$RbtSearchType": "Search by Roll No.",
	        "ctl00$ContentPlaceHolder1$TxtSearchText": rnum,
	        "__EVENTTARGET": "",
	        "__EVENTARGUMENT": "",
	        "__LASTFOCUS": "",
	        "__VIEWSTATE": "/wEPDwUJMTc1MTQyOTY1D2QWAmYPZBYCAgEPZBYCAgMPZBYKAgEPZBYCZg9kFgYCAQ8QZGQWAQICZAIDDxAPFgYeCENzc0NsYXNzBQhERExTdHlsZR4EXyFTQgICHgdWaXNpYmxlZ2QQFRIMU0VMRUNUIFlFQVIuBDIwMjMEMjAyMgQyMDIxBDIwMjAEMjAxOQQyMDE4BDIwMTcEMjAxNgQyMDE1BDIwMTQEMjAxMwQyMDEyBDIwMTEEMjAxMAQyMDA5BDIwMDgEMjAwNxUSDFNFTEVDVCBZRUFSLgYyMDIzLTEGMjAyMi0yBjIwMjEtMgYyMDIwLTEGMjAxOS0yBjIwMTgtMgYyMDE3LTIGMjAxNi0yBjIwMTUtMgYyMDE0LTIGMjAxMy0yBjIwMTItMgYyMDExLTIGMjAxMC0yBjIwMDktMgYyMDA4LTIGMjAwNy0yFCsDEmdnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAgFkAgUPEA8WAh8CZ2QPFgECAhYBEGRkaBYBAgFkAgMPZBYCZg9kFgQCAQ8PFgIeBFRleHRlZGQCAw8QDxYCHwJnZGQWAWZkAgUPZBYCZg9kFgICAQ8PFgIfAmhkZAIHD2QWAmYPZBYIAgEPDxYEHwMFHVBsZWFzZSBXcml0ZSBZb3VyIFJvbGwgTm8gOi0gHwJnZGQCAw8PFgIfAmdkZAIFDw8WBB8CaB8DZWRkAgcPDxYCHwJnZGQCCw9kFgJmD2QWBAIBD2QWAgICD2QWAmYPZBYCAgMPZBYCZg9kFgJmD2QWAgIDDzwrABECARAWABYAFgAMFCsAAGQCAw88KwARAwAPFgIfAmhkARAWABYAFgAMFCsAAGQYAgUuY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRHcmRWaWV3SW5zdGl0dXRlQ29kZQ9nZAUjY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRHcmlkVmlldzEPZ2R8lCteJrejPJTuf8PR2f6Sfg+NMTYYdp4b4KVVaR7f8A==",
	        "__EVENTVALIDATION": "/wEdACH9dw8wcgdxAOeTbVbQOqpGStDmKLo2JPA2LKuSRZL7E2HYKEZZxLCYb/5dcpsezg0WWj5w9GW4p46PhhLl5lgZCbHdk2MYWN136RPPHqYi9W2Pm6eW96195mSAukOAmOCqV+1NHZzzStJhoU4ks33n96mE42nulLXmPGNq9hW18jXGywMJYXKMBYX03GkDbXUsPMBBqjdfXlSsdMjFQpndytQh1hcdMx/1AFwjYDTwPeIcqQmiaiw26Z4Xw8vRI23ffYcvHAjUhxi/iOnaSDCQhdGSPbzA9Y59Z5Hdkw2RDT9MzHDW/ilpXWh7QNbigIp2de4lsmJJqYq17RFgmaMWU6IdehNxZzWlavULMn1W9Dhx3H/asl3h8u2yo2SQ5tu4eTYs8dSHl55ffdV/sG+FXcvbd6+clkmytNxamjwtnxZA4MpiH0epQXrPgJ71sR4mhTdZwCQU7BVJX4ilO9f3o8QjUJSX/aarGvahYhG37TNnjpFtDGRnpvOnFRP1s8ha89Efhddelf6wjt8ZJof5QveklbLQnXAPUaB5KWxITdlhM42EIG2IpCFXCLhT0qiM60YvlhVQmXKpnBwOtddpr+/VWH9ulRqrNZe8nDxzX5kzywWZH7LN7kYC9AKKyHWCipTPszqHHn1PgQHqqIzy2ULbP/xalU1J560ruI4iS0wKCXI110TBKlzGJTMYDz2Ejw86IQKXdmhn4AC7GBjqkQaeO/6cYK55IPsul60cvQ==",
	        "__ASYNCPOST": "false",
	        "ctl00$ContentPlaceHolder1$BtnShowResults": "Show Result"})
        #print(response.status)
        soup = BeautifulSoup(response.data,'html.parser')


        #print(soup.text)
        if 'BIOLOGY' in soup.text:
            table = soup.findAll('table')[3]
            td_tags = table.select('td')
            
            # for (i, item) in enumerate(td_tags, start=0):
            #    print(i, item)
            rn = int(f'{td_tags[1].contents[1].text}'.replace("Roll No. ",''))
            name = (f'{td_tags[5].text}').replace("\n",'')
            fname = (f'{td_tags[7].text}').replace("\n",'')
            
            marks = ((f'{td_tags[72].text}'))
            
            marks = ''.join(filter(str.isdigit,marks))

            bio = int(soup.find(id='ContentPlaceHolder1_LblPaper5ObtainedMarksWithGrade').text.partition('= ')[2])
            phy = int(soup.find(id='ContentPlaceHolder1_LblPaper6ObtainedMarksWithGrade').text.partition('= ')[2])
            chem =int(soup.find(id='ContentPlaceHolder1_LblPaper7ObtainedMarksWithGrade').text.partition('= ')[2])
            #
            marks1 = bio+phy+chem
            bar()
            row = [rn,name,fname,marks,marks1]
            print(rn,name,fname,marks,marks1)
            return row
            
        else:
            bar()
            math = rnum
            return math
    except Exception as e:
        print(e)
        bar()
        failed = f'failed {rnum}'
        return rnum
    


start = time()

processes = []
count = 0

with alive_bar(414067-400001) as bar:
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(400001,414067):
            sleep(0.1)
            processes.append(executor.submit(download_file, f'https://www.bisesargodha.edu.pk/content/boardresult.aspx',i))


for task in as_completed(processes):
    #print(task.result())
    if type(task.result()) is not str:
        print(task.result())
        with open('result2023srg.csv','a',newline='') as new:
            count +=1
            #print(count)
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