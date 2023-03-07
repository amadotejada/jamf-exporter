from colorama import Fore
from unopass import unopass as secret

import modules.export_profiles as export_profiles
import modules.export_scripts as export_scripts


def main():
    while True:
        try:
            print(Fore.BLUE + "\n===== JAMF Pro Exporter =====\n")
            print(f"{Fore.YELLOW}1. Export Scripts")
            print(f"{Fore.YELLOW}2. Export Profiles")
            print("3. Exit\n")
            choice = input("Select an option: ")

            if choice == "1":
                export_scripts.main()
            elif choice == "2":
                export_profiles.main()
            elif choice == "3":
                secret.signout(deauthorize=True)
                break
            else:
                print(f"{Fore.RED}Invalid choice. Please try again.")
        except KeyboardInterrupt:
            secret.signout(deauthorize=True)
            break


if __name__ == "__main__":
    main()
