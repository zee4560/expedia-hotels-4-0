thonimport requests

class ExpediaExtractor:
    def __init__(self, location, check_in, check_out):
        self.location = location
        self.check_in = check_in
        self.check_out = check_out

    def extract_data(self):
        url = f"https://www.expedia.com/api/v1/hotels?location={self.location}&check_in={self.check_in}&check_out={self.check_out}"
        response = requests.get(url)
        data = response.json()
        
        extracted_data = []
        for hotel in data['hotels']:
            hotel_info = {
                "hotelname": hotel['name'],
                "location": hotel['location'],
                "description": hotel['description'],
                "amenities": hotel['amenities'],
                "reviews": hotel['reviews'],
                "rating": hotel['rating'],
                "offers": hotel['offers']
            }
            extracted_data.append(hotel_info)
        return extracted_data