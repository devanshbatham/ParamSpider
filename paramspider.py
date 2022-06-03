#!/usr/bin/env python3
from core import requester
from core import extractor
from core import save_it
from urllib.parse import unquote
import argparse
import os
import time
import colorama
from colorama import Fore

start_time = time.time()

colorama.init()

RED = Fore.RED
GREEN = Fore.GREEN
LIGHTGREEN = Fore.LIGHTGREEN_EX
BLUE = Fore.BLUE
GREEN = Fore.GREEN
CYAN = Fore.CYAN
RESET = Fore.RESET


def clear_screen():
    """Clears the screen"""
    if os.name == "nt":  # for windows
        os.system("cls")
    else:  # for linux
        os.system("clear")


def print_banner():
    """Prints the banner"""
    banner = f"""{CYAN}

         ___                               _    __       
        / _ \___ ________ ___ _  ___ ___  (_)__/ /__ ____
       / ___/ _ `/ __/ _ `/  ' \(_-</ _ \/ / _  / -_) __/
      /_/   \_,_/_/  \_,_/_/_/_/___/ .__/_/\_,_/\__/_/   
                                  /_/     {RESET}               
                            
                           {GREEN} - coded with <3 by Devansh Batham{RESET} 
    """
    print(banner)


def get_args():
    """Get arguments from the user"""
    parser = argparse.ArgumentParser(
        description="ParamSpider a parameter discovery suite"
    )
    parser.add_argument(
        "-d",
        "--domain",
        help="Domain name of the taget [ex : hackerone.com]",
        required=True,
    )
    parser.add_argument(
        "-s",
        "--subs",
        help="Set False for no subs [ex : --subs False ]",
        default="True",
        choices=["True", "False"],
    )
    parser.add_argument(
        "-l", "--level", help="For nested parameters [ex : --level high]"
    )
    parser.add_argument(
        "-e", "--exclude", help="extensions to exclude [ex --exclude php,aspx]"
    )
    parser.add_argument(
        "-o", "--output", help="Output file name [by default it is 'domain.txt']"
    )
    parser.add_argument(
        "-p",
        "--placeholder",
        help="The string to add as a placeholder after the parameter name.",
        default="FUZZ",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        help="Do not print the results to the screen",
        action="store_true",
    )
    parser.add_argument(
        "-r",
        "--retries",
        help="Specify number of retries for 4xx and 5xx errors",
        default=3,
    )

    return parser.parse_args()


def main():
    clear_screen()
    print_banner()

    args = get_args()

    if args.subs == "True":
        url = f"https://web.archive.org/cdx/search/cdx?url=*.{args.domain}/*&output=txt&fl=original&collapse=urlkey&page=/"
    else:
        url = f"https://web.archive.org/cdx/search/cdx?url={args.domain}/*&output=txt&fl=original&collapse=urlkey&page=/"

    retry = True
    retries = 0
    while retry and retries <= int(args.retries):
        response, retry = requester.connector(url)
        retries += 1
    if not response:
        return
    response = unquote(response)

    # for extensions to be excluded
    black_list = []
    if args.exclude:
        if "," in args.exclude:
            black_list = args.exclude.split(",")
            for i in range(len(black_list)):
                black_list[i] = "." + black_list[i]
        else:
            black_list.append("." + args.exclude)

        print(
            f"{RED}[!] URLS containing these extensions will be excluded from the results   : {black_list}{RESET}\n"
        )

    final_uris = extractor.param_extract(
        response, args.level, black_list, args.placeholder
    )
    save_it.save_func(final_uris, args.output, args.domain)

    if not args.quiet:
        print(LIGHTGREEN)
        print("\n".join(final_uris))
        print(RESET)

    print(f"\n{GREEN}[+] Total number of retries:  {retries-1}{RED}")
    print(f"{GREEN}[+] Total unique urls found : {len(final_uris)}{RED}")
    if args.output:
        if "/" in args.output:
            print(f"{GREEN}[+] Output is saved here :{RED} {CYAN}{args.output}{RED}")

        else:
            print(
                f"{GREEN}[+] Output is saved here :{RED} {CYAN}output/{args.output}{RED}"
            )
    else:
        print(
            f"{GREEN}[+] Output is saved here   :{RED} {CYAN}output/{args.domain}.txt{RED}"
        )
    print(
        f"\n{RED}[!] Total execution time      : {str((time.time() - start_time))[:-12]}s{RESET}"
    )


if __name__ == "__main__":
    main()
