import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

# --- Scraper Configuration ---
# Use a common User-Agent to avoid being blocked
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

# --- Helper Function to Clean Prices ---
def clean_price(price_str):
    """Removes currency symbols, commas, and converts to float."""
    if not price_str:
        return None
    # Remove all non-digit characters except for the decimal point
    cleaned = re.sub(r'[^\d.]', '', price_str)
    try:
        return float(cleaned)
    except (ValueError, TypeError):
        return None

# --- Scraper Functions for Each Platform ---

def scrape_amazon(product_name):
    """Scrapes Amazon.com (US) for a given product."""
    print(f"Searching Amazon for '{product_name}'...")
    products = []
    search_query = product_name.replace(' ', '+')
    url = f"https://www.amazon.com/s?k={search_query}"
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        results = soup.find_all('div', {'data-component-type': 's-search-result'})
        for item in results:
            try:
                title = item.find('h2').find('a').text.strip()
                link = "https://www.amazon.com" + item.find('h2').find('a')['href']
                
                price_whole = item.find('span', 'a-price-whole')
                price_fraction = item.find('span', 'a-price-fraction')
                if price_whole and price_fraction:
                    price_str = f"{price_whole.text.strip()}{price_fraction.text.strip()}"
                    price = clean_price(price_str)
                    if price:
                        products.append({'name': title, 'price': price, 'link': link, 'source': 'Amazon', 'currency': '$'})
            except AttributeError:
                continue
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Amazon page: {e}")
    return products

def scrape_flipkart(product_name):
    """Scrapes Flipkart (India) for a given product."""
    print(f"Searching Flipkart for '{product_name}'...")
    products = []
    search_query = product_name.replace(' ', '+')
    url = f"https://www.flipkart.com/search?q={search_query}"

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Flipkart has multiple potential class names for containers
        results = soup.find_all('div', {'class': '_1AtVbE'})
        if not results:
             results = soup.find_all('div', {'class': '_4ddWXP'}) # Fallback selector

        for item in results:
            try:
                title_element = item.find('div', {'class': '_4rR01T'}) or item.find('a', {'class': 's1Q9rs'})
                price_element = item.find('div', {'class': '_30jeq3'}) or item.find('div', {'class': '_3I9_wc'})
                link_element = item.find('a', {'class': '_1fQZEK'}) or item.find('a', {'class': 's1Q9rs'})
                
                if title_element and price_element and link_element:
                    title = title_element.text.strip()
                    price = clean_price(price_element.text)
                    link = "https://www.flipkart.com" + link_element['href']
                    if price:
                        products.append({'name': title, 'price': price, 'link': link, 'source': 'Flipkart', 'currency': '₹'})
            except AttributeError:
                continue
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Flipkart page: {e}")
    return products

def scrape_croma(product_name):
    """Scrapes Croma (India) for a given product."""
    print(f"Searching Croma for '{product_name}'...")
    products = []
    search_query = product_name.replace(' ', '%20')
    url = f"https://www.croma.com/search/?q={search_query}%3Arelevance"

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        results = soup.find_all('li', class_='product-item')
        for item in results:
            try:
                title_element = item.find('h3', class_='product-title')
                price_element = item.find('span', {'data-testid': 'pdp-product-price'})
                link_element = item.find('a', class_='product-img')
                
                if title_element and price_element and link_element:
                    title = title_element.text.strip()
                    price = clean_price(price_element.text)
                    link = "https://www.croma.com" + link_element['href']
                    if price:
                        products.append({'name': title, 'price': price, 'link': link, 'source': 'Croma', 'currency': '₹'})
            except AttributeError:
                continue
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Croma page: {e}")
    return products

def scrape_reliance_digital(product_name):
    """Scrapes Reliance Digital (India) for a given product."""
    print(f"Searching Reliance Digital for '{product_name}'...")
    products = []
    search_query = product_name.replace(' ', '%20')
    url = f"https://www.reliancedigital.in/search?q={search_query}"

    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        results = soup.find_all('div', class_='sp grid')
        for item in results:
            try:
                title_element = item.find('p', class_='sp__name')
                price_element = item.find('span', class_='kCJOnt')
                link_element = item.find('a')
                
                if title_element and price_element and link_element:
                    title = title_element.text.strip()
                    price = clean_price(price_element.find('span').text)
                    link = "https://www.reliancedigital.in" + link_element['href']
                    if price:
                        products.append({'name': title, 'price': price, 'link': link, 'source': 'Reliance Digital', 'currency': '₹'})
            except AttributeError:
                continue
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Reliance Digital page: {e}")
    return products

def scrape_google_shopping(product_name):
    """Scrapes Google Shopping. Highly likely to fail due to bot protection."""
    print(f"Searching Google Shopping for '{product_name}'...")
    print("NOTE: Google Shopping often blocks scrapers. Results may be empty.")
    products = []
    search_query = product_name.replace(' ', '+')
    url = f"https://www.google.com/search?tbm=shop&q={search_query}"
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Selectors for Google are very unstable and change often
        results = soup.find_all('div', class_='sh-dgr__gr-auto')
        for item in results:
            try:
                title = item.find('h3', class_='tAxDx').text.strip()
                price_str = item.find('span', class_='a8Pemb').text.strip()
                link = "https://www.google.com" + item.find('a')['href']
                
                # Google Shopping prices can have extra text, so clean carefully
                price = clean_price(price_str.split()[0]) # Take the first part of the price string
                
                if price:
                    # Determine currency based on symbol
                    currency = '₹' if '₹' in price_str else '$'
                    products.append({'name': title, 'price': price, 'link': link, 'source': 'Google Shopping', 'currency': currency})
            except (AttributeError, IndexError):
                continue
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Google Shopping page: {e}")
    return products


def open_link_with_selenium(url):
    """Uses Selenium to open the given URL in a Chrome browser."""
    print("\nInitializing browser to open the cheapest link...")
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get(url)
        print(f"Successfully opened: {url}")
        input("Press Enter in this terminal to close the browser...")
        driver.quit()
    except Exception as e:
        print(f"An error occurred with Selenium: {e}")
        print("Please ensure you have Google Chrome installed.")

# --- Main Execution ---
if __name__ == "__main__":
    product_to_search = input("Enter the product you want to search for: ")
    
    # Scrape from all platforms
    all_products = []
    all_products.extend(scrape_amazon(product_to_search))
    all_products.extend(scrape_flipkart(product_to_search))
    all_products.extend(scrape_croma(product_to_search))
    all_products.extend(scrape_reliance_digital(product_to_search))
    all_products.extend(scrape_google_shopping(product_to_search))

    if not all_products:
        print("\nSorry, no products were found. This could be due to:")
        print("1. The product name is too specific or not available.")
        print("2. The websites blocked the scraping request (this is common).")
    else:
        # Note: Sorting works across currencies but isn't a direct comparison.
        # This will list all INR products first, then all USD products (or vice-versa).
        # A true comparison would require currency conversion.
        # For simplicity, we sort by the numeric price value.
        sorted_products = sorted(all_products, key=lambda x: x['price'])
        
        print("\n--- Search Results (Sorted by Price Value) ---")
        print("Disclaimer: Prices are shown in their local currency ($ or ₹) and are not converted.")
        for product in sorted_products:
            print(f"Source: {product['source']}")
            print(f"  Name: {product['name'][:70]}...")
            print(f"  Price: {product['currency']}{product['price']:,}") # Format with comma separators
            print(f"  Link: {product['link']}\n")
            
        cheapest_product = sorted_products[0]
        print("--- CHEAPEST OPTION (Based on numeric value, not currency conversion) ---")
        print(f"Source: {cheapest_product['source']}")
        print(f"Name: {cheapest_product['name']}")
        print(f"Price: {cheapest_product['currency']}{cheapest_product['price']:,}")
        
        open_link_with_selenium(cheapest_product['link'])
