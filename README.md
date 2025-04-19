Overview
`````````
This Python script allows users to scrape product details from Flipkart based on a search query. It collects and stores data such as product names, prices, discounts, and descriptions from multiple pages and exports the results into a CSV file for further use.

Key Features
````````````
- Command-line based input for product search

- Automatic pagination and multi-page scraping

- Extracts product name, discounted price, original price, discount percentage, and description

- Outputs results into a structured CSV file

- Handles missing data gracefully

Technologies Used
``````````````````
- Python 3.x

- requests – for sending HTTP requests

- BeautifulSoup (from bs4) – for parsing HTML content

- pandas – for data manipulation and CSV export

- re – for regular expressions to clean up pricing strings

How It Works
`````````````
- The script prompts the user for a search query (e.g., “smartphones”).

- It constructs the Flipkart search URL using the query and navigates through all available pages.

- On each page, it extracts:

	- Product names

	- Discounted and original prices

	- Discount percentages

	- Product descriptions

- After scraping, the user is prompted to name the CSV file for saving the collected data.

Usage Instructions
``````````````````
- Ensure all required libraries are installed:

- Run the script in a Python environment.

- Enter your desired search term when prompted (e.g., laptops).

- Enter a name for the output CSV file (e.g., flipkart_laptops.csv).

- The script will scrape the data and create the CSV file in the current directory.

Limitations
````````````
- Ratings are currently commented out due to potential inconsistencies in the DOM structure.

- HTML classes used for scraping may change over time, which would break the scraper.

- Designed specifically for Flipkart's current layout and may require updates for future changes.

Disclaimer
``````````
This script is intended for educational and personal use only. Web scraping should always comply with the website’s terms of service. Use responsibly.

