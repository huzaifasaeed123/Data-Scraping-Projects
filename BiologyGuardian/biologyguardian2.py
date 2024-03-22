import requests
from bs4 import BeautifulSoup
import os
import time
session = requests.Session()
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        # Add more headers if needed
    }
cookies = {'TOKEN': 'eyJpdiI6IjBvbEo2SENSRGZJanBGU0M5c2haRGc9PSIsInZhbHVlIjoiYXdhTlRLYThWbUkzMHZ3RlRmNm92cFZoMHVWMlJTUkRKeEwvcHRhQ3VpclpPaXJHZENzc3JnTk9IMDc5eU1zUkQwTXhvd2J4T3lNaGtNTDNqelhST3FzbVpZMkY4OEFkNWJ3L1NJY1RTSUxESHVnWFZCbnE4eVBmOE5lUkx5TW4iLCJtYWMiOiI5MTRlY2U3ZGIzNjBmNGE4MjkxNjNmNjIyMTgxOWU1NjdlOTI5ZmY2ZjE5OGY5YmVhOGZhZjM2YmFhZTlmOWYxIiwidGFnIjoiIn0%3D'} 
def takeToken():
    
    response=session.get("https://biologyguardian.com/login",headers=headers)
    soup=BeautifulSoup(response.content,'html.parser')
    # Find the first input tag within the form
    first_input = soup.find('form').find('input')

# Extract the value attribute from the input tag
    if first_input:
        value = first_input.get('value')
        return value
    else:
        print("No input field found")



def login_and_access(url, email, password):
    # Session object to persist the login session
    token=takeToken()

    print(token)
    # Login data
    login_data = {
        '_token': token,
        'email': email,
        'password': password
    }
  
    response = session.post(url, data=login_data,headers=headers)
    print(response.status_code)
    #print(soup)
    if response.status_code == 200:
        print("Login successful")
        # Now you can access the restricted page
        list2=[
            "https://biologyguardian.com/user/chapters/97",
            "https://biologyguardian.com/user/chapters/109",
            "https://biologyguardian.com/user/chapters/124",
            "https://biologyguardian.com/user/chapters/125",
            "https://biologyguardian.com/user/chapters/131",
            "https://biologyguardian.com/user/chapters/132",
            "https://biologyguardian.com/user/chapters/133",
            "https://biologyguardian.com/user/chapters/135",
            "https://biologyguardian.com/user/chapters/137",
            "https://biologyguardian.com/user/chapters/141",
            "https://biologyguardian.com/user/chapters/146",
            "https://biologyguardian.com/user/chapters/147",

        ]
        link_list=[]
        for link in list2:
            chapter = session.get(link,headers=headers)
        
        # Check if access to restricted page was successful
            if chapter.status_code == 200:
                print("Access to restricted page successful")
                soup2=BeautifulSoup(chapter.content,'html.parser')
            
                res=soup2.select(".thumbnail a")
                
                for a in res:
                    href=a.get("href")
                    #lecture = session.get(href,headers=headers)
                    response = session.get(href,headers=headers)  
                    soup3=BeautifulSoup(response.content,'html.parser') 
                    videoTag=soup3.select_one("#videoPreview")
                    VideoLink=videoTag.get("src")
                    #link_list.append("href")
                    link_list.append(VideoLink)
                    print(VideoLink)
            else:
                print("Failed to access the restricted page")
            
            # Print or process the content of the restricted page
        return link_list
            #print(soup)
            
    else:
        print("Login failed")

def download_videos(video_links, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate over the list of video links
    for index, link in enumerate(video_links, start=1):
        try:
            # Send a GET request to the video link
            start_time = time.time()  # Start measuring time
            response = session.get(link,headers=headers)
            end_time = time.time()  # End measuring time

            # Check if request was successful
            if response.status_code == 200:
                # Extract the filename from the URL
                filename = os.path.join(destination_folder, f"{index}-LEC NO-{index}.mp4")

                # Write the content to the file
                with open(filename, 'wb') as file:
                    file.write(response.content)

                print(f"Video {index} downloaded successfully to: {filename}")
                print(f"Time taken to download: {end_time - start_time:.2f} seconds")
            else:
                print(f"Failed to download video {index}. Status code: {response.status_code}")

        except Exception as e:
            print(f"An error occurred while downloading video {index}: {e}")

# Example usage:

#token=takeToken()
links=login_and_access('https://biologyguardian.com/login', 'email@gmail.com', 'Password')
print(links)
download_videos(links, "Biology")