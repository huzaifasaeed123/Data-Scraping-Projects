import requests
import ffmpeg
import m3u8
from bs4 import BeautifulSoup
from subprocess import check_call
import re

# Define the login URL and the credentials
login_url = 'https://firstaidmadeeasy.com.pk/Account/Login'  # Replace with the actual login URL
video_url = 'https://iframe.mediadelivery.net/embed/6781/27dc83d0-ffe8-458b-9404-716fda06d9a1?autoplay=true'  # Replace with the actual video URL
video_url1 = 'https://iframe.mediadelivery.net/27dc83d0-ffe8-458b-9404-716fda06d9a1/playlist.drm?contextId=d51fdf46-ac9e-489e-9de9-21348188581f&secret=c008a465-90c0-4ac5-8e2c-b4d8059cc030'  # Replace with the actual video URL
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
#StoredID 26a385ae-f46d-4fb4-9980-3ec9d02f83fb

def extract_secret_id(text):
    
    pattern2 = r"secret=([a-f0-9\-]+)"
    #secret=48ea7ba8-ad8f-44d8-86c0-38f130aa236d
    
    match = re.search(pattern2, text)
    
    # If a match is found, return the contextId value
    if match:
        return match.group(1)
    else:
        return None
def extract_context_id(text):
    # Define the regex pattern to match contextId
    pattern1 = r"contextId=([a-f0-9\-]+)"
    
    # Search for the pattern in the text
    match = re.search(pattern1, text)
    
    # If a match is found, return the contextId value
    if match:
        return match.group(1)
    else:
        return None
session = requests.Session()
def fetch_id():
    url = 'https://firstaidmadeeasy.com.pk/Student/TakeCourse/5'  # Replace with the actual URL

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
# Create a session
#fetch_id()
session = requests.Session()
# Perform login
login_response = session.post(login_url, data=credentials)
#print(session.headers)
# Check if login was successful
if login_response.status_code == 200:
    # print("Login successful!")
    # response1 = session.get('https://firstaidmadeeasy.com.pk/Account/Login')
    print(session.cookies.get_dict())
    # soup = BeautifulSoup(response1.content, 'html.parser')
    # input_element=soup.find("input", id="StoredID")
    # print(input_element)
    # Request the video URL
    video_response = session.get(video_url,headers=headers, stream=True)
    # print(video_response.content)
    # Check if the video URL request was successful
    
    print(video_response.status_code)
    if video_response.status_code == 200:
        #print(video_response.content)
        contextid=extract_context_id(video_response.content.decode('utf-8'))
        secretid=extract_secret_id(video_response.content.decode('utf-8'))
        print("ContextID="+contextid)
        video_url2 = f"https://iframe.mediadelivery.net/27dc83d0-ffe8-458b-9404-716fda06d9a1/playlist.drm?contextId={contextid}&secret={secretid}"  # Replace with the actual video URL

        # Save the M3U8 playlist content
        # with open('video_playlist.m3u8', 'wb') as file:
        #     file.write(video_response.content)
        #     print(video_response.content)
        # print("M3U8 playlist downloaded successfully!")
        
        # # Load the M3U8 playlist
        # m3u8_obj = m3u8.load('video_playlist.m3u8')
        
        # # Check if the playlist is valid
        # if m3u8_obj.is_variant:
        #     playlist_url = m3u8_obj.playlists[0].absolute_uri
        #     print("jfdkjfkd")
        # else:
        #     playlist_url = video_url
        
        # Convert M3U8 to MP4 using FFmpeg
        cookies = session.cookies.get_dict()
    
        # Format the cookies into a single string
        cookies_header = '; '.join([f'{key}={value}' for key, value in cookies.items()])
        
        # Define headers with the Cookie header
        headers = {
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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',  # Replace with the actual user-agent string
    #'Cookie': cookies_header
    'Cookie':'qbsWX-gxuq_0Vz3agFCIA_rxBgtYs-1qt9KyoLV9DcH2j6wY1ULWLpDmzQmh0tbVGooFFuU3iqSE8sWsPihMAS4PHVG-_Hlifos3IOsbQoU1',
    
        }
        output_file = 'downloaded_video1.mp4'
        try:
            if headers:
                headers_str = "\r\n".join(f"{k}: {v}" for k, v in headers.items()) + "\r\n"
            else:
                headers_str = ""
            (
                ffmpeg
                .input(video_url2, headers=headers_str)
                .output(output_file, codec="copy")
                .run(overwrite_output=True)
            )
            print(f"Video successfully converted to {output_file}")
        except ffmpeg.Error as e:
            print("An error occurred during the conversion process:", e)
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Error: {err}")
        # ffmpeg_command = ['ffmpeg', '-i', playlist_url, '-c', 'copy', output_file]
        # check_call(ffmpeg_command)
        # print(f"Video converted and saved as {output_file}!")
    else:
        print(f"Failed to download video: {video_response.status_code}")

else:
    print(f"Login failed: {login_response.status_code}")
