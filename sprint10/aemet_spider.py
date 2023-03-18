import scrapy
import os
import requests
from pathlib import Path

output_path = 'D:/Sistema_Solar/Python/itacademy/itacademy-datascience/sprint10/output/'
output_path = Path(output_path)

class AEMETSpider(scrapy.Spider):
    name = 'aemet_spider'
    start_urls = ['https://www.aemet.es/ca/eltiempo/prediccion/mapa_frentes']

    # Configuració per optimitzar les peticions
    custom_settings = {
        'CONCURRENT_REQUESTS': 1, # Evite fer massa peticions a la vegada
        'AUTOTHROTTLE_ENABLED': True, # Controla la velocitat de les peticions
        'DOWNLOAD_DELAY': 1 # Temps entre peticions
    }

    def parse(self, response):
        enlaces = response.css("img.lazyOwl")

        for enlace in enlaces:

            url_map = enlace.attrib["data-src"]
            url_map = 'https://www.aemet.es' + url_map

            file_name = url_map.split("/")[-1]

            file_path = "mapes_scrapy/" + file_name
            output_map = output_path / file_path
            print(output_map)
            output_map = Path(output_map)
            with open(output_map, "wb") as archivo:
                archivo.write(requests.get(url_map).content)
                print(f"Mapa {file_name} descarregat.")