"""
@title: Get info on fixtures in the tournament
@author: Sushant Rao
@twitter: @statpeekers
"""
import re
import os.path

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

from utils.common_functions import select_tournament_name, get_data_from_file_json, put_data_to_file_json


def get_fixture_info(
    tour_id: int,
    tour_name: str,
    base_url: str,
    event_no: int,
    month: int = 0,
    year=int
):

    data_dir = f"../data/Football/AIFF/{tour_name}"
    s_driver = webdriver.Chrome()
    scrape_url = base_url + "event=" + str(event_no) + "&month=" + str(month) + "&year=" + str(year)
    s_driver.get(scrape_url)
    sleep(5)
    # Read the existing json file:
    fixture_data = get_data_from_file_json(f"{data_dir}/fixture_info.json")
    """
    Obtain table headers
    """
    t_rows = s_driver.find_elements(By.XPATH, '//*[@id="calendar"]/div[3]/div[1]/table/tbody/tr')
    for row in t_rows:
        # Get match_id
        try:
            match_url = row.find_element(By.XPATH, ".//td/a").get_attribute("href")
            match_id = re.findall('[0-9]+', match_url)[0]
            _ = {
                fix.update({"link": match_url})
                for fix in fixture_data["events"] if fix["id"] == int(match_id)
            }
            print("URL updated for matchID:", match_id)
        except NoSuchElementException:
            pass
    s_driver.close()
    # Write to the existing json file:
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
    put_data_to_file_json(f"{data_dir}/fixture_info.json", fixture_data)
    print("Fixture update completed")


if __name__ == "__main__":
    t_id, t_name = select_tournament_name()
    mapping_dict = {
        237: {
            "event_no": 19,
            "month": 0,
            "year": 2020
        },
        366: {
            "event_no": 19,
            "month": 0,
            "year": 2022
        },
        620: {
            "event_no": 19,
            "month": 0,
            "year": 2023
        },
        823: {
            "event_no": 10,
            "month": 0,
            "year": 2024
        },
        604: {
            "event_no": 2,
            "month": 0,
            "year": 2024
        },
        721: {
            "event_no": 1,
            "month": 0,
            "year": 2024
        }
    }
    b_url = "https://www.the-aiff.com/calendar?"
    e_no = mapping_dict[t_id]["event_no"]  # for Durand Cup
    mnth = mapping_dict[t_id]["month"]  # 0 for all months in a calender year else specify the month number
    yr = mapping_dict[t_id]["year"]  # Year of the tournament
    get_fixture_info(t_id, t_name, b_url, e_no, mnth, yr)
