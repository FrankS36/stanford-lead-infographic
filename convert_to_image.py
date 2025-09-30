#!/usr/bin/env python3
"""
Script to convert the HTML infographic to high-quality image formats
Requires: pip install selenium pillow
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import io

def convert_html_to_image():
    """Convert HTML infographic to PNG and PDF formats"""
    
    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1200,2000")  # Set desired dimensions
    
    # Initialize Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    try:
        # Get the absolute path to the HTML file
        html_file = os.path.abspath("infographic.html")
        file_url = f"file://{html_file}"
        
        print(f"Loading HTML file: {file_url}")
        driver.get(file_url)
        
        # Wait for page to load
        time.sleep(3)
        
        # Get the full page height
        total_height = driver.execute_script("return document.body.scrollHeight")
        print(f"Page height: {total_height}px")
        
        # Set window size to capture full content
        driver.set_window_size(1200, total_height + 100)
        time.sleep(2)
        
        # Get the infographic element
        infographic = driver.find_element("class name", "infographic")
        
        # Take screenshot
        print("Taking screenshot...")
        screenshot = infographic.screenshot_as_png
        
        # Save as PNG
        with open("ignite6_infographic.png", "wb") as f:
            f.write(screenshot)
        print("✅ Saved as ignite6_infographic.png")
        
        # Optional: Create a PDF version
        # Note: This requires additional setup for PDF generation
        print("📄 For PDF conversion, you can:")
        print("   1. Open the HTML file in Chrome")
        print("   2. Press Ctrl+P (Cmd+P on Mac)")
        print("   3. Choose 'Save as PDF'")
        print("   4. Set margins to 'None' for best results")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nAlternative method:")
        print("1. Open 'infographic.html' in your web browser")
        print("2. Take a screenshot or use browser's print to PDF feature")
        print("3. For best quality, use browser's developer tools to set viewport size")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    print("🚀 Converting HTML infographic to image...")
    print("📋 Make sure you have installed: pip install selenium pillow webdriver-manager")
    print()
    
    try:
        convert_html_to_image()
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("📦 Install with: pip install selenium pillow webdriver-manager")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n🔄 Fallback: Open 'infographic.html' in your browser and take a screenshot")
