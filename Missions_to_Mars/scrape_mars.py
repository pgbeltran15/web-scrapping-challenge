def scrape():
    mars_info = []
    # Dependencies
    from bs4 import BeautifulSoup
    import requests
    import pymongo
    from splinter import Browser
    import pandas as pd

    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    #Windows users
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #Mac users
    # executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    # browser = Browser('chrome', **executable_path, headless=False)

    #NASA Scrapping

    #NASA URL
    NASA_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(NASA_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('div', class_='list_text')
    results

    #List of articles
    for result in results:
        title= result.find('div', class_="content_title")
        text = result.find('div', class_='article_teaser_body')
        date= result.find('div',class_='list_date')
        article_url= result.find('a')['href']
        print('-----------')
        print(title)
        print(text)
        print(date)
        print(NASA_url + article_url)
        

    #Store latest article in dictionary
    news_title = []
    news_p =[]
    news_date = []

    title= result.find('div', class_="content_title")
    text = result.find('div', class_='article_teaser_body')
    date= result.find('div',class_='list_date')
    article_url= result.find('a')['href']

    news_title.append(title)
    news_p.append(text)
    news_date.append(date)

    #JPL Mars Space Images Scrapping
    JPL_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(JPL_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    images = soup.find_all('div', class_='carousel_container')
    images

    img_url = image.find('article')['style']
    img_url = img_url.split("'")[1]
    img_url = img_url.split("'")[0]
    featured_img_url= 'https://www.jpl.nasa.gov/'+ img_url
    print(featured_img_url)

    #Mars Facts Scrapping
    mars_facts_url = 'https://space-facts.com/mars/'

    table= pd.read_html(mars_facts_url)
    df = tables[0]
    df.columns=['Facts','Info']
    df.to_html('mars_facts.html')

    #Mars Hemispheres Scrapping
    hemisphere_image_urls = []

    #cerberus hemisphere
    cerberus_hemisphere_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    response = requests.get(cerberus_hemisphere_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    cerberus = soup.find('li')
    img_url = cerberus.find('a')['href']
    cerberus_hemisphere = {'title': title, 'img_url':img_url}
    hemisphere_image_urls.append(cerberus_hemisphere)

    #schiaparelli hemisphere
    schiaparelli_hemisphere_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    response = requests.get(schiaparelli_hemisphere_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    schiaparelli = soup.find('li')
    img_url = schiaparelli.find('a')['href']
    schiaparelli_hemisphere = {'title': title, 'img_url':img_url}
    hemisphere_image_urls.append(schiaparelli_hemisphere)


    #sytris major hemisphere
    sytris_major_hemisphere_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    response = requests.get(sytris_major_hemisphere_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    sytris_major = soup.find('li')
    img_url = sytris_major.find('a')['href']
    sytris_major_hemisphere = {'title': title, 'img_url':img_url}
    hemisphere_image_urls.append(sytris_major_hemisphere)


    # Valles Marineris hemisphere
    valles_marineris_hemisphere_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    response = requests.get(valles_marineris_hemisphere_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    valles_marineris = soup.find('li')
    img_url = valles_marineris.find('a')['href']
    valles_marineris_hemisphere = {'title': title, 'img_url':img_url}
    hemisphere_image_urls.append(valles_marineris_hemisphere)

    hemisphere_image_urls

    mars_info.append(news_title)
    mars_info.append(news_p)
    mars_info.append(featured_img_url)
    mars_info.append(mars_facts_url)
    mars_info.append(hemisphere_image_urls)
    
    return mars_info

scrape()
