# 1st Project-Amazon Price Tracker Bot

This project is a Python bot that tracks the prices of products on Amazon and notifies users when the price drops below a certain threshold.

### Features
- Tracks the prices of products on Amazon.
- Sends email notifications when the price drops below a certain threshold.
- Uses BeautifulSoup for web scraping and smtplib for sending emails.
  
### Usage
- Modify the url variable in the amazon_price_tracker.py file to the URL of the product you want to track.
  
### Configuration
- Set up a Gmail account to send the notification emails.
- Enable less secure apps access in your Gmail account settings.
- Update the sender_mail and password variables in the amazon_price_tracker.py file with your Gmail email address and password.

### Contributing
- Contributions are welcome! Please fork the repository and submit a pull request with your changes.
- ![image](https://github.com/huzaifasaeed123/Data-Scraping-Practice/assets/143410512/545f5326-1439-4384-b836-6a533f5213fd)

# 2nd Project-Spotify Playlist Creator from Billboard Top 100

### Project Description

This project scrapes the top 100 song titles from the Billboard website and creates a Spotify playlist, adding all those top 100 songs to the playlist automatically.

### Features

- **Web Scraping**: Extracts the top 100 songs from Billboard's website.
- **Spotify Integration**: Creates a playlist on Spotify and adds the scraped songs to it.

### How It Works

1. **Scrape Billboard Top 100**: The script uses BeautifulSoup to scrape song titles from Billboard's Hot 100 chart.
2. **Spotify API**: Utilizes the Spotipy library to interact with the Spotify API.
   - Authenticates with Spotify using OAuth.
   - Creates a new playlist.
   - Searches for each song on Spotify and adds it to the created playlist.
   - See Playlist Details on given link https://open.spotify.com/playlist/6uodKBXWI0S5IAPSFMtLDX
   - And Here is the Screenshot of created Playlist
   - ![image](https://github.com/huzaifasaeed123/Data-Scraping-Projects/assets/143410512/cb9b8378-501f-4f90-9f44-b53197c70645)

# 3rd Project-Video Downloader from Biology Guardian

## Project Description

This project scrapes all video links from a specified website and downloads all videos with their titles into a specific folder.

## Features

- **Web Scraping**: Extracts video links from specified chapters on the Biology Guardian website.
- **Authentication**: Logs in to the website using provided credentials.
- **Video Downloading**: Downloads all the scraped videos and saves them with appropriate titles in the specified folder.

## Steps

1. **Session Initialization**: Initialize a session to persist the login session and set headers for the requests.
2. **Token Extraction**: Access the login page and extract the CSRF token required for authentication.
3. **Login**: Post the login credentials along with the extracted token to authenticate with the website.
4. **Chapter Access**: Access the restricted pages (chapters) containing the videos.
5. **Video Link Extraction**: Scrape the video links from each chapter page.
6. **Video Downloading**: Download each video from the extracted links and save them in a specified folder with appropriate titles.

Thank you for checking out this project! Feel free to contribute or reach out if you have any questions.
# 4th Project-MCQs and Video Content Downloader from Kips LMS

## Project Description

This project has two main parts:

1. **MCQs Extraction and Word Document Creation**: Extracts complete MCQs tests with all details from the Kips LMS API and converts these tests into properly formatted Word documents. Images are directly uploaded to a WordPress LMS, and their links are saved in the Word documents in place of the images.
2. **Video and Notes Extraction**: Extracts videos (in m3u8 format) and notes from the same website, handling encryption tokens on videos and other content, and saves the videos and notes appropriately.

## Features

### Part 1: MCQs Extraction and Word Document Creation

- **Authentication**: Logs in to the Kips LMS API using provided credentials.
- **Subjects Fetching**: Fetches subjects and corresponding tests from the API.
- **Questions Extraction**: Retrieves questions for each test.
- **Image Handling**: Downloads images from the question content and uploads them to a WordPress LMS, then replaces the image URLs in the questions with the uploaded image URLs.
- **Word Document Generation**: Creates a Word document for each test, including questions, options, correct answers, and explanations.

### Part 2: Video and Notes Extraction

- **Authentication**: Logs in to the Kips LMS API using provided credentials.
- **Subjects Fetching**: Fetches subjects and corresponding content from the API.
- **Video Downloading**: Downloads encrypted videos (m3u8 format) using ffmpeg.
- **Notes Downloading**: Downloads notes and converts them to PDF format.
- **Encryption Handling**: Manages encryption tokens required for video and content access.

## Steps

### Part 1: MCQs Extraction and Word Document Creation

1. **Session Initialization**: Initialize a session to persist the login session and set headers for the requests.
2. **Token Extraction**: Access the login page and extract the CSRF token required for authentication.
3. **Login**: Post the login credentials along with the extracted token to authenticate with the API.
4. **Subjects Fetching**: Fetch the subjects data from the API.
5. **Questions Fetching**: Fetch the questions for each test.
6. **Image Downloading and Uploading**: Download images from the questions, upload them to the WordPress LMS, and replace the image URLs in the questions with the uploaded image URLs.
7. **Word Document Creation**: Create a Word document for each test with formatted questions, options, correct answers, and explanations.

### Part 2: Video and Notes Extraction

1. **Session Initialization**: Initialize a session to persist the login session and set headers for the requests.
2. **Token Extraction**: Access the login page and extract the CSRF token required for authentication.
3. **Login**: Post the login credentials along with the extracted token to authenticate with the API.
4. **Subjects Fetching**: Fetch the subjects data from the API.
5. **Content Fetching**: Fetch the content for each subject, including videos and notes.
6. **Video Downloading**: Download encrypted videos (m3u8 format) using ffmpeg and handle the encryption tokens.
7. **Notes Downloading**: Download notes and convert them to PDF format.
8. **Save Content**: Save the downloaded videos and notes in the appropriate format and location.

Thank you for checking out this project! Feel free to contribute or reach out if you have any questions.

# 5th Project-Hidden API Scraper for PhyInSecond LMS

## Project Description

This project scrapes all website content by targeting hidden APIs used on the website. By scraping these hidden APIs, we access all available content, including downloading videos with special titles and notes.

## Features

- **Hidden API Targeting**: Identifies and targets hidden APIs to access website content.
- **Content Aggregation**: Combines information from multiple APIs to gather comprehensive data.
- **Video Downloading**: Downloads videos using extracted URLs and saves them with appropriate titles.

## Steps

### Hidden API Scraping and Content Extraction

1. **Session Initialization**: Initialize a session to persist the login session and set headers for the requests.
2. **Login**: Post the login credentials to authenticate with the website.
3. **Fetch Course Content**: Access the course content API to retrieve the list of videos.
4. **Extract Video Source IDs**: Iterate through the list of videos to extract the source IDs.
5. **Fetch Video Details**: Use the source IDs to fetch video details from another API.
6. **Aggregate Video Data**: Combine the information from the APIs to gather video URLs and titles.
7. **Download Videos**: Download the videos using the aggregated URLs and save them with appropriate titles.

Thank you for checking out this project! Feel free to contribute or reach out if you have any questions.
# 6th Project-Encrypted Iframe Video Downloader

## Project Description

This project scrapes hidden APIs to extract video private IDs or keys, combines these IDs to construct video URLs, and downloads specially encrypted iframe videos. Using this code, over 2000 encrypted videos, totaling nearly 2TB in size, were downloaded from a website.

## Features

- **Hidden API Targeting**: Identifies and targets hidden APIs to access video content.
- **ID Extraction**: Extracts private video IDs from multiple APIs.
- **URL Construction**: Combines extracted IDs to create valid video URLs.
- **Encrypted Video Downloading**: Downloads specially encrypted iframe videos using the constructed URLs.

## Steps

### Hidden API Scraping and ID Extraction

1. **Session Initialization**: Initialize a session to persist the login session and set headers for the requests.
2. **Login**: Post the login credentials to authenticate with the website.
3. **Fetch Video IDs**: Access the course content API to retrieve the list of video IDs.
4. **Extract Video Paths**: Use the video IDs to fetch video paths and details from another API.
5. **Construct Video URLs**: Combine the extracted video IDs and paths to construct valid video URLs.
6. **Download Encrypted Videos**: Pass the constructed URLs to the `BunnyVideoDRM` class to download the encrypted iframe videos.

### Encrypted Iframe Video Downloading

1. **Prepare Download**: Ping and activate the video context using the extracted IDs and paths.
2. **Download Video**: Use `yt-dlp` to download the encrypted video from the constructed URL.

## Achievements

- **Massive Data Download**: Successfully downloaded over 2000 encrypted videos.
- **Large Data Size**: Managed a total download size of nearly 2TB.

Thank you for checking out this project! Feel free to contribute or reach out if you have any questions.

# 7th Project-MCQs Scraper and Formatter from StepBYPGC

## Project Description

This project scrapes more than 25,000 MCQs from the StepBYPGC website by targeting hidden APIs and formats these MCQs into a special format in Word documents. The scraping process involves using Microsoft authentication to access the hidden APIs and extract the required data.

## Features

- **Hidden API Targeting**: Identifies and targets hidden APIs to access MCQs content.
- **Massive Data Extraction**: Successfully scraped over 25,000 MCQs.
- **MCQs Formatting**: Formats the extracted MCQs into a special format in Word documents, including images.
- **Automated Word Document Creation**: Automatically generates Word documents for each set of MCQs.

## Steps

1. **Session Initialization**: Initialize a session to persist the login session and set headers for the requests.
2. **Login**: Authenticate using Microsoft credentials to access the hidden APIs.
3. **Fetch Work Batch Data**: Retrieve work batch data from the API.
4. **Fetch Work Day Data**: For each work day, fetch the corresponding MCQs tests and other related data.
5. **Extract and Format MCQs**: Extract MCQs and format them into a special format in Word documents.
6. **Download Images**: Download any images associated with the MCQs and include them in the Word documents.
7. **Save Word Documents**: Save the formatted MCQs as Word documents with appropriate titles.

## Achievements

- **Large Scale Data Extraction**: Successfully extracted and formatted over 25,000 MCQs.
- **Automated Document Generation**: Created Word documents in a special format, ready for use or distribution.

## Example

Here is an example screenshot of the formatted Word document:

![image](https://github.com/huzaifasaeed123/Data-Scraping-Projects/assets/143410512/8ee6c24c-f7ac-491e-b7e9-74c7951f99d2)

Thank you for checking out this project! Feel free to contribute or reach out if you have any questions.


# 8th Project-MCQs Scraper and Formatter from Premed.pk

## Project Description

This project scrapes more than 50,000 MCQs from the Premed.pk website by targeting hidden APIs and formats these MCQs into a special format in Word documents. The scraping process involves accessing the hidden APIs to extract the required data.

## Features

- **Hidden API Targeting**: Identifies and targets hidden APIs to access MCQs content.
- **Massive Data Extraction**: Successfully scraped over 50,000 MCQs.
- **MCQs Formatting**: Formats the extracted MCQs into a special format in Word documents, including images.
- **Automated Word Document Creation**: Automatically generates Word documents for each set of MCQs.

## Steps

1. **Session Initialization**: Initialize a session to set headers for the requests.
2. **Fetch MCQs Data**: Access the hidden APIs to retrieve the MCQs data.
3. **Extract and Format MCQs**: Extract MCQs and format them into a special format in Word documents.
4. **Download Images**: Download any images associated with the MCQs and include them in the Word documents.
5. **Save Word Documents**: Save the formatted MCQs as Word documents with appropriate titles.

## Achievements

- **Large Scale Data Extraction**: Successfully extracted and formatted over 50,000 MCQs.
- **Automated Document Generation**: Created Word documents in a special format, ready for use or distribution.

## Example

Here is an example screenshot of the formatted Word document:

![image](https://github.com/huzaifasaeed123/Data-Scraping-Projects/assets/143410512/05910486-04f0-4560-afe1-00a532346766)


Thank you for checking out this project! Feel free to contribute or reach out if you have any questions.

