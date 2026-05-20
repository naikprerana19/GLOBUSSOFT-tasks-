import requests
from bs4 import BeautifulSoup
import pandas as pd

# Amazon URL
url = "https://www.amazon.in/s?k=laptops"

# Headers
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9"
}

# Send request
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.content, "html.parser")

# Find all products
products = soup.find_all("div", {"data-component-type": "s-search-result"})

# Store data
data = []

for product in products:

    # Title
    title_tag = product.find("h2")
    title = title_tag.text.strip() if title_tag else "N/A"

    # Price
    price_tag = product.find("span", class_="a-price-whole")
    price = price_tag.text.strip() if price_tag else "N/A"

    # Rating
    rating_tag = product.find("span", class_="a-icon-alt")
    rating = rating_tag.text.strip() if rating_tag else "N/A"

    # Image
    image_tag = product.find("img")
    image = image_tag["src"] if image_tag else "N/A"

    # Ad or Organic
    ad_text = "Ad" if "Sponsored" in product.text else "Organic"

    # Append data
    data.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Image": image,
        "Ad/Organic": ad_text
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save CSV
df.to_csv("amazon_laptops.csv", index=False)

# Show output
print(df.head())

print("EXL File Saved Successfully!")
