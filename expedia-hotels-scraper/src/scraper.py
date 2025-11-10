thonimport json
import requests
from extractors.expedia_extractor import ExpediaExtractor
from extractors.hotels_com_extractor import HotelsComExtractor
from outputs.results_handler import ResultsHandler

class HotelScraper:
    def __init__(self, location, check_in, check_out):
        self.location = location
        self.check_in = check_in
        self.check_out = check_out
        self.expedia_extractor = ExpediaExtractor(self.location, self.check_in, self.check_out)
        self.hotels_com_extractor = HotelsComExtractor(self.location, self.check_in, self.check_out)
        self.results_handler = ResultsHandler()

    def scrape(self):
        expedia_data = self.expedia_extractor.extract_data()
        hotels_com_data = self.hotels_com_extractor.extract_data()

        all_data = expedia_data + hotels_com_data
        self.results_handler.handle_results(all_data)

if __name__ == "__main__":
    scraper = HotelScraper("New York", "2023-12-01", "2023-12-05")
    scraper.scrape()