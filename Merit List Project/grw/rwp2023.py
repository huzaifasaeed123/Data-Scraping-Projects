from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
import urllib3, csv
from alive_progress import alive_bar
import requests
http = urllib3.PoolManager()


# with open('rollnoabove950marks.txt')as new:
#    lines = [line.rstrip() for line in new]
# session = requests.Session()
# session.cookies.update({'ASP.NET_SessionId': 'nsex4mh3pnviutnketrke01d'})
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
# }

def download_file(url, rnum):
    try:
        response = http.request('POST', url, fields={
        "__VIEWSTATE": "/wEPDwULLTEzMDIzNTU0NzNkZMm7w/LHXTGAXTOab+81vHOsS4wTT06movGRvMaG+J4n",
        "__VIEWSTATEGENERATOR": "CA0B0334",
        "__EVENTVALIDATION": "/wEdABndGJ9mhJWUddQ/Jt+IwTwqlPoxp0F+T8HoOcRNzMcdj5fcod9lwYztBZPfH6+W5Bc30/WM89sveaK06aLhHYMNBqLoyFeYCV79e/CJ/SSk22qfpArKNM7TRdZPpNPd/v5/ZlavtzqnSOtk3AIA7L44cmEZsVjbzqIGsM/h/iV37LOepqOgtAZMM/978JZsahd6iidFgfyIiGiUvhTXUoLUClbIzuqOUiEmKNPuzZOKq/l8oxJixkaoZIUrx5wUcxR2Zq54J6bK8kPMiTkvnCpUhEL33EeRY71t6yum47sP4zCtVkc6+h/mO/hesAMBZYJt9lQ7vENMTIefGSeaRO3v/MbYgrxtQMxznQTCndFj7WjmAhBG4DmPNvKFaPpGihoEC5t43wVThjqO9uNjNQ3jEuY50NUE1tOJdk4oBpR4ry4cUAAJMv4oX60YH0TrSsD9k2wopwiHZ4vkJ7v09rMEWB/t8XsfPbhKtaDxBSD9L6M6CWabl8ZKTlSSkWx8rh6F5PHoN/Yvf4O3Q4ns4lMrI+nYxyD4Q42DqaC9CftEbH0QM5QSzTXZ828eCBPAupo=",
        "ddl_examtype": "4",
        "ddl_year": "2023",
        "rb_searchby": "1",
        "txtRollNo": rnum,
        "txtName": "",
        "btnViewResult": "View Result"
                })
        #print(response.data)
        soup = BeautifulSoup(response.data, 'html.parser')
        # input_element1 = soup.find(id="txtStudentName")
        # name=input_element1.get('value')
        # input_element2 = soup.find(id="txtStudentFatherName")
        # fname=input_element2.get('value')
        
        # input_element3 = soup.find(id="txtStudentSubejctGroup")
        # group=input_element3.get('value')
        # input_element4 = soup.find(id="txtRollNo")
        # Roll_NUm=input_element4.get('value')
        # print(Roll_NUm,fname,name,group)
        # row=[Roll_NUm,name,fname,group]
        # return row

        #print(soup.text)
        if 'BIOLOGY' in soup.text:
        #     span = soup.find_all("b")
        #     rn = (f'{span[0].text}')
        #     name = (f'{span[2].text}')
        #     fname = (f'{span[3].text}')
        #     marks = int((f'{span[6].text}'))
        #    # print(rn)
        #     print(rn,name,fname,marks)

            # table = soup.find('table')  # get desired table
            # td_tags = table.select('td')

            # for (i, item) in enumerate(td_tags, start=1):
            #     print(i, item)

            name=soup.find(id="lblName").text
            Roll_Num=soup.find(id="lblRollNumber").text
            marks=soup.find(id="lblTotal").text
            phy = soup.find(id="Repeater_result4_Label6_5").text
            chem = soup.find(id="Repeater_result4_Label6_6").text
            bio = soup.find(id="Repeater_result4_Label6_4").text
            marks1 = int(phy) + int(bio) + int(chem)
            row = [Roll_Num, name,marks,marks1]
            print(name,Roll_Num,marks,marks1)
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

with alive_bar(762357 - 700001) as bar:
    with ThreadPoolExecutor(max_workers=15) as executor:
        for i in range(725484, 760717):
            processes.append(executor.submit(download_file, f'https://results.biserawalpindi.edu.pk/', i))
#https://result.bisegrw.edu.pk/result-card.html
# http://www.bisegrw.edu.pk/result-card-matric.html  old
for task in as_completed(processes):
    if type(task.result()) is not str:
        print(task.result())
        with open('RwpResult2023Main.csv', 'a', newline='') as new:
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