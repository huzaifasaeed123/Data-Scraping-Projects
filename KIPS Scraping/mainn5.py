import string
import secrets
import requests
from docx import Document
from urllib.parse import urlencode
import base64
import os
os.environ['path'] += r';C:\Program Files\UniConvertor-2.0rc5\dlls'
import ffmpeg
import m3u8_To_MP4
import gzip
import sys
import pdfkit
def login(api_url, username, password):
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Api-Security-Key": "A956FFC5-8069-47F3-B1D7-AC6E11A21BFD"}
    data = {"username": username, "password": password, "grant_type":"password"}
    response = requests.post(api_url, headers=headers, data=urlencode(data))

    if response.status_code == 200:
        login_data = response.json()
        auth_token = login_data.get("access_token")
        return auth_token
    else:
        raise Exception(f"Login failed. Status code: {response.status_code}")

def fetch_subjects(api_url, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}", "Api-Security-Key": "A956FFC5-8069-47F3-B1D7-AC6E11A21BFD"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        subjects_data = response.json()
        return subjects_data
    else:
        raise Exception(f"Failed to fetch subjects data from API. Status code: {response.status_code}") 


def download_video(video_url, token, output_path='downloaded_video2.mp4'):
    headers = {'Authorization': f"Bearer {token}", "Api-Security-Key": 'A956FFC5-8069-47F3-B1D7-AC6E11A21BFD',
                'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Origin': 'https://student.kipslms.com',
        'Referer': 'https://student.kipslms.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site'}
    try:
        if headers:
            headers_str = "\r\n".join(f"{k}: {v}" for k, v in headers.items()) + "\r\n"
        else:
            headers_str = ""
        (
            ffmpeg
            .input(video_url, headers=headers_str)
            .output(output_path, codec="copy")
            .run(overwrite_output=True)
        )
        print(f"Video successfully converted to {output_path}")
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
def html_to_pdf(html_text,path):
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
    }
    
    directory = os.path.dirname(path)
    
    # Check if directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    try:
        pdfkit.from_string(html_text, path, options=options,configuration=pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'))
        print(f"PDF generated successfully at {path}")
    except Exception as e:
        print(f"Error generating PDF: {e}")  

if __name__ == "__main__":
    login_url = "https://api.kipslms.com/api/v5/oauth/token"  # Replace with the login API endpoint URL 84755
    subjects_url = "https://api.kipslms.com/api/v5/CandidateCourseService/GetCourseSubjectDayActivitites?candidateSOSId=543907&subjectId=29120&sosDetailId=206814&groupName=WEEK+1"  # Replace with the subjects API endpoint URL
    #subjects_url = "https://api.kipslms.com/api/v5/CandidateCourseService/GetCourseSubjectActivityGroups?candidateSOSId=543907&subjectId=29120"  # Replace with the subjects API endpoint URL
    #subjects_url = "https://api.kipslms.com/api/v5/CandidateCourseService/GetCourseSubjectActivityDays?candidateSOSId=543907&subjectId=29120&groupName=WEEK+1"  # Replace with the subjects API endpoint URL
    #subjects_url = "https://api.kipslms.com/api/v5/CandidateContentService/GetContentVideo?contentId=63637&sosDetailContentId=779621&CandidateSOSId=543907"  # Replace with the subjects API endpoint URL
    course_url = "https://api.kipslms.com/api/v5/CandidateCourseService/GetMyCourses?CourseType=1"  # Replace with the subjects API endpoint URL
    #video_url = "https://cdn.kipslms.com/kipslms/VideoLectures-HLS/210203_ETP_Chem_NMDCAT_Unit_1_Mole_Molar_Volume_Dr_Saeed_02_02_2021_playlist.m3u8"  # Replace with the subjects API endpoint URL
    #video_url = "https://cdn.kipslms.com/kipslms/VideoLectures-HLS/210203_ETP_Chem_NMDCAT_Unit_1_Mole_Molar_Volume_Dr_Saeed_02_02_2021/360p.m3u8"  # Replace with the subjects API endpoint URL
    username = "saeedhuzaifa111@gmail.com"  # Replace with your username
    password = "Saeed@123"  # Replace with your password

    wordpress_user = "abaid987"
    wordpress_password = "jWKY daN1 KvS6 fsZl sz5A qlgS"

    wordpress_url = "https://saeedmdcatlms.com/wp-json/wp/v2/media"

    wordpress_credentials = wordpress_user + ":" + wordpress_password
    wordpress_token = base64.b64encode(wordpress_credentials.encode())
    
    try:
        auth_token = login(login_url, username, password)
        # subject_data = fetch_subjects(subjects_url, auth_token) 
        # print(subject_data)   
        # sys.exit()
        course_data = fetch_subjects(course_url, auth_token)
        for course in course_data['Courses'][0]['Subjects']:
            subject_id=course['SubjectId']
            subject_Name=course['SubjectName']
            index2=0
            index3=0
            for index in range(1, 11):
                subjects_url=f"https://api.kipslms.com/api/v5/CandidateCourseService/GetCourseSubjectActivityDays?candidateSOSId=551981&subjectId={subject_id}&groupName=WEEK+{index}"
                subject_data = fetch_subjects(subjects_url, auth_token)
                # print(subject_data)
                # sys.exit()
                for week in subject_data:
                    SOSDetailId=week["SOSDetailId"]
                    GroupName=week["GroupName"]
                    week_url = f"https://api.kipslms.com/api/v5/CandidateCourseService/GetCourseSubjectDayActivitites?candidateSOSId=551981&subjectId={subject_id}&sosDetailId={SOSDetailId}" 
                    week_data=fetch_subjects(week_url, auth_token)
                    for day in week_data:
                        #print("2nd")
                        ContentId=day["ContentId"]
                        SOSDetailContentId=day["SOSDetailContentId"]
                        Title=day["Title"]
                    #print(Title," Prev title")
                        if day["ActivityType"]==1:
                            
                            #print(Title)
                            # video_url=f"https://api.kipslms.com/api/v5/CandidateContentService/GetContentVideo?contentId={ContentId}&sosDetailContentId={SOSDetailContentId}&CandidateSOSId=543907"
                            # video_data=fetch_subjects(video_url, auth_token)
                            # print(video_data["VideoLink"])
                            # print(video_data["Title"])
                            index2+=1
                            #print(f"{index2}-{Title}.mp4")
                            # download_video("https://cdn.kipslms.com/kipslms/VideoLectures-HLS/210203_ETP_Chem_NMDCAT_Unit_1_Mole_Molar_Volume_Dr_Saeed_02_02_2021/360p.m3u8",auth_token
                            #               ,f"{index2}-{Title}.mp4" )
                            #sys.exit()
                        elif day["ActivityType"]==2:
                            notes_url=f"https://api.kipslms.com/api/v5/CandidateContentService/GetContentReading?contentId={ContentId}&sosDetailContentId={SOSDetailContentId}&CandidateSOSId=551981"
                            notes_data=fetch_subjects(notes_url, auth_token)
                            content=notes_data["Description"]
                            title=notes_data["Title"]
                            print(title)
                            index3+=1
                            path=f"NotesECAT/{subject_Name}/{index3}-{Title}.pdf"
                            html_to_pdf(content,path)
                            #
                            #print(notes_data)
                        
    
                        #sys.exit()
                    # print(ContentId)
                    # print(SOSDetailContentId)
                    


                
        # subject_data=fetch_subjects(subjects_url, auth_token)
        # print(subject_data)
        #download_video(video_url,auth_token)
        print("ddfkdjf")
        #print(auth_token)
        counter=0
        # for subject in subjects_data['Tests']:
        #     word_output_file = f"PHY/{subject['TestName'].replace('|', '')}.docx"            # Replace with the desired output Word file name
        #     if os.path.exists(word_output_file):
        #         word_output_file = f"Testing/{subject['TestName'].replace('|', '')} {counter}.docx"
        #         counter += 1
        #     test_id = subject["TestId"]
        #     questions_url = f"https://api.kipslms.com/api/v5/CandidateContentService/GetContentVideo?contentId=63637&sosDetailContentId=779621&CandidateSOSId=543907"  # Replace with the questions API endpoint URL
        #     questions_data = fetch_questions(questions_url, auth_token)
        #     #print(questions_data)
        #     #create_word_document(questions_data, word_output_file)
        #     print("Word document created successfully.")
    except Exception as e:
        print(f"Error: {e}")
