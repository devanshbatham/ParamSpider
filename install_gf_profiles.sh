#!/bin/bash

# https://raw.githubusercontent.com/devanshbatham/ParamSpider/master/gf_profiles/xss.json
# https://github.com/devanshbatham/ParamSpider/blob/master/gf_profiles/wordpress.json
# https://github.com/devanshbatham/ParamSpider/blob/master/gf_profiles/redirect.json
# https://github.com/devanshbatham/ParamSpider/blob/master/gf_profiles/potential.json

GF_FOLDER="$HOME/.gf/"

URLS=('https://raw.githubusercontent.com/devanshbatham/ParamSpider/master/gf_profiles/xss.json' 'https://github.com/devanshbatham/ParamSpider/blob/master/gf_profiles/wordpress.json' 'https://github.com/devanshbatham/ParamSpider/blob/master/gf_profiles/redirect.json' 'https://github.com/devanshbatham/ParamSpider/blob/master/gf_profiles/potential.json')

for I in ${URLS[@]} 
	do 
		wget ${I} -P ${GF_FOLDER} 
	done
