<h1 align="center">
    paramspider
  <br>
</h1>

<h4 align="center">  Mining URLs from dark corners of Web Archives for bug hunting/fuzzing/further probing </h4>

<p align="center">
  <a href="#about">📖 About</a> •
  <a href="#installation">🏗️ Installation</a> •
  <a href="#usage">⛏️ Usage</a> •
  <a href="#examples">🚀 Examples</a> •
  <a href="#contributing">🤝 Contributing</a> •
</p>


![paramspider](https://github.com/devanshbatham/ParamSpider/blob/master/static/paramspider.png?raw=true)

## About

`paramspider` allows you to fetch URLs related to any domain or a list of domains from Wayback achives. It filters out "boring" URLs, allowing you to focus on the ones that matter the most.

## Installation

To install `paramspider`, follow these steps:

```sh
git clone https://github.com/devanshbatham/paramspider
cd paramspider
pip install .
```

On Linux you can also use [OTinstaller](https://github.com/OSINTVerseHQ/OTinstaller), a third-party tool manager that installs `paramspider` from this repository into its own virtualenv. It isn't maintained here, so please report problems with it [on the OTinstaller tracker](https://github.com/OSINTVerseHQ/OTinstaller/issues).

```sh
pipx install otinstaller
otinstaller init
otinstaller install paramspider
otinstaller run paramspider -- d:example.com   # same as paramspider -d example.com
```

## Usage

To use `paramspider`, follow these steps:

```sh
paramspider -d example.com
```

## Examples

Here are a few examples of how to use `paramspider`:

- Discover URLs for a single domain:

  ```sh
  paramspider -d example.com
  ```

- Discover URLs for multiple domains from a file:

  ```sh
  paramspider -l domains.txt
  ```

- Stream URLs on the termial:

    ```sh 
    paramspider -d example.com -s
    ```

- Set up web request proxy:

    ```sh
    paramspider -d example.com --proxy '127.0.0.1:7890'
    ```
- Adding a placeholder for URL parameter values (default: "FUZZ"): 

  ```sh
   paramspider -d example.com -p '"><h1>reflection</h1>'
  ```


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=devanshbatham/paramspider&type=Date)](https://star-history.com/#devanshbatham/paramspider&Date)


