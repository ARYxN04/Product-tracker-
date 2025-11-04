
# India Price Comparator

## Introduction

**India Price Comparator** is a Python-based web scraper and automation tool that helps users find the **best prices** for products across multiple Indian e-commerce platforms.  
By integrating **BeautifulSoup** for web scraping and **Selenium** for browser automation, the tool provides real-time comparison and automatically opens the **lowest-priced product** link in the browser.

It is ideal for **tech enthusiasts**, **developers**, or **bargain hunters** who want to quickly compare prices without manually checking each website.

---

## Features

The India Price Comparator offers a streamlined, automated way to find the best deal:

### 1. **Multi-Platform Search**
- Searches across top Indian e-commerce websites:
  - Amazon India  
  - Flipkart  
  - Croma  
  - Reliance Digital  
  - Google Shopping  

### 2. **Web Scraping & Data Extraction**
- Uses **BeautifulSoup4** to extract product names, prices, and links  
- Automatically cleans and normalizes prices (e.g., “₹12,999” → `12999.0`)  
- Ignores incomplete or invalid data  

### 3. **Price Comparison Engine**
- Merges and sorts all collected results by price  
- Displays a formatted list of the **top 10 cheapest listings**  
- Highlights the **lowest available price**  

### 4. **Automated Link Opening**
- Uses **Selenium WebDriver** to open the link with the best deal  
- Automatically installs and manages the correct ChromeDriver version  
- Opens the page in Chrome and closes it after a short delay  

### 5. **Extensible Design**
- Modular functions for each website (easy to add new stores)  
- Clean structure for future enhancements such as:
  - Headless browsing  
  - CSV export  
  - Parallel scraping  

---

## Tech Stack

- **Python 3.8+** – Core programming language  
- **BeautifulSoup4** – For parsing and scraping web content  
- **Requests** – For making HTTP requests  
- **Selenium** – For automating the browser and opening links  
- **WebDriver Manager** – Automatically manages ChromeDriver versions  

---

## Screenshots

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
<img width="600" height="300" alt="Console Output" src="https://github.com/user-attachments/assets/b4a4726e-3b59-4c54-a331-0479d19d9e6a" />
<img width="600" height="300" alt="Selenium Automation" src="https://github.com/user-attachments/assets/61c6532b-4d4a-4b74-9a34-2f17c2a7f6e3" />
</div>

---

## Architecture

The project follows a **modular procedural architecture** for clarity and extensibility:

- **`search_amazon()`** – Scrapes Amazon India search results  
- **`search_flipkart()`** – Extracts product info from Flipkart  
- **`search_croma()`** – Parses product listings from Croma  
- **`search_reliance()`** – Fetches items from Reliance Digital  
- **`search_google_products()`** – Collects results from Google Shopping  
- **`clean_price()`** – Utility function for price normalization  
- **`main()`** – Combines results, sorts by price, displays output, and automates browser navigation  

---

## Getting Started

### Prerequisites
- **Python 3.8 or higher**
- **Google Chrome browser**
- Stable **Internet connection**

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd india-price-comparator
```

2. Install dependencies:
```bash
pip install requests beautifulsoup4 selenium webdriver-manager
```

3. Run the program:
```bash
python india_price_comparator.py
```

---

## Example Output

```
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
```

---

## Contributing Guidelines

We welcome community contributions to improve the scraper, add new stores, or enhance features.

### How to Contribute

1. **Fork the repository**  
2. **Create a feature branch:**  
   ```bash
   git checkout -b feature/new-store-support
   ```
3. **Implement your changes** following clean code standards  
4. **Test your scraper** with multiple product names  
5. **Commit your changes** with clear messages  
6. **Push and open a Pull Request**

### Code Style Guidelines
- Follow **PEP8 Python coding standards**  
- Use **meaningful variable names**  
- Write **docstrings** for functions  
- Ensure all scrapers **return consistent tuple formats**:  
  `(Platform, Product Title, Price, Link)`  
- Handle missing or invalid data gracefully  

### Pull Request Process
- Confirm that your code runs without errors  
- Include documentation updates for new features  
- Mention any dependencies or external tools used  

---

## Future Enhancements

| Feature | Description |
|----------|--------------|
| 🕶️ Headless Selenium | Run without opening browser windows |
| 💾 CSV Export | Save all price results in a structured file |
| ⚡ Async Scraping | Faster results using `aiohttp` |
| 🧩 GUI Interface | Build a user-friendly desktop interface |
| 🔁 Proxy Support | Prevent IP rate-limiting on multiple requests |

---

## License

This project is released for **educational and personal use**.  
Unauthorized commercial scraping of websites may violate their **Terms of Service**.  
Always verify site permissions before large-scale data extraction.

---

## Acknowledgments

- **BeautifulSoup** and **Selenium** communities for powerful open-source tools  
- **E-commerce platforms** for making product data accessible  
- **Developers & Contributors** who improve open-source automation projects  

---

**Built with ❤️ by [Aryan Badola](https://github.com/aryan-badola)**  
