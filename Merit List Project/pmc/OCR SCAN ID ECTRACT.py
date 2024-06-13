from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time,sleep
import csv,re,base64
from alive_progress import alive_bar
from tika import parser
import os
import glob

#print('-----------------------STARTING------------------------')
#filename = input("Enter Filename:\n")
#start_line = int(input('Enter starting line No:\n'))
#end_line = int(input('Enter ending line No:\n'))
#failed_file = input('Enter failed Filename:\n')

print('-------------------------File Loaded-------------------')

path = glob.glob("dgk-male/*.pdf")

def pdf_extract(filename):
    try:
        text = parser.from_file(filename)
        #print(text['content'])
        rn = (re.search(r'Roll Number\n(.*?)\n', text['content']).group(1))
        name = (re.search(r'Full Name: (.*?)\n', text['content']).group(1))
        fname = (re.search(r'Father\'s Name: (.*?)\n', text['content']).group(1))
        cnic = (re.search(r'ID Number: (.*?)\n', text['content']).group(1)) + "'"
        row = [rn,name,fname,cnic]
        print(row)
        bar()
        return row
    except Exception as e:
        print(e)
        bar()
        return filename


start = time()

processes = []

with alive_bar(len(path)) as bar:
    with ThreadPoolExecutor(max_workers=4) as executor:
        for i in path:
            sleep(0.01)
            processes.append(executor.submit(pdf_extract,i))

    for task in as_completed(processes):
        if type(task.result()) is not str:
            with open('dgk-male.csv','a',newline='') as new:
                res_writer = csv.writer(new, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                res_writer.writerow(task.result())
        else:
            with open('failed.txt','a')as fail:
                fail.write(f'{task.result()}\n')

        
        
        
        
        
        

print(f'Time taken: {time() - start}')