import scrapy
from corteingles.items import CorteinglesItem
from scrapy.exceptions import CloseSpider
import csv

class CorteSpider(scrapy.Spider):
    name = "corte"
    allowed_domains = ["www.elcorteingles.es"]
    start_urls = ["https://www.elcorteingles.es/electronica/accesorios-informatica/teclados/"]
    handle_httpstatus_list = [404]  # Capturar respuesta 404 con una devolución de llamada
    page_number = 1
    data = []

    def parse(self, response):
        # Detener el spider en caso de respuesta 404
        if response.status == 404:
            raise CloseSpider('Recibida respuesta 404')

        # Detener el spider cuando no se encuentren teclados en la respuesta
        if len(response.css('div.product_preview-body')) == 0:
            raise CloseSpider('No hay teclados en la respuesta')

        # Iterar sobre cada teclado en la respuesta
        for keyboard in response.css('div.product_preview-body'):
            # Crear un item para el teclado
            keyboard_item = CorteinglesItem()
            # Extraer la marca y el precio
            keyboard_item['name'] = keyboard.css('p.product_preview-desc::text').get()
            keyboard_item['marca'] = keyboard.css('div.product_preview-brand::text').get()
            keyboard_item['price'] = keyboard.css('span.integer-price::text').get()

            # Agregar el item a la lista de datos
            self.data.append(keyboard_item)

        # Ir a la siguiente página
        self.page_number += 1
        next_page = f'https://www.elcorteingles.es/electronica/accesorios-informatica/teclados/{self.page_number}/'
        yield response.follow(next_page, callback=self.parse)

    def closed(self, reason):
        # Guardar los datos en un archivo CSV cuando el spider se cierre
        filename = 'teclados.csv'
        fieldnames = ['name' ,'marca', 'price']
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows([data_dict for data_dict in self.data])
        self.log(f'Spider cerrado: {reason}. Los datos se han guardado en {filename}.')
