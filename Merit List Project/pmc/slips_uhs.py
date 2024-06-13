from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
import urllib3,csv,re
from io import BytesIO
from alive_progress import alive_bar
import base64
http = urllib3.PoolManager()


print('-----------------------STARTING------------------------')
#filename = input("Enter Filename:\n")
#start_line = int(input('Enter starting line No:\n'))
#end_line = int(input('Enter ending line No:\n'))
failed_file = input('Enter failed Filename:\n')

#with open(filename)as new:
#    lines = [line.rstrip() for line in new]


print('-------------------------File Loaded-------------------')

def download_file(url):
    try:
        response = http.request('GET',url)

        pdf = response.data
        bar()
        return pdf,url[-25:-13]

        
    except Exception as e:
        print(e)
        return url[-25:-13]


start = time()

processes = []

n_id = 45105
# n_id = 1202

with alive_bar(4024107 - 4020000) as bar:
    with ThreadPoolExecutor(max_workers=6) as executor:
        for i in range(1036054, 1036065):
            print(i);print(n_id)
            rn = base64.b64encode(str(i).encode('ascii'))
            nid = base64.b64encode(str(n_id).encode('ascii'))
            url = f'http://111.68.105.13/mdcat2022/exams.php?action=ET_DownloadSlip&rn={rn.decode("ascii")}&nId={nid.decode("ascii")}'
            print(url)
            processes.append(executor.submit(download_file, url))
            n_id +=1



    for task in as_completed(processes):
        print(task.result()[1])
        if type(task.result()) is not str:
            with open(f'bwp-female2/{(base64.b64decode(task.result()[1])).decode("ascii")}.pdf','wb') as new:
                new.write(task.result()[0])
        else:
            print('test')
            with open(failed_file,'a')as fail:
                fail.write(f'{task.result()}\n')

        
        
        
        
        
        

print(f'Time taken: {time() - start}')