import hashlib
import csv
import os
import datetime
from colorama import init, Fore, Style

# Initialize Colorama for ANSI color codes
init(autoreset=True)

# Constants
EVIDENCE_DIR = "evidence"
CUSTODY_RECORDS_FILE = "custody_records.csv"

# Create evidence directory if it doesn't exist
if not os.path.exists(EVIDENCE_DIR):
    os.makedirs(EVIDENCE_DIR)

# Initialize CSV file for custody records if it doesn't exist
if not os.path.isfile(CUSTODY_RECORDS_FILE):
    with open(CUSTODY_RECORDS_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Evidence', 'Hash'])

# Define colored text styles
BOLD = Fore.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT
ERROR = Fore.LIGHTRED_EX + Style.BRIGHT
SUCCESS = Fore.LIGHTGREEN_EX + Style.BRIGHT

# ASCII art banner
BANNER = BOLD + r'''
 ██████╗██╗   ██╗██████╗ ███████╗██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗   ██║   ██████╔╝███████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
'''

# Functions for recording and verifying custody
def record_chain_of_custody():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    evidence_name = input("Enter the name of the digital evidence file: ")

    evidence_path = os.path.join(EVIDENCE_DIR, evidence_name)

    if not os.path.isfile(evidence_path):
        print(ERROR + "File does not exist.")
        return

    # Calculate SHA-256 hash of the file
    hasher = hashlib.sha256()
    with open(evidence_path, 'rb') as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            hasher.update(data)

    file_hash = hasher.hexdigest()

    # Append the custody record to the CSV file
    with open(CUSTODY_RECORDS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, evidence_name, file_hash])

    print(SUCCESS + "Chain of custody recorded successfully.")
    input("Press Enter to continue...")

def verify_chain_of_custody():
    evidence_name = input("Enter the name of the digital evidence file: ")

    # Find the latest custody record for the evidence
    latest_record = None
    with open(CUSTODY_RECORDS_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == evidence_name:
                latest_record = row

    if latest_record:
        print(BOLD + "Latest custody record:")
        print("Timestamp:", latest_record[0])
        print("Evidence:", latest_record[1])
        print("Hash:", latest_record[2])
    else:
        print(ERROR + "Evidence not found in custody records.")

if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print(BANNER)
        print(BOLD + "Chain of Custody Tool")
        print("1. Record Chain of Custody")
        print("2. Verify Chain of Custody")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            record_chain_of_custody()
        elif choice == '2':
            verify_chain_of_custody()
        elif choice == '3':
            break
        else:
            print(ERROR + "Invalid choice. Please try again.")
