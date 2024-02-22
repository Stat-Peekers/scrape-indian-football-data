"""
@title: Module to scrape points table
@author: Sushant Rao / @StatPeekers
"""

import os
import requests

from utils.common_functions import select_tournament_name, put_data_to_file_json


class PtsTable:

    def __init__(self, tour_id, tour_name):
        super().__init__()
        self.tour_id = tour_id
        self.tour_name = tour_name
        self.scrape_url = f"https://www.the-aiff.com/api/stats/points-table/{tour_id}"
        self._get_json_from_requests()

    def _get_json_from_requests(self):
        response = requests.get(self.scrape_url)
        if response.status_code != 200:
            raise Exception("Response was code " + str(response.status_code))
        data_dir = f"../data/Football/AIFF/{self.tour_name}/"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        put_data_to_file_json(data_dir + "points_table.json", response.json())


if __name__ == "__main__":
    t_id, t_name = select_tournament_name()
    PtsTable(t_id, t_name)
