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
   
