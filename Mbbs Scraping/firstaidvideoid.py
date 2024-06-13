import json
import requests
import ffmpeg
import m3u8
from bs4 import BeautifulSoup
from subprocess import check_call
import re
from iframe import BunnyVideoDRM


# Define the login URL and the credentials
login_url = 'https://firstaidmadeeasy.com.pk/Account/Login'  # Replace with the actual login URL
credentials = {
    'StoredID': '',
    'Email': 'chaudharyritesh980@gmail.com',  # Replace with your actual username
    'Password': 'Rkc@980'   # Replace with your actual password
}
# Headers to include in the video request
headers = {
    'Cookie':'qbsWX-gxuq_0Vz3agFCIA_rxBgtYs-1qt9KyoLV9DcH2j6wY1ULWLpDmzQmh0tbVGooFFuU3iqSE8sWsPihMAS4PHVG-_Hlifos3IOsbQoU1',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://iframe.mediadelivery.net/embed/6781/27dc83d0-ffe8-458b-9404-716fda06d9a1?autoplay=true',  # Replace with the actual referer URL
    'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'  # Replace with the actual user-agent string
}

session = requests.Session()
def get_video_path(videoid,sectionid):
    try:
        # Send a GET request to the specified URL
        url=f"https://firstaidmadeeasy.com.pk/Student/GetVideoPath?VideoID={videoid}&SecID={sectionid}"
        response = session.get(url)
        # Check if the request was successful
        response.raise_for_status()
        # Convert the response content into JSON format
        data = response.json()
        url = data['Video']['Video_Path']
        name = data['Video']['Video_Name']
        #cprint("Befor Cutting",url)
    # If the query parameter is found, remove it
        question_mark_index = url.find('?')
    
    # If '?' is found, cut the URL at that position (including '?')
        if question_mark_index != -1:
            url = url[:question_mark_index]  # Include '?' in the slice
    
        object={
            "url":url,
            "video_name":name
        }
        #print(url)
        return object
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except json.JSONDecodeError:
        print("Failed to decode JSON from the response")
def fetch_id(SectionId):
    url = f"https://firstaidmadeeasy.com.pk/Student/TakeCourse/{SectionId}"  # Replace with the actual URL

# Send a GET request to the URL
    response = session.get(url)
    if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        video_elements = soup.find_all('a', class_='btnplayVideo')
    
    # List to store the video details
    videos = []

    # Iterate over each element and extract data-id and other details
    for element in video_elements:
        video_id = element.get('data-id')
        videos.append(video_id)
    
    return videos

# Perform login
login_response = session.post(login_url, data=credentials)
SectionId=5
# Check if login was successful
if login_response.status_code == 200:
    videos_id=fetch_id(SectionId)
    video_path=[]
    index=0
    for videoid in videos_id:
        index=index+1
        
        #video_path.append(get_video_path(videoid,5))
        video_url_object=get_video_path(videoid,SectionId)
        name=f"{index}-{video_url_object['video_name']}"
        print(name)
        video = BunnyVideoDRM(
        # insert the referer between the quotes below (address of your webpage)
        referer=video_url_object['url'],
        # paste your embed link
        embed_url=video_url_object["url"],
        # you can override file name, no extension
        name=f"{index}-{video_url_object['video_name']}",
        # you can override download path
        path=r"/MBBS Videos")
    # video.session.close()
        video.download()
    
    #(video_path)   
    
else:
    print(f"Login failed: {login_response.status_code}")
