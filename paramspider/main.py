import argparse
import os
import logging
import colorama
from colorama import Fore, Style
from . import client  # Importing client from a module named "client"
from urllib.parse import urlparse, parse_qs, urlencode
import os

yellow_color_code = "\033[93m"
reset_color_code = "\033[0m"

colorama.init(autoreset=True)  # Initialize colorama for colored terminal output

log_format = '%(message)s'
logging.basicConfig(format=log_format, level=logging.INFO)
logging.getLogger('').handlers[0].setFormatter(logging.Formatter(log_format))

HARDCODED_EXTENSIONS = [
    ".jpg", ".jpeg", ".png", ".gif", ".pdf", ".svg", ".json",
    ".css", ".js", ".webp", ".woff", ".woff2", ".eot", ".ttf", ".otf", ".mp4", ".txt"
]

def has_extension(url, extensions):
    """
    Check if the URL has a file extension matching any of the provided extensions.

    Args:
        url (str): The URL to check.
        extensions (list): List of file extensions to match against.

    Returns:
        bool: True if the URL has a matching extension, False otherwise.
    """
    parsed_url = urlparse(url)
    path = parsed_url.path
    extension = os.path.splitext(path)[1].lower()

    return extension in extensions

def clean_url(url):
    """
    Clean the URL by removing redundant port information for HTTP and HTTPS URLs.

    Args:
        url (str): The URL to clean.

    Returns:
        str: Cleaned URL.
    """
    parsed_url = urlparse(url)
    
    if (parsed_url.port == 80 and parsed_url.scheme == "http") or (parsed_url.port == 443 and parsed_url.scheme == "https"):
        parsed_url = parsed_url._replace(netloc=parsed_url.netloc.rsplit(":", 1)[0])

    return parsed_url.geturl()

def clean_urls(urls, extensions, placeholder):
    """
    Clean a list of URLs by removing unnecessary parameters and query strings.

    Args:
        urls (list): List of URLs to clean.
        extensions (list): List of file extensions to check against.

    Returns:
        list: List of cleaned URLs.
    """
    cleaned_urls = set()
    for url in urls:
        cleaned_url = clean_url(url)
        if not has_extension(cleaned_url, extensions):
            parsed_url = urlparse(cleaned_url)
            query_params = parse_qs(parsed_url.query)
            cleaned_params = {key: placeholder for key in query_params}
            cleaned_query = urlencode(cleaned_params, doseq=True)
            cleaned_url = parsed_url._replace(query=cleaned_query).geturl()
            cleaned_urls.add(cleaned_url)
    return list(cleaned_urls)

def fetch_and_clean_urls(domain, extensions, stream_output,proxy, placeholder):
    """
    Fetch and clean URLs related to a specific domain from the Wayback Machine.

    Args:
        domain (str): The domain name to fetch URLs for.
        extensions (list): List of file extensions to check against.
        stream_output (bool): True to stream URLs to the terminal.

    Returns:
        None
    """
    logging.info(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Fetching URLs for {Fore.CYAN + domain + Style.RESET_ALL}")
    wayback_uri = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=txt&collapse=urlkey&fl=original&page=/"
    response = client.fetch_url_content(wayback_uri,proxy)
    urls = response.text.split()
    
    logging.info(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Found {Fore.GREEN + str(len(urls)) + Style.RESET_ALL} URLs for {Fore.CYAN + domain + Style.RESET_ALL}")
    
    cleaned_urls = clean_urls(urls, extensions, placeholder)
    logging.info(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Cleaning URLs for {Fore.CYAN + domain + Style.RESET_ALL}")
    logging.info(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Found {Fore.GREEN + str(len(cleaned_urls)) + Style.RESET_ALL} URLs after cleaning")
    logging.info(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Extracting URLs with parameters")
    
    results_dir = "results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    result_file = os.path.join(results_dir, f"{domain}.txt")

    with open(result_file, "w") as f:
        for url in cleaned_urls:
            if "?" in url:
                f.write(url + "\n")
                if stream_output:
                    print(url)
    
    logging.info(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Saved cleaned URLs to {Fore.CYAN + result_file + Style.RESET_ALL}")

def main():
    """
    Main function to handle command-line arguments and start URL mining process.
    """
    log_text = """
           
                                      _    __       
   ___  ___ ________ ___ _  ___ ___  (_)__/ /__ ____
  / _ \/ _ `/ __/ _ `/  ' \(_-</ _ \/ / _  / -_) __/
 / .__/\_,_/_/  \_,_/_/_/_/___/ .__/_/\_,_/\__/_/   
/_/                          /_/                    

                              with <3 by @0xasm0d3us           
    """
    colored_log_text = f"{yellow_color_code}{log_text}{reset_color_code}"
    print(colored_log_text)
    parser = argparse.ArgumentParser(description="Mining URLs from dark corners of Web Archives ")
    parser.add_argument("-d", "--domain", help="Domain name to fetch related URLs for.")
    parser.add_argument("-l", "--list", help="File containing a list of domain names.")
    parser.add_argument("-s", "--stream", action="store_true", help="Stream URLs on the terminal.")
    parser.add_argument("--proxy", help="Set the proxy address for web requests.",default=None)
    parser.add_argument("-p", "--placeholder", help="placeholder for parameter values", default="FUZZ")
    args = parser.parse_args()

    if not args.domain and not args.list:
        parser.error("Please provide either the -d option or the -l option.")

    if args.domain and args.list:
        parser.error("Please provide either the -d option or the -l option, not both.")

    if args.list:
        with open(args.list, "r") as f:
            domains = [line.strip().lower().replace('https://', '').replace('http://', '') for line in f.readlines()]
            domains = [domain for domain in domains if domain]  # Remove empty lines
            domains = list(set(domains))  # Remove duplicates
    else:
        domain = args.domain

    extensions = HARDCODED_EXTENSIONS

    if args.domain:
        fetch_and_clean_urls(domain, extensions, args.stream, args.proxy, args.placeholder)

    if args.list:
        for domain in domains:
            fetch_and_clean_urls(domain, extensions, args.stream,args.proxy, args.placeholder)

if __name__ == "__main__":
    main()