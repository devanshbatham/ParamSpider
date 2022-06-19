
  

## ParamSpider : Parameter miner for humans

![ParamSpider](https://raw.githubusercontent.com/devanshbatham/ParamSpider/master/static/banner.PNG)

### Key Features :

  

- Finds parameters from web archives of the entered domain.

- Finds parameters from subdomains as well.

- Gives support to exclude urls with specific extensions.

- Saves the output result in a nice and clean manner.

- It mines the parameters from web archives (without interacting with the target host)

  

### Usage instructions :

```
Note : Use python 3.7+

$ git clone https://github.com/devanshbatham/ParamSpider
$ cd ParamSpider
$ pip3 install -r requirements.txt
$ python3 paramspider.py --domain hackerone.com
```

### Run Docker :

```bash
docker build -qt paramspider . 
docker run paramspider --domain hackerone.com
```

  

### Usage options :

```
1 - For a simple scan [without the --exclude parameter]
$ python3 paramspider.py --domain hackerone.com
-> Output ex : https://hackerone.com/test.php?q=FUZZ

2 - For excluding urls with specific extensions
$ python3 paramspider.py --domain hackerone.com --exclude php,jpg,svg

3 - For finding nested parameters
$ python3 paramspider.py --domain hackerone.com --level high
-> Output ex : https://hackerone.com/test.php?p=test&q=FUZZ

4 - Saving the results
$ python3 paramspider.py --domain hackerone.com --exclude php,jpg --output hackerone.txt

5 - Using with a custom placeholder text (default is FUZZ), e.g. don't add a placeholder
$ python3 paramspider.py --domain hackerone.com --placeholder FUZZ2

6 - Using the quiet mode (without printing the URLs on screen)
$ python3 paramspider.py --domain hackerone.com --quiet

7 - Exclude subdomains [for parameters from domain+subdomains, do not specify this argument]
$ python3 paramspider.py --domain hackerone.com --subs False 
```

### ParamSpider + GF (for massive pwnage)

  

Lets say you have already installed ParamSpider and now you want to filter out the juicy parameters from plethora of parameters. No worries you can easily do it using [GF(by tomnomnom)](https://github.com/tomnomnom/gf) .

  

**Note** : Make sure you have [go](https://golang.org/doc/install) properly installed on your machine .

  

**Follow along this :**

```
$ go get -u github.com/tomnomnom/gf
$ cp -r $GOPATH/src/github.com/tomnomnom/gf/examples ~/.gf

Note : Replace '/User/levi/go/bin/gf' with the path where gf binary is located in your system.

$ alias gf='/User/levi/go/bin/gf'
$ cd ~/.gf/

Note : Paste JSON files(https://github.com/devanshbatham/ParamSpider/tree/master/gf_profiles) in ~/.gf/ folder

Now run ParamSpider and navigate to the output directory

$ gf redirect domain.txt //for potential open redirect/SSRF parameters
$ gf xss domain.txt //for potential xss vulnerable parameters
$ gf potential domain.txt //for xss + ssrf + open redirect parameters
$ gf wordpress domain.txt //for wordpress urls

[More GF profiles to be added in future]
```

  

## Example :

```
$ python3 paramspider.py --domain bugcrowd.com --exclude woff,css,js,png,svg,php,jpg --output bugcrowd.txt
```

  

![](https://raw.githubusercontent.com/devanshbatham/ParamSpider/master/static/example.PNG)

  

#### Note :

```
As it fetches the parameters from web archive data ,
so chances of false positives are high.
```

### Contributing to ParamSpider :

 - Report bugs , missing best practices 
 - Shoot my [DM](https://twitter.com/0xAsm0d3us) with new ideas 
 - Make more GF profiles (.json files)
 - Help in Fixing bugs
 - Submit Pull requests 

 
  

### My Twitter :


**Say hello** : [0xAsm0d3us](https://twitter.com/0xAsm0d3us)

  
## __Want to support my work?__
If you think my work has added some value to your existing knowledge, then you can [Buy me a Coffee here](https://www.buymeacoffee.com/Asm0d3us) (and who doesn't loves a good cup of coffee?')


[![name](https://img.buymeacoffee.com/api/?url=aHR0cHM6Ly9jZG4uYnV5bWVhY29mZmVlLmNvbS91cGxvYWRzL3Byb2ZpbGVfcGljdHVyZXMvMjAyMS8wOS8wMGU4ZGJjODc0NzI0MmRjYTJmNGJkMmMzMzQ1ODUzZC5wbmdAMzAwd18wZS53ZWJw&creator=Asm0d3us&is_creating=creating%20educational%20cybersecurity%20related%20content.&design_code=1&design_color=%235F7FFF&slug=Asm0d3us)](https://www.buymeacoffee.com/Asm0d3us)
