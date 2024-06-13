from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time, sleep
from bs4 import BeautifulSoup
import urllib3, csv
from alive_progress import alive_bar

http = urllib3.PoolManager()


# with open('rn950.txt')as new:
#    lines = [line.rstrip() for line in new]


def download_file(url, rnum):
    try:
        response = http.request('POST', url, fields={
            "ctl00$ScriptManager1": "ctl00$ContentPlaceHolder1$UpdatePanel2|ctl00$ContentPlaceHolder1$BtnShowResults",
            "ctl00$ContentPlaceHolder1$DDLExam": "2",
            "ctl00$ContentPlaceHolder1$DDLExamYear": "2021-1",
            "ctl00$ContentPlaceHolder1$DDLExamSession2": "1",
            "ctl00$ContentPlaceHolder1$RbtSearchType": "Search by Roll No.",
            "ctl00$ContentPlaceHolder1$TxtSearchText": rnum,
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            "__LASTFOCUS": "",
            "__VIEWSTATE": "/wEPDwULLTE0NjM5OTQ1NzIPZBYCZg9kFgICAQ9kFgICAw9kFgoCAQ9kFgJmD2QWBgIBDxBkZBYBAgJkAgMPEA8WBh4IQ3NzQ2xhc3MFCERETFN0eWxlHgRfIVNCAgIeB1Zpc2libGVnZBAVEQxTRUxFQ1QgWUVBUi4EMjAyMgQyMDIxBDIwMjAEMjAxOQQyMDE4BDIwMTcEMjAxNgQyMDE1BDIwMTQEMjAxMwQyMDEyBDIwMTEEMjAxMAQyMDA5BDIwMDgEMjAwNxURDFNFTEVDVCBZRUFSLgYyMDIyLTEGMjAyMS0yBjIwMjAtMQYyMDE5LTIGMjAxOC0yBjIwMTctMgYyMDE2LTIGMjAxNS0yBjIwMTQtMgYyMDEzLTIGMjAxMi0yBjIwMTEtMgYyMDEwLTIGMjAwOS0yBjIwMDgtMgYyMDA3LTIUKwMRZ2dnZ2dnZ2dnZ2dnZ2dnZ2cWAQICZAIFDxAPFgIfAmdkDxYBAgIWARBkZGcWAQIBZAIDD2QWAmYPZBYEAgEPDxYCHgRUZXh0ZWRkAgMPEA8WAh8CZ2RkFgFmZAIFD2QWAmYPZBYCAgEPDxYCHwJoZGQCBw9kFgJmD2QWBgIBDw8WAh8CZ2RkAgMPDxYCHwJnZGQCBw8PFgIfAmdkZAILD2QWAmYPZBYEAgEPFgIfAmcWBAIBD2QWAmYPZBYCAgEPDxYCHwMFJElOVEVSTUVESUFURSBBTk5VQUwgRVhBTUlOQVRJT04gMjAyMWRkAgIPZBYCZg9kFgYCAw9kFgJmD2QWAmYPZBYEAgEPDxYCHwNlZGQCAw88KwARAgEQFgAWABYADBQrAABkAgUPZBYCZg9kFgICAQ9kFgICAQ8PFgIfAwUBMGRkAgcPFgIfAmcWGmYPZBYEAgEPZBYCAgEPDxYCHwMFBjQwMjgyN2RkAgMPZBYCAgEPDxYCHwMFDzM4MzAyLTg3MDMzMDYtNGRkAgEPZBYCAgEPZBYCAgEPDxYCHwMFCklRUkEgQUhNQURkZAICD2QWAgIBD2QWAgIBDw8WAh8DBQpBSE1BRCBLSEFOZGQCAw9kFgICAQ9kFgICAQ8PFgIfAwUjU3VwZXJpb3IgQ29sbGVnZSBmb3IgV29tZW4gTWlhbndhbGlkZAIGD2QWDGYPZBYCAgEPDxYCHwMFEUlTTEFNSUMgRURVQ0FUSU9OZGQCAQ9kFgICAQ8PFgIfAwUCNTBkZAICD2QWAgIBDw8WAh8DBQI0N2RkAgMPZBYCAgEPDxYCHwMFBTk0LjAwZGQCBA9kFgICAQ8PFgIfAwUCQStkZAIFD2QWAgIBDw8WAh8DBQRQQVNTZGQCBw9kFgxmD2QWAgIBDw8WAh8DBRBQQUtJU1RBTiBTVFVESUVTZGQCAQ9kFgICAQ8PFgIfAwUCNTBkZAICD2QWAgIBDw8WAh8DBQI0N2RkAgMPZBYCAgEPDxYCHwMF",
            "__EVENTVALIDATION": "wb4Vdy9t3r5yWSbK03FqaPC2fFkDgymIfR6lBes+AnvWxHiaFN1nAJBTsFUlfiKU71/ejxCNQlJf9pqsa9qFiEbftM2eOkW0MZGem86cVE/WzyFrz0R+F116V/rCO3xkmh/lC96SVstCdcA9RoHkpbEhN2WEzjYQgbYikIVcIuFPSqKcQ3rokLlxCJPA8Y5Bnm3aM60YvlhVQmXKpnBwOtddpr+/VWH9ulRqrNZe8nDxzX5kzywWZH7LN7kYC9AKKyHWCipTPszqHHn1PgQHqqIzy2ULbP/xalU1J560ruI4iS0wKCXI110TBKlzGJTMYDz0mwKrWU8aCHdeob6iETFVbPXNR5YHZqt/ohw05s1MFJw==",
            "__ASYNCPOST": "false",
            "ctl00$ContentPlaceHolder1$BtnShowResults": "Show Result"})
        # print(response.status)
        soup = BeautifulSoup(response.data, 'html.parser')

        # print(soup.text)
        if 'BIOLOGY' in soup.text:
            table = soup.findAll('table')[3]
            td_tags = table.select('td')

            # for (i, item) in enumerate(td_tags, start=0):
            #    print(i, item)
            rn = int(f'{td_tags[1].contents[1].text}'.replace("Roll No. ", ''))
            name = (f'{td_tags[5].text}').replace("\n", '')
            fname = (f'{td_tags[7].text}').replace("\n", '')

            marks = ((f'{td_tags[66].text}'))

            marks = ''.join(filter(str.isdigit, marks))

            bio = int(soup.find(id='LblMarks5').text.partition('= ')[2])
            phy = int(soup.find(id='LblMarks6').text.partition('= ')[2])
            chem = int(soup.find(id='LblMarks7').text.partition('= ')[2])
            #
            marks1 = bio + phy + chem
            bar()
            row = [rn, name, fname, marks, marks1]
            print(rn)
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

with alive_bar(459012 - 400001) as bar:
    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(402827, 402829):
            sleep(0.1)
            processes.append(
                executor.submit(download_file, f'https://www.bisesargodha.edu.pk/content/boardresult.aspx', i))

for task in as_completed(processes):
    # print(task.result())
    if type(task.result()) is not str:
        print(task.result())
        with open('results_2022.csv', 'a', newline='') as new:
            count += 1
            # print(count)
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