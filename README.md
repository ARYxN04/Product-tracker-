This Python script automates product price comparison across multiple Indian e-commerce platforms using web scraping and browser automation.

It:
Takes a product name as input.
Searches the product on:
🟠 Amazon India
🔵 Flipkart
🟢 Croma
🔴 Reliance Digital
🌐 Google Shopping

Extracts product names, prices, and links using BeautifulSoup.
Displays a sorted list of results by price.
Opens the cheapest product link automatically in a browser using Selenium.

🧩 System Requirements
Component	Minimum Requirement
OS	Windows, macOS, or Linux
Python	3.8 or above
Chrome Browser	Latest version
Internet Connection	Required
⚙️ Installation Guide

Install Python packages

pip install requests beautifulsoup4 selenium webdriver-manager


Save the script

Copy the code into a file named india_price_comparator.py.

Run the script

python india_price_comparator.py

🚀 How It Works
1. User Input

You enter a product name (e.g., "iphone 15").

2. Scraping Phase (BeautifulSoup)

For each site, the script:

Builds the search URL.

Sends a GET request with a fake browser user-agent.

Parses the HTML using BeautifulSoup.

Extracts:

Product Title

Price

Product Link

3. Data Cleaning

Removes symbols like ₹, commas, or spaces.

Converts prices to numeric floats for sorting.

4. Sorting & Display

Combines all results into a list.

Sorts them by ascending price.

Prints the top 10 results neatly formatted in the console.

5. Automation (Selenium)

Uses webdriver_manager to automatically install ChromeDriver.

Opens Chrome and loads the cheapest product link.

Waits for 10 seconds, then closes the browser.

📜 Example Run
Enter product name: iphone 15 128gb
🔍 Searching Amazon...
🔍 Searching Flipkart...
🔍 Searching Croma...
🔍 Searching Reliance Digital...
🔍 Searching Google Products...

🛒 Price Comparison Results:
Amazon     | ₹78999.00 | Apple iPhone 15 (128 GB) - Blue...
Flipkart   | ₹78899.00 | Apple iPhone 15 (128 GB, Blue)...
Croma      | ₹79999.00 | Apple iPhone 15 (128 GB, Blue)...
Reliance   | ₹79999.00 | Apple iPhone 15 128 GB Blue...
Google     | ₹78500.00 | Apple iPhone 15 128GB - Various Stores...

💰 Lowest price found on Google: ₹78500.00
Opening link: https://www.google.com/shopping/product/...
