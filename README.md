<p align="center">
    <a href="https://docs.scrapy.org/en/latest/">
        <img src="resources\scrapy_img.png" alt="scrapy">
    </a>
</p>

# Mini Scrapy project
This is a small project to see how the Python Scrapy framework works and how we can get data from different web pages. In this case we are going to scrape the online shop "elcorteingles.es" and get the name, brand and price of all the keyboards they sell and download them in a csv file.

## Installation process 

Clone the repository

    git clone https://github.com/pablopuch/scrapy.git

Install framework scrapy

    pip install scrapy

Install management of virtual environments pipenv

    pip install pipenv

Run pipenv

    pipenv shell

Move to the scrapy directory

    cd .\scrapy\corteingles\

run scrapy

    scrapy crawl corte


## First scrpay result, exporting the data to a csv file.

<p align="center">
    <a href="https://docs.scrapy.org/en/latest/">
        <img src="resources\csv.png" alt="csv_final">
    </a>
</p>

## Resources

Full tutorial : https://openwebinars.net/academia/portada/extrae-informacion-web-scrapy/