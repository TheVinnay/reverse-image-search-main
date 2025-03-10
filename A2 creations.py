import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to set up proxy (optional)
def set_proxy():
    # Setup for ChromeDriver with a proxy, optional
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # To run Chrome in headless mode (no UI)
    
    # Specify the location of ChromeDriver
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Scrape data from Noon
def scrape_noon_data():
    url = "https://www.noon.com/ween/sports-and-outdoors/exercise-and-fitness/yoga-15328/"
    driver = set_proxy()
    driver.get(url)

    products = []
    
    while len(products) < 200:
        # Extract page source with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Find product containers (adjust this class based on site structure)
        product_containers = soup.find_all('div', class_='productContainer')  # Adjust based on actual HTML structure

        for item in product_containers:
            try:
                name = item.find('h3', class_='product-name').text.strip()
                price = item.find('div', class_='price').text.strip()
                brand = item.find('div', class_='brand').text.strip()
                seller = item.find('div', class_='seller').text.strip()
                url = item.find('a')['href']
                products.append([name, price, brand, seller, url])
            except AttributeError:
                continue

        # Click on the next page button for pagination (XPath might vary)
        try:
            next_button = driver.find_element(By.XPATH, '//button[@class="next-btn"]')
            next_button.click()
            time.sleep(random.uniform(2, 5))  # Random delay to mimic human behavior
        except:
            break

    driver.quit()
    
    # Save data to a DataFrame
    df = pd.DataFrame(products, columns=['Product Name', 'Price', 'Brand', 'Seller', 'URL'])
    df['Date Scraped'] = pd.to_datetime('now').date()
    
    return df

# Export to CSV
df = scrape_noon_data()
df.to_csv('noon_yoga_products.csv', index=False)

# Data Analysis
def analyze_data(df):
    # Most expensive product
    most_expensive = df.loc[df['Price'].idxmax()]
    print("Most expensive product:", most_expensive)

    # Cheapest product
    cheapest = df.loc[df['Price'].idxmin()]
    print("Cheapest product:", cheapest)

    # Number of products by brand
    brand_count = df['Brand'].value_counts()
    
    # Number of products by seller
    seller_count = df['Seller'].value_counts()

    # Plotting the number of products by brand
    plt.figure(figsize=(10, 5))
    sns.barplot(x=brand_count.index, y=brand_count.values)
    plt.xticks(rotation=90)
    plt.title("Number of Products by Brand")
    plt.show()

    # Plotting the number of products by seller
    plt.figure(figsize=(10, 5))
    sns.barplot(x=seller_count.index, y=seller_count.values)
    plt.xticks(rotation=90)
    plt.title("Number of Products by Seller")
    plt.show()

# Analyze the data
analyze_data(df)