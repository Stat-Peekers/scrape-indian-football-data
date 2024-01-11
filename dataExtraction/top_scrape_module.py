"""
@title: Top calling module to scrape single match
@author: Sushant Rao / @StatPeekers
"""

import os
import sys
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

# src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# sys.path.append(src_dir)
# os.chdir(src_dir)

# from dataExtraction.rfdl.scrape_rfdl_events import RFDLMatchEventScraping
# from dataExtraction.rfdl.scrape_rfdl_match_info import RFDLMatchInfoScraping
# from dataExtraction.rfdl.scrape_rfdl_coach_info import RFDLCoachDataScraping
# from dataExtraction.rfdl.scrape_rfdl_lineup_data import RFDLLineUpDataScraping
from utils.common_functions import select_tournament_name, put_data_to_file_json

# parent_dir = os.path.abspath(os.path.join(src_dir, os.pardir))
# sys.path.append(parent_dir)
# os.chdir(parent_dir)


class TopScrape:

    def __init__(self, match_no, match_id, tour_id, tour_name):
        super().__init__()
        self.match_no = match_no
        self.match_id = match_id
        self.tour_id = tour_id
        self.tour_name = tour_name
        self.scrape_url = "https://www.the-aiff.com/api/fixtures/cms/" + str(self.match_id)
        self._get_all_match_data_json()

    @staticmethod
    def _get_json_from_requests(scrape_url):
        return requests.get(scrape_url).json()

    def _get_all_match_data_json(self):
        all_match_data_dict = self._get_json_from_requests(self.scrape_url)
        time.sleep(5)
        is_match_ended = all_match_data_dict["fixture"]["ft"]
        json_dir = f"../data/Football/AIFF/{self.tour_name}/match_json_files/"
        if not os.path.exists(json_dir):
            os.makedirs(json_dir)
        is_file_exists = sum(1 if str(self.match_id) in filename else 0 for filename in os.listdir(f"{json_dir}"))
        if is_match_ended and not is_file_exists:
            put_data_to_file_json(f"{json_dir}{self.match_id}.json", all_match_data_dict)
