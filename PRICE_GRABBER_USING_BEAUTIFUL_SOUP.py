import bs4, requests


# function that returns a price once you pass productURL
def getAmazonPrice(productURL):
    # added some headers so Amazon will think I'm using a browser to connect.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    req = requests.get(productURL, headers=headers)

    try:
        req.raise_for_status()
    except:
        print("There was an error grabbing the url, here is status code " + str(req.status_code))

    soup = bs4.BeautifulSoup(req.text, 'html.parser')

    listOfElements = soup.select('#priceblock_ourprice')

    # strip takes out spaces
    return listOfElements[0].text.strip()


# main method
price = getAmazonPrice("https://www.amazon.ca/dp/B076FZ7VJ2")

print("The price is " + price)
