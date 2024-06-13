import requests
from bs4 import BeautifulSoup
import json
import os
session = requests.Session()
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/333.4629917.798.43',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
        # Add more headers if needed
    }
def download_pdf(video_list):
    index=1
    for pdf in reversed(video_list):
        url = pdf['url']
        title = pdf['title']
        try:
            # Create a directory to store the downloaded videos if it doesn't exist
            if not os.path.exists("PhyInSeconds/LR"):
                os.makedirs("PhyInSeconds/LR")

            # Download the video from the URL
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                # Write the video content to a file with the title as the filename
                with open(f"PhyInSeconds/LR/{index}-{title}.pdf", 'wb') as f:
                    f.write(response.content)
                    index=index+1
                print(f"PDF '{title}' downloaded successfully.")
            else:
                print(f"Failed to download PDF '{title}' from {url}.")
        except Exception as e:
            print(e)


def make_login():
    login_data = {
        'email': 'hannanujjan39@gmail.com',
        'login': 'hannanujjan39@gmail.com',
        'password': 'ABDullahshabaz11*'
    }
    session.post("https://physicsinseconds.com/api/signin",headers=headers,data=login_data)
    #response=session.get("https://physicsinseconds.com/api/course/mdcat-biology-advance?contents",headers=headers)
    response=session.get("https://physicsinseconds.com/api/course/mdcat-logical-reasoning?contents",headers=headers)
    #soup=BeautifulSoup(response.content,'html.parser')
    #Request URL: https://physicsinseconds.com/api/unlock/pdf/1-Lecture%20%201%20Nervous%20System-2-2.pdf?courseid=mdcat-biology-advance&section=mdcat_coordination__control&json

    #print(response.content)
    json_data = response.json()
    #print(json_data)
    pdf_details=[]
    with open("example2.txt", "w") as file:
        file.write(json.dumps(json_data))
    for key in json_data['course']['objects']:
        # print(key)
        # print(json_data['course']['objects'][key]['objectType'])
        # print(json_data['course']['objects'][key]['title'])
        #print(json_data['course']['objects'][i]['objectType']['data']['pdf_full'])
        try:
            if(json_data['course']['objects'][key]['objectType']=='pdf'):
                data={
                    'url':json_data['course']['objects'][key]['data']['pdf_full'],
                    'title': json_data['course']['objects'][key]['title']
                }
                print(data['title'])
                pdf_details.append(data)
                
        except Exception as e:
            print(e)
    return pdf_details
details=make_login()
#print(details)
download_pdf(details)
# print(details)
