import requests
from bs4 import BeautifulSoup
import json

# URL of the specific CVPR 2024 paper
url = "https://openaccess.thecvf.com/content/CVPR2024/html/Zeng_Unmixing_Diffusion_for_Self-Supervised_Hyperspectral_Image_Denoising_CVPR_2024_paper.html"

# Send a GET request to the website
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract title
title = soup.find('div', id='papertitle').text.strip()

# Extract authors
authors = soup.find('div', id='authors').text.strip()

# Extract abstract
abstract = soup.find('div', id='abstract').text.strip()

# Extract PDF link
pdf_link = soup.find('a', text='pdf')['href']
pdf_link = "https://openaccess.thecvf.com" + pdf_link if pdf_link else None

# Extract supplementary materials link (if available)
supp_link = soup.find('a', text='supplementary materials')
supp_link = "https://openaccess.thecvf.com" + supp_link['href'] if supp_link else None

# Store paper data in a dictionary
paper_data = {
    "title": title,
    "authors": authors,
    "abstract": abstract,
    "pdf_link": pdf_link,
    "supplementary_materials_link": supp_link
}

# Save the data to a JSON file
with open('cvpr2024_paper.json', 'w', encoding='utf-8') as json_file:
    json.dump(paper_data, json_file, indent=4, ensure_ascii=False)

print("Data extraction complete. Saved to 'cvpr2024_paper.json'.")