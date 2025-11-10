thonimport json

class ResultsHandler:
    def handle_results(self, data):
        with open("data/hotel_results.json", "w") as file:
            json.dump(data, file, indent=4)