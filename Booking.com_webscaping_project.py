import requests
from bs4 import BeautifulSoup
import csv
import time
import random

def web_scrapper2(web_url, f_name):
    # Greetings
    print("Thank you for sharing the URL and file name!\n⏳ Reading the content...")

    # Random delay to mimic human behavior
    num = random.randint(3, 7)
    time.sleep(num)

    # Headers for the request
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }

    # Send GET request
    response = requests.get(web_url, headers=header)

    if response.status_code == 200:
        print("Connected to the website")
        html_content = response.text

        # Creating soup
        soup = BeautifulSoup(html_content, 'lxml')

        # Main containers for hotels
        hotel_divs = soup.find_all('div', role="listitem")

        with open(f'{f_name}.csv', 'w', encoding='utf-8', newline='') as file_csv:
            writer = csv.writer(file_csv)

            # Adding header
            writer.writerow(['Hotel Name', 'Location', 'Price', 'Rating', 'Score', 'Review', 'Link'])

            # Extracting data
            for hotel in hotel_divs:
                try:
                    hotel_name = hotel.find('div', class_="f6431b446c a15b38c233")
                    hotel_name = hotel_name.text.strip() if hotel_name else "NA"

                    location = hotel.find('span', class_="aee5343fdb def9bc142a")
                    location = location.text.strip() if location else "NA"

                    price = hotel.find('span', class_="f6431b446c fbfd7c1165 e84eb96b1f")
                    price = price.text.replace('₹ ', '').strip() if price else "NA"

                    rating = hotel.find('div', class_="a3b8729ab1 e6208ee469 cb2cbb3ccb")
                    rating = rating.text.strip() if rating else "NA"

                    score = hotel.find('div', class_="a3b8729ab1 d86cee9b25")
                    score = score.text.strip().split(' ')[-1] if score else "NA"

                    review = hotel.find('div', class_="abf093bdfe f45d8e4c32 d935416c47")
                    review = review.text.strip() if review else "NA"

                    link = hotel.find('a', href=True)
                    link = "https://www.booking.com" + link['href'] if link else "NA"

                    # Save data to CSV
                    writer.writerow([hotel_name, location, price, rating, score, review, link])

                except Exception as e:
                    print(f"Error extracting hotel data: {e}")

        print("Web scraping complete. Data saved to file.")
    else:
        print(f"Connection failed! HTTP Status Code: {response.status_code}")

# Execute only if run as a script
if __name__ == '__main__':
    url = input("Please enter URL: ")
    fn = input("Please give a file name: ")

    # Calling the function
    web_scrapper2(url, fn)
