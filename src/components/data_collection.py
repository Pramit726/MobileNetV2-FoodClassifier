import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
import urllib

def scrape_images_for_items(item, directory, num_images_per_item, min_width=300, min_height=300):
    """
    Scrape and download images related to the specified item from Unsplash.

    Args:
        item (str): The item to search for images.
        directory (str): The directory to save the downloaded images.
        num_images_per_item (int): The number of images to download for the specified item.
        min_width (int, optional): The minimum width of the downloaded images (default is 300).
        min_height (int, optional): The minimum height of the downloaded images (default is 300).

    Returns:
        None
    """
    # Define the URL to scrape
    url = "https://unsplash.com/s/photos/{}".format(item)

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all image tags
    img_tags = soup.find_all('img')

    # Create a directory to save the images
    if not os.path.exists(directory):
        os.makedirs(directory, mode=0o755)

    # Download and save images
    downloaded_images = 0
    for i, img_tag in enumerate(img_tags):
        try:
            img_url = img_tag['src']
            img_name = "{}_{}.jpg".format(item, downloaded_images)
            img_path = os.path.join(directory, img_name)
            urllib.request.urlretrieve(img_url, img_path)

            # Check the dimensions of the downloaded image
            img = Image.open(img_path)
            width, height = img.size
            if width >= min_width and height >= min_height:
                downloaded_images += 1
                print("Image {}/{} for {} downloaded successfully".format(downloaded_images, num_images_per_item, item))

                # If the required number of images is reached, break the loop
                if downloaded_images == num_images_per_item:
                    break
            else:
                # Delete the image if it does not meet the size requirements
                os.remove(img_path)
        except Exception as e:
            print("Error downloading image {} for {}: {}".format(downloaded_images + 1, item, e))