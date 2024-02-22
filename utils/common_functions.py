# import os
# import sys
import json
import requests


# src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# sys.path.append(src_dir)
# os.chdir(src_dir)
#
# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
# sys.path.append(parent_dir)
# os.chdir(parent_dir)
#

def get_data_from_url_json(my_json_url):
    data = 0
    try:
        response = requests.get(my_json_url)
        data = response.json()
    except Exception as ex:
        print('URL is not available. ' + str(ex))

    return data


def get_data_from_file_json(filename):
    data = 0
    try:
        data = json.load(open(filename))
    except Exception as ex:
        print('JSON file is not available. ' + str(ex))

    return data


def put_data_to_file_json(filename, json_data):
    try:
        with open(filename, 'w') as f:
            json.dump(json_data, f)
    except Exception as ex:
        print('JSON file could not be updated. ' + str(ex))


def select_tournament_name():
    """
    Select the id and name for the required tournament based on input from user / client
    :return: tuple, (tourn_id, tourn_name)
    """
    tournaments_list = get_data_from_file_json("config/tour_info.json")
    # Get input for tournament details:
    i = 1
    for i, tour_dict in enumerate(tournaments_list, start=1):
        print("{}. {}".format(i, tour_dict["tour_name"]))
    while True:
        try:
            selected = int(input('Select one of the below (1-{}): '.format(i)))
            tourn_meta = tournaments_list[selected - 1]
            print('Selected Tournament is {}'.format(tourn_meta["tour_name"]))
            break
        except(ValueError, IndexError):
            print('This is not a valid selection. Please enter number between 1 and {}!'.format(i))

    return tourn_meta["tour_id"], tourn_meta["tour_name"]


# def select_team_id_name():
#     config_obj = Config()
#     team_id_name_df = config_obj.team_id_name_df
#
#     team_list = team_id_name_df["name"].unique().tolist()
#     team_dict = team_id_name_df[["name", "id"]].set_index("name").to_dict()["id"]
#
#     # Get input for team details:
#     for i, text_output in enumerate(team_list, start=1):
#         print("{}. {}".format(i, text_output))
#     while True:
#         try:
#             selected = int(input('Select one of the below (1-{}): '.format(i)))
#             team_name = team_list[selected - 1]
#             print('Selected Team is {}'.format(team_name))
#             break
#         except(ValueError, IndexError):
#             print('This is not a valid selection. Please enter number between 1 and {}!'.format(i))
#
#     team_id = team_dict[team_name]
#
#     return team_id, team_name
#
#
# def select_from_dict(fdict):
#     key_list = list(fdict.keys())
#     values_list = list(fdict.values())
#     # Get input for tournament details:
#     for i, text_output in enumerate(values_list, start=1):
#         print("{}. {}".format(i, text_output))
#     while True:
#         try:
#             selected = int(input('Select one of the below (1-{}): '.format(i)))
#             key_name = key_list[selected - 1]
#             value_name = values_list[selected - 1]
#             print('Selected Value is {}'.format(value_name))
#             break
#         except(ValueError, IndexError):
#             print('This is not a valid selection. Please enter number between 1 and {}!'.format(i))
#
#     return key_name, value_name
#
#
# def select_from_list(flist):
#     # Get input for tournament details:
#     for i, text_output in enumerate(flist, start=1):
#         print("{}. {}".format(i, text_output))
#     while True:
#         try:
#             selected = int(input('Select one of the below (1-{}): '.format(i)))
#             value_name = flist[selected - 1]
#             print('Selected Value is {}'.format(value_name))
#             break
#         except(ValueError, IndexError):
#             print('This is not a valid selection. Please enter number between 1 and {}!'.format(i))
#
#     return value_name
#
#
# def select_n_matches():
#
#     n_matches = input("Enter the range of match nos to be scraped.\nEg.1: If only 1 match is required input range(1, 2) if match no. is 1"
#                       "\nEg.2: If matches 1 to 10 are required input range(1, 11)"
#                       "\nEg.3: If matches 1, 19 and 23 are required input [1, 19, 23]\n")
#     # Return a list of match nos.
#     return eval(n_matches)
