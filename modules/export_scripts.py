import os

import requests
from colorama import Fore
from unopass import unopass as secret

JAMF_URL = secret.unopass("personal", "hyper_jamf", "url2")
JAMF_USERNAME = secret.unopass("personal", "hyper_jamf", "username2")
JAMF_PASSWORD = secret.unopass("personal", "hyper_jamf", "password2")
OUTPUT_FOLDER = "./exported_jamf_scripts"

EXTENSIONS = {
    "bash": ".sh",
    "sh": ".sh",
    "zsh": ".sh",
    "python": ".py",
    "python3": ".py",
    "package main": ".go",
}


def get_script_ids():
    with requests.Session() as session:
        session.auth = (JAMF_USERNAME, JAMF_PASSWORD)
        session.headers = {"Accept": "application/json"}
        response = session.get(f"{JAMF_URL}/JSSResource/scripts")
        response.raise_for_status()
        scripts = response.json().get("scripts", [])
        for script in scripts:
            script_id = script["id"]
            get_script_data(script_id, session)


def get_script_data(script_id, session):
    script_url = os.path.join(f"{JAMF_URL}/JSSResource/scripts/", "id", str(script_id))
    response = session.get(script_url)
    response.raise_for_status()
    script = response.json().get("script", {})
    script_name = script.get("name")
    script_content = script.get("script_contents", "")
    interpreter = next(
        (
            line.split("/")[-1].split()[-1].strip()
            for line in script_content.split("\n")
            if line.startswith("#!")
        ),
        None,
    )
    write_script(script_name, script_content, interpreter)


def write_script(script_name, script_content, interpreter):
    if interpreter in EXTENSIONS:
        script_path = os.path.join(
            OUTPUT_FOLDER, f"{script_name}{EXTENSIONS.get(interpreter)}"
        )
    else:
        script_path = os.path.join(OUTPUT_FOLDER, f"{script_name}.txt")
        print(f"Unsupported interpreter: {interpreter}, script_name: {script_name}")
    with open(script_path, "w") as f:
        f.write(script_content)
    print(f"Exported script - {script_name}")


def main():
    try:
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)
        get_script_ids()
        print(f"{Fore.GREEN}\nJamf scripts exported successfully.")
    except Exception as e:
        secret.signout(deauthorize=True)
        print(f"{Fore.RED}Error: {e}")


if __name__ == "__main__":
    main()
