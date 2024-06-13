from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
import urllib3, csv
from alive_progress import alive_bar
import requests
http = urllib3.PoolManager()

with open('sample.txt')as new:
    lines = [line.rstrip() for line in new]


def download_file(url, rnum):
    try:
        response = http.request('POST', url, fields={
        "ScriptManager1": "UpdatePanel2|btnFetchMe",
        "__LASTFOCUS" : "",
        "__EVENTTARGET":"" ,
        "__EVENTARGUMENT":"" ,
        "__VIEWSTATE": "/wEPDwUJMjUwMDE2ODEyD2QWAgIBD2QWBAIHDxYCHglpbm5lcmh0bWwFNyBXZWxjb21lIHRvIFJlQ2hlY2tpbmcgRm9ybSBmb3IgSFNTQyBGSVJTVCBBTk5VQUwsIDIwMjNkAgkPZBYCZg9kFhICAQ8WAh8AZWQCBQ8PFgIeBFRleHRlZGQCCQ8PFgQfAWUeB0VuYWJsZWRoZGQCCw8PFgQfAWUfAmhkZAINDw8WBB8BZR8CaGRkAg8PDxYEHwFlHwJoZGQCEQ8PFgQfAWUfAmhkZAITDw8WBB8BZR8CaGRkAhkPPCsAEQMADxYGHgtfIURhdGFCb3VuZGceC18hSXRlbUNvdW50Zh4HVmlzaWJsZWhkARAWABYAFgAMFCsAAGQYAwUVR3JkU3R1ZGVudF9BdHRlbmRhbmNlDzwrAAwBCGZkBQl0eHRNb2JpbGUPDzwrAAcAZGQFCXR4dFJvbGxObw8PPCsABwBkZHjtnsrW7ntWASYA0PpJEzieo77VJI2/kSY9n3jcdK3D",
        "__VIEWSTATEGENERATOR": "CA0B0334",
        "__EVENTVALIDATION": "/wEdAA4XCs54mP2vpHMoOQK1Ihf/OuV4VHc25VRXgCLOw3s9xBDuqC2nksUG5vImDKQbXi5YH+3xex89uEq1oPEFIP0veXGI+rAYtYOkXe9IjqbQOi+z8L63awvFhCnC71KXJFEjoIoajkzPB1FzhqJPvH20BMh4m/z+RcOqD3zZj1lZiFP+w13A9dO/NG8yEfMI+MyDiE8aBy/Tbqa0Twn7o/VVlFSloPIT02vC5AD2R5t+TBXE3dkwa1cRACVa3MHp4Buaj50dSVxh1rHEj9T9L1ldlliAPKY+KvRmniYVjNuQiCPgr4iACgyngFZ51FQ3KWr1nkjoday4Hm4goCrAxg77",
        "hdSubjectAmount": "1300",
        "hdProcessingAmount": "0",
        "txtRollNo": rnum,
        "txtStudentName":"" ,
        "txtStudentFatherName": "",
        "txtStudentSubejctGroup": "",
        "txtStudentExamGroup": "",
        "txtExamName": "",
        "txtExamYear": "",
        "txtMobile": "03",
        "txtAddress": "",
        "__ASYNCPOST": "false",
        "btnFetchMe": "Get My Info",
                })
        print(response.data)
        soup = BeautifulSoup(response.data, 'html.parser')
        input_element1 = soup.find(id="txtStudentName")
        name=input_element1.get('value')
        input_element2 = soup.find(id="txtStudentFatherName")
        fname=input_element2.get('value')
        
        input_element3 = soup.find(id="txtStudentSubejctGroup")
        group=input_element3.get('value')
        input_element4 = soup.find(id="txtRollNo")
        Roll_NUm=input_element4.get('value')
        print(Roll_NUm,name,fname,group)
        row=[Roll_NUm,name,fname,group]
        return row
    except:
        pass


start = time()

processes = []
count = 0

with alive_bar(100000 - 10000) as bar:
    with ThreadPoolExecutor(max_workers=3) as executor:
        for i in lines:
            print(i)
            processes.append(executor.submit(download_file, f'https://rechecking.biserawalpindi.edu.pk/', i))
#https://result.bisegrw.edu.pk/result-card.html
# http://www.bisegrw.edu.pk/result-card-matric.html  old
for task in as_completed(processes):
    if type(task.result()) is not str:
        print(task.result())
        with open('FinalRwpWithFname2023.csv', 'a', newline='') as new:
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