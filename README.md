# jamf-exporter
Export all scripts, proflles and more from Jamf Pro

This script allows you to export all the macOS scripts and configuration profiles from a JAMF Pro server. Scripts are saved with their file extensions and profiles as .mobileconfig files on your local system.

#
### Requirements
- `pip install -r requirements.txt`
- unopass: https://github.com/amadotejada/unopass

#
### Usage
1. Configure unopass
2. Fork or download this project
3. Run it from the command line:

`python jamf_profiles_exporter.py`

<img src="./screenshot.png" width="100%">

- Scripts are downloaded in: `./exported_jamf_scripts`
- Profiles are downloaded in: `./exported_jamf_profiles`

#
### TODO
- Add support for exporting printers
- Add support for exporting iOS configuration profiles

#
### Licence
This script is released under the MIT License. You are free to use, modify, and distribute the script as long as you include the original license file.

### Disclaimer
This script is provided as-is and is not guaranteed to work for all JAMF Pro servers. Use it at your own risk and always test it thoroughly before using it in a production environment.
#