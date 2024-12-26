# scraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from datetime import datetime
import uuid
import pymongo
from pymongo import MongoClient
import time
from config import *

class TwitterScraper:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client['twitter_trends']
        self.collection = self.db['trends']

    # In scraper.py, update the setup_driver method:
    def setup_driver(self):
        options = webdriver.ChromeOptions()
        
        # Add additional options for better stability
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--start-maximized')
        
        # Don't use executable_path anymore as it's deprecated
        driver = webdriver.Chrome(options=options)
        return driver

    def login_to_twitter(self, driver):
        try:
            # Go to Twitter login page
            driver.get('https://x.com/i/flow/login')
            time.sleep(5)  # Wait for page to fully load
            
            print("Attempting to login...")
            
            # Wait for and enter username
            username_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]'))
            )
            username_input.clear()
            username_input.send_keys(TWITTER_USERNAME)
            print("Username entered...")
            
            # Click Next button
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']"))
            )
            next_button.click()
            print("Clicked next...")
            
            time.sleep(3)
            
            # Enter password
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
            )
            password_input.clear()
            password_input.send_keys(TWITTER_PASSWORD)
            print("Password entered...")
            
            # Click Login button
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']"))
            )
            login_button.click()
            print("Clicked login...")
            
            # Wait for login to complete
            time.sleep(5)
            
        except TimeoutException as e:
            print(f"Timeout during login: {str(e)}")
            raise
        except Exception as e:
            print(f"Error during login: {str(e)}")
            raise

    def get_trending_topics(self):
        driver = None
        try:
            driver = self.setup_driver()
            print("Driver setup complete...")
            
            self.login_to_twitter(driver)
            print("Login complete...")
            
            # Wait for home page to load
            time.sleep(10)
            #dhruv156328@gmail.com
            # Update the trends section finder in get_trending_topics():
            print("Looking for trends section...")

            # Get trends with more robust selector
            trends = []
            # First find the What's happening section
            trends_section = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Timeline: Trending now"]'))
            )

            # Get all trend elements with a more inclusive selector
            trend_elements = trends_section.find_elements(By.CSS_SELECTOR, '[data-testid="trend"]')
            processed_trends = 0

            for trend_element in trend_elements:
                if processed_trends >= 5:  # Stop after getting 5 trends
                    break
                    
                try:
                    # Try multiple selectors to get the trend text
                    trend_text = None
                    
                    # First try to find the text in the main trend div
                    trend_spans = trend_element.find_elements(By.CSS_SELECTOR, 'span[dir="ltr"]')
                    for span in trend_spans:
                        text = span.text.strip()
                        if text and not text.startswith("Trending"):
                            trend_text = text
                            break
                            
                    if not trend_text:
                        # Fallback to looking in div if span doesn't work
                        trend_divs = trend_element.find_elements(By.CSS_SELECTOR, 'div[dir="ltr"]')
                        for div in trend_divs:
                            text = div.text.strip()
                            if text and not text.startswith("Trending"):
                                trend_text = text
                                break
                    
                    if trend_text:
                        print(f"Found trend: {trend_text}")
                        trends.append(trend_text)
                        processed_trends += 1
                        
                except Exception as e:
                    print(f"Error extracting trend: {str(e)}")
                    continue

            # Fill remaining slots if we couldn't get 5 trends
            while len(trends) < 5:
                trends.append("Unable to fetch trend")

            print(f"Found {len(trends)} trends...")
            
            # Get IP (without proxy for testing)
            ip_address = "127.0.0.1"  # For testing
            
            # Create record
            record = {
                '_id': str(uuid.uuid4()),
                'nameoftrend1': trends[0] if len(trends) > 0 else "N/A",
                'nameoftrend2': trends[1] if len(trends) > 1 else "N/A",
                'nameoftrend3': trends[2] if len(trends) > 2 else "N/A",
                'nameoftrend4': trends[3] if len(trends) > 3 else "N/A",
                'nameoftrend5': trends[4] if len(trends) > 4 else "N/A",
                'timestamp': datetime.now(),
                'ip_address': ip_address
            }
            
            # Store in MongoDB
            self.collection.insert_one(record)
            return record

        except Exception as e:
            print(f"Error in get_trending_topics: {str(e)}")
            raise

        finally:
            if driver:
                driver.quit()