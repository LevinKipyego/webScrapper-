import requests
from bs4 import BeautifulSoup
from icecream import ic
import os

# URL of the web page containing the images
url = "https://www.google.com/search?client=opera-gx&hs=OY0&sca_esv=383ef31e719fe62f&sca_upv=1&q=ankole+cattle&uds=AMwkrPuChM3QNXggeGrmIi9L-QtMzlkpdJAOTA2Mbk_cVAFRgn0Yb2ZIfhuaYgrR43Z_8J5QFuKTR5C4xXrn7JJZEW6FzasTzDa1ppXa_a7ths9cq2_cKaUT8NPsF569XmhacdwOn4qpC5-h28GuvStVs_v7XBPfZNd9jcPe_7Huyj-THluHFJlx3eV7bFZ5eFc10lfCIl4Aa6BVdTQLjhtsnvqQDAI3QbR7lRZwCdXROXeudT5TlbIrv5jmaz9ud727rYPUntyS&udm=2&prmd=vismbz&sa=X&ved=2ahUKEwjTl8SykbiFAxWYnP0HHQDSCa8QtKgLegQIDBAB&biw=757&bih=787"
# Send an HTTP GET request to fetch the web page content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')



# Find all image elements on the page
images = soup.find_all('img')

# Directory to save downloaded images
download_dir = r"C:\Users\levyt\Downloads\ankole_cattle"

# Download each image to the specified directory
for index, image in enumerate(images):
    image_url = image['src']
    if image_url == '/images/branding/searchlogo/1x/googlelogo_desk_heirloom_color_150x55dp.gif':
        continue
    
    ic(image_url)
    # Implement logic to download the image using urllib or requests library
    # Save the image to the specified directory
    image_data = requests.get(image_url).content
    ic(image_data)
    
    with open(os.path.join(download_dir, f'image_{index}.jpeg'), 'wb') as f:
        f.write(image_data)

