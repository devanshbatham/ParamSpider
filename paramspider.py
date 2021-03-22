#!/usr/bin/env python3
from core import requester
from core import extractor
from core import save_it
from urllib.parse import unquote 
import requests
import re
import argparse
import os
import sys
import time 
start_time = time.time()


def main():
    if os.name == 'nt':
        os.system('cls')
    banner = """\u001b[36m

         ___                               _    __       
        / _ \___ ________ ___ _  ___ ___  (_)__/ /__ ____
       / ___/ _ `/ __/ _ `/  ' \(_-</ _ \/ / _  / -_) __/
      /_/   \_,_/_/  \_,_/_/_/_/___/ .__/_/\_,_/\__/_/   
                                  /_/     \u001b[0m               
                            
                           \u001b[32m - coded with <3 by Devansh Batham\u001b[0m 
    """
    print(banner)

    parser = argparse.ArgumentParser(description='ParamSpider a parameter discovery suite')
    parser.add_argument('-d','--domain' , help = 'Domain name of the taget [ex : hackerone.com]' , required=True)
    parser.add_argument('-s' ,'--subs' , help = 'Set False for no subs [ex : --subs False ]' , default=True)
    parser.add_argument('-l','--level' ,  help = 'For nested parameters [ex : --level high]')
    parser.add_argument('-e','--exclude', help= 'extensions to exclude [ex --exclude php,aspx]')
    parser.add_argument('-o','--output' , help = 'Output file name [by default it is \'domain.txt\']')
    parser.add_argument('-p','--placeholder' , help = 'The string to add as a placeholder after the parameter name.', default = "FUZZ")
    parser.add_argument('-q', '--quiet', help='Do not print the results to the screen', action='store_true')
    parser.add_argument('-r', '--retries', help='Specify number of retries for 4xx and 5xx errors', default=3)
    args = parser.parse_args()

    if args.subs == True or " True":
        url = f"https://web.archive.org/cdx/search/cdx?url=*.{args.domain}/*&output=txt&fl=original&collapse=urlkey&page=/"
    else:
        url = f"https://web.archive.org/cdx/search/cdx?url={args.domain}/*&output=txt&fl=original&collapse=urlkey&page=/"
    
    retry = True
    retries = 0
    while retry == True and retries <= int(args.retries):
             response, retry = requester.connector(url)
             retry = retry
             retries += 1
    if response == False:
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
             
    else: 
         black_list = [] # for blacklists
    if args.exclude:
        print(f"\u001b[31m[!] URLS containing these extensions will be excluded from the results   : {black_list}\u001b[0m\n")
    
    final_uris = extractor.param_extract(response , args.level , black_list, args.placeholder)
    save_it.save_func(final_uris , args.output , args.domain)

    if not args.quiet:
        print("\u001b[32;1m")
        print('\n'.join(final_uris))
        print("\u001b[0m")

    print(f"\n\u001b[32m[+] Total number of retries:  {retries-1}\u001b[31m")
    print(f"\u001b[32m[+] Total unique urls found : {len(final_uris)}\u001b[31m")
    if args.output:
        if "/" in args.output:
            print(f"\u001b[32m[+] Output is saved here :\u001b[31m \u001b[36m{args.output}\u001b[31m" )

        else:
            print(f"\u001b[32m[+] Output is saved here :\u001b[31m \u001b[36moutput/{args.output}\u001b[31m" )
    else:
        print(f"\u001b[32m[+] Output is saved here   :\u001b[31m \u001b[36moutput/{args.domain}.txt\u001b[31m")
    print("\n\u001b[31m[!] Total execution time      : %ss\u001b[0m" % str((time.time() - start_time))[:-12])




if __name__ == "__main__":
    main()
    
