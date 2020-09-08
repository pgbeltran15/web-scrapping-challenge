from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    
    #NASA Scrapping

    #NASA URL
    NASA_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    # Retrieve page with the requests module
    response = requests.get(NASA_url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'html.parser')

    news_title= soup.find('div', class_="content_title").text
    news_p = soup.find('div', class_='rollover_description_inner').text

    #JPL Mars Space Images Scrapping
    JPL_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(JPL_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    img_url = soup.find('article')['style']
    img_url = img_url.split("'")[1]
    img_url = img_url.split("'")[0]
    featured_img_url= 'https://www.jpl.nasa.gov/'+ img_url

    # Close the browser after scraping
    browser.quit()

    #Mars Facts Scrapping
    mars_facts_url = 'https://space-facts.com/mars/'

    table = pd.read_html(mars_facts_url)
    df = table[0]
    df.columns=['Facts','Info']
    df.to_html('mars_facts.html')
    # mars_facts= pd.read_html('mars_facts.html')
    mars_facts= df.to_html('mars_facts.html')

    #Mars Hemispheres Scrapping
    hemisphere_image = []

    #cerberus hemisphere
    cerberus_hemisphere_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    response = requests.get(cerberus_hemisphere_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    cerberus = soup.find('li')
    img_url = cerberus.find('a')['href']
    cerberus_hemisphere = {'title': title, 'img_url':img_url}
    hemisphere_image.append(cerberus_hemisphere)

    #schiaparelli hemisphere
    schiaparelli_hemisphere_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    response = requests.get(schiaparelli_hemisphere_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    schiaparelli = soup.find('li')
    img_url = schiaparelli.find('a')['href']
    schiaparelli_hemisphere = {'title': title, 'img_url':img_url}
    hemisphere_image.append(schiaparelli_hemisphere)

    #sytris major hemisphere
    sytris_major_hemisphere_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    response = requests.get(sytris_major_hemisphere_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    sytris_major = soup.find('li')
    img_url = sytris_major.find('a')['href']
    sytris_major_hemisphere = {'title': title, 'img_url':img_url}
    hemisphere_image.append(sytris_major_hemisphere)

    # Valles Marineris hemisphere
    valles_marineris_hemisphere_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    response = requests.get(valles_marineris_hemisphere_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    valles_marineris = soup.find('li')
    img_url = valles_marineris.find('a')['href']
    valles_marineris_hemisphere = {'title': title, 'img_url':img_url}
    hemisphere_image.append(valles_marineris_hemisphere)

    mars_data={
       'news_title': news_title,
       'news_p': news_p,
       'featured_img_url': featured_img_url,
       'mars_facts': mars_facts,
       'hemisphere_image': hemisphere_image
    }
    
    return mars_data

scrape()
