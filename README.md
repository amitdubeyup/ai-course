# Hyperspectral Image Denoising and Instagram Image Downloader

## Overview

This repository contains two main scripts:

1. `beautiful_soup.py`: A script to scrape and save details of a CVPR 2024 paper on hyperspectral image denoising.
2. `download_instagram_images.py`: A script to download public images from an Instagram profile.

## Files

- `beautiful_soup.py`: Uses BeautifulSoup to scrape the title, authors, abstract, and PDF link of a specific CVPR 2024 paper and saves the data in `cvpr2024_paper.json`.
- `download_instagram_images.py`: Uses Instaloader to download all public images from a specified Instagram profile.
- `cvpr2024_paper.json`: Contains the scraped data of the CVPR 2024 paper.
- `grapeot_images/`: Directory containing downloaded Instagram images.
- `LICENSE`: MIT License for the repository.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Usage

### Scraping CVPR 2024 Paper Details

1. Ensure you have the required libraries installed:
    ```sh
    pip install requests beautifulsoup4
    ```
2. Run the script:
    ```sh
    python beautiful_soup.py
    ```
3. The details of the paper will be saved in `cvpr2024_paper.json`.

### Downloading Instagram Images

1. Ensure you have the required library installed:
    ```sh
    pip install instaloader
    ```
2. Replace the `username` variable in `download_instagram_images.py` with the target Instagram username.
3. Run the script:
    ```sh
    python download_instagram_images.py
    ```
4. The images will be downloaded to a directory named `<username>_images`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.