from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from bs4 import BeautifulSoup
import urllib3,csv
from alive_progress import alive_bar

http = urllib3.PoolManager()


print('-----------------------STARTING------------------------')
#filename = input("Enter Filename:\n")
start_line = int(input('Enter starting line No:\n'))
end_line = int(input('Enter ending line No:\n'))
#failed_file = input('Enter failed Filename:\n')

with open('cinc2.txt')as new:
    lines = [line.rstrip() for line in new]


print('-------------------------File Loaded-------------------')

def download_file(url):
    try:
        response = http.request('GET',url)
        soup = BeautifulSoup(response.data,'html.parser')
        
        name = soup.find(id='name').text
        marks = soup.find(id='omarks').text
        cnic = soup.find(id='cnic').text


        row = [name,marks,cnic]

        bar()
        return row
    except Exception as e:
        #print(e)
        bar()
        return url


start = time()

processes = []

with alive_bar(end_line-start_line) as bar:
    with ThreadPoolExecutor(max_workers=20) as executor:
        for i in lines[start_line:end_line]:
            #print(i)
            processes.append(executor.submit(download_file, f'https://pmc.gov.pk/Results/ResultsInfo?rollNo={i}&session=2022'))

    for task in as_completed(processes):
        print(task.result())
        if type(task.result()) is not str:
            with open('resultspmc_2022.csv','a',newline='') as new:
                res_writer = csv.writer(new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                res_writer.writerow(task.result())
        else:
            with open('failed_file','a')as fail:
                fail.write(f'{task.result()}\n')

        
        
        
        
        
        

print(f'Time taken: {time() - start}')