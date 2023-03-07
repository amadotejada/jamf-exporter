import os

import requests
from colorama import Fore
from unopass import unopass as secret

JAMF_URL = secret.unopass("personal", "hyper_jamf", "url2")
API_USER = secret.unopass("personal", "hyper_jamf", "username2")
API_PASSWORD = secret.unopass("personal", "hyper_jamf", "password2")
OUTPUT_FOLDER = "./exported_jamf_profiles"

session = requests.Session()
session.auth = (API_USER, API_PASSWORD)
session.headers.update({"Accept": "application/json"})


def get_profiles_ids():
    response = session.get(f"{JAMF_URL}/JSSResource/osxconfigurationprofiles")
    response.raise_for_status()
    for profile in response.json()["os_x_configuration_profiles"]:
        get_profiles_data(profile)


def get_profiles_data(profile):
    profile_id = profile["id"]
    profile_name = profile["name"]
    response = session.get(f"{JAMF_URL}/JSSResource/osxconfigurationprofiles/id/{profile_id}/subset/General")
    response.raise_for_status()
    profile_data = response.json()["os_x_configuration_profile"]["general"]["payloads"]
    file_name = f"{profile_name}.mobileconfig"
    file_path = os.path.join(OUTPUT_FOLDER, file_name)
    write_profiles(file_path, profile_data, file_name)


def write_profiles(file_path, profile_data, file_name):
    with open(file_path, "w") as f:
        f.write(profile_data)
    print(f"Exported profile - {file_name}")


def main():
    try:
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        get_profiles_ids()
        print(f"{Fore.GREEN}\nJamf profiles exported successfully.")
    except Exception as e:
        secret.signout(deauthorize=True)
        print(f"{Fore.RED}Error: {e}")


if __name__ == "__main__":
    main()
