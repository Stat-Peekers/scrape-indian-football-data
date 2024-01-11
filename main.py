"""
@title: Main script to scrape Durand Cup match-wise data
@author: Sushant Rao / @StatPeekers
"""
import os.path

from os import listdir
from tqdm import trange

from utils.common_functions import select_tournament_name, get_data_from_file_json


def logger_setup():
    import logging.config
    logging.config.fileConfig('logs/console_logs.conf')


def get_tour_match_ids(tour_name):
    # Read the existing json file:
    fixture_data = get_data_from_file_json(f"../data/Football/AIFF/{tour_name}/fixture_info.json")
    return [fix["id"] for fix in fixture_data["events"] if fix["link"] != ""]


if __name__ == "__main__":
    """
    Set-up logger
    """
    t_id, t_name = select_tournament_name()
    # Scrape pts table:
    from dataExtraction.pts_table_scraping import PtsTable
    PtsTable(t_id, t_name)
    while True:
        initial_input = input("Select type of scraping:\n1. Single match\n2. All matches in tournament\n")
        try:
            initial_input = int(initial_input)
            if initial_input in [1, 2]:
                break
            else:
                print("Input should be either 1 or 2. Try again...\n")
        except ValueError:
            print("You have not entered a valid numeric value. Try again...\n")

    # Scrape match-wise data:
    from dataExtraction.top_scrape_module import TopScrape
    # Get list of match_ids
    match_ids = get_tour_match_ids(t_name)
    data_dir = f"../data/Football/AIFF/{t_name}/match_json_files/"
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
    existing_match_ids = listdir(data_dir)
    existing_match_ids = [int(filename.replace(".json", "")) for filename in existing_match_ids]

    if initial_input == 1:
        """ ------------------------------------------------ For Single Match ------------------------------------------------ """
        # Take input for match no to process:
        print("\n=== You can find specific match IDs from config/fixture_info.json ===\n")
        while True:
            try:
                m_id = int(input("Enter the Match ID: "))
                i = match_ids.index(m_id)
                break
            except ValueError:
                print("Incorrect Match ID selected. Try Again...\n")
        print("\nScraping for:", t_name, "Match no:", m_id)
        TopScrape(i, m_id, t_id, t_name)
    elif initial_input == 2:
        """ ------------------------------------------------ For All Matches ------------------------------------------------- """
        for i in trange(len(match_ids), desc="Getting Match-wise Data"):
            m_id = match_ids[i]
            if m_id in existing_match_ids:
                continue
            TopScrape(i, m_id, t_id, t_name)
    else:
        print("Incorrect initial input selected")
