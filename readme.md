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

### My Twitter :

**Say hello** : [0xAsm0d3us](https://twitter.com/0xAsm0d3us)

### Wanna show support for the tool ?

**I will be more than happy if you will show some love for Animals by donating to [Animal Aid Unlimited](https://animalaidunlimited.org/)** **,Animal Aid Unlimited saves animals through street animal rescue, spay/neuter and education. Their mission is dedicated to the day when all living beings are treated with compassion and love.** ✨
