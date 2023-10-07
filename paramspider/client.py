import requests
import logging
import time
import sys
from fake_useragent import UserAgent

logging.basicConfig(level=logging.INFO)

MAX_RETRIES = 3
user_agent = UserAgent()

def fetch_url_content(url, proxy):
    """
    Fetches the content of a URL using a random user agent.
    Retries up to MAX_RETRIES times if the request fails.
    """
    if proxy is not None:
        proxy = {
            'http': proxy,
            'https': proxy
        }
    for i in range(MAX_RETRIES):
        headers = {
            "User-Agent": user_agent.random
        }

        try:
            response = requests.get(url, proxies=proxy, headers=headers)
            response.raise_for_status()
            return response
        except (requests.exceptions.RequestException, ValueError):
            logging.warning(f"Error fetching URL {url}. Retrying in 5 seconds...")
            time.sleep(5)
        except KeyboardInterrupt:
            logging.warning("Keyboard Interrupt received. Exiting gracefully...")
            sys.exit()

    logging.error(f"Failed to fetch URL {url} after {MAX_RETRIES} retries.")
    sys.exit()
