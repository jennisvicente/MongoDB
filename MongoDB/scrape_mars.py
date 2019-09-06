from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scraper():
    browser = init_browser()
    mars_w = []
    Mars_dict = {}
    #Urls
    url1="https://mars.nasa.gov/news/"
    url2= "https://twitter.com/marswxreport?lang=en"
    facts_url ="https://space-facts.com/mars/"
    
    #Mars NASA
    
    
    browser.visit(url1)
    html1 = browser.html
    soup1 = BeautifulSoup(html1, 'html.parser')
    
    
    #Twitter Weather
    
    browser.visit(url2)
    html2 = browser.html
    soup2 = BeautifulSoup(html2, 'html.parser')

    
    timeline = soup2.select('#timeline li.stream-item')
    for tweet in timeline:
      # tweet_id = tweet['data-item-id']
      tweet_text = tweet.select('p.tweet-text')[0].get_text()
      mars_w.append(tweet_text) 
      mars_weather=mars_w[0]
      
    #Pandas Scrape
      
      browser.visit(facts_url)
      tables = pd.read_html(facts_url)
      df = tables[1]
      df.columns = ['Facts','Mars']
      df.set_index('Facts', inplace=True)
      df.to_html('mars_facts.html')
    
    #Featured image
    feature_img_url="https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA09320_ip.jpg)"
    
    #Hemispheres
      hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"}
]

    
      Mars_dict["Latest title"] = soup1.find("div", class_="content_title").text
      Mars_dict["news_p"] = soup1.find('div', class_='rollover_description').text
      Mars_dict["tweet_text"]=mars_weather
      Mars_dict["feature_img"]=feature_img_url  
      Mars_dict["hemispheres"]= hemisphere_image_urls
        
      return Mars_dict
      
      