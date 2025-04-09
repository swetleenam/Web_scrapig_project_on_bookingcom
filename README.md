# 🕸️ Booking.com Hotel Scraper

This Python script is a simple web scraping tool designed to extract hotel information from [Booking.com](https://www.booking.com) using the BeautifulSoup and Requests libraries.

---

## 🚀 Features

- Extracts key details such as:
  - 🏨 Hotel name  
  - 📍 Location  
  - 💰 Price  
  - ⭐ Rating & score  
  - 📝 Review summary  
  - 🔗 Direct link to the hotel page  
- Automatically saves the extracted data into a `.csv` file  
- Includes randomized delays to mimic human browsing behavior  
- User-friendly input prompts for URL and output file name  
- Handles missing data gracefully with default `"NA"` values  

---

## 🧠 How It Works

1. The script takes a Booking.com search results URL and a filename from the user.
2. It makes an HTTP request with browser-like headers to avoid bot detection.
3. The HTML content is parsed using BeautifulSoup.
4. All hotel cards are identified and relevant information is extracted.
5. Data is saved into a well-formatted CSV file.

---

## 🧰 Requirements

- Python 3.x  
- `requests`  
- `beautifulsoup4`  
- `lxml`

Install dependencies with:

```bash
pip install requests beautifulsoup4 lxml
