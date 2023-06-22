from urllib import request, error
from urllib.parse import urljoin

def enumerate_directories(url, wordlist_file):
    try:
        with open(wordlist_file, 'r') as f:
            directory_list = f.read().splitlines()

        for directory in directory_list:
            directory = directory.strip()  # Remove leading/trailing whitespaces
            full_url = url.replace("FUZZ", directory)  # Replace "FUZZ" with the directory from the wordlist

            # Check if the directory exists
            try:
                response = request.urlopen(full_url)
                if response.code == 200:
                    print(f"[+] Directory found: {full_url}")

            except error.HTTPError as e:
                if e.code == 403:
                    print(f"[-] Access forbidden: {full_url}")
                elif e.code == 404:
                    print(f"[-] Not found: {full_url}")
                else:
                    print(f"[!] Unexpected status code {e.code} for {full_url}")

            except error.URLError as e:
                print(f"[!] Failed to reach the server: {e.reason}")

    except FileNotFoundError:
        print(f"[!] Wordlist file '{wordlist_file}' not found.")

# Example usage
target_url = input("Enter the target URL (with 'FUZZ' where the wordlist should be inserted): ")
wordlist_file = input("Enter the wordlist file path: ")

enumerate_directories(target_url, wordlist_file)
