# WEB PARSER BeautifulSoup

## Preprocess Text Clean
import requests
from bs4 import BeautifulSoup

def clean_text(text):
    """
    Clean the text by removing extra whitespace and unwanted artifacts.
    """
    # Replace multiple spaces with a single space
    return ' '.join(text.split())


## Extract Text
def extract_text(url, method="beautifulsoup"):
    """
    Extracts and cleans text from the given URL using the specified method.
    Supported methods: "beautifulsoup"
    """
    if method == "beautifulsoup":
        return extract_text_bs4(url)
    else:
        return "Unsupported extraction method specified."

## Example Usage
if __name__ == "__main__":
    # Example URL
    url = "https://championstactics.ubisoft.com/items/champions/4197"
    
    # Extract text using the unified extractor
    extracted_text = extract_text(url, method="beautifulsoup")
    print(f"Extracted Text:\n{extracted_text}")
