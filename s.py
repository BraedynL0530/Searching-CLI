import sys
import urllib.parse
import subprocess
import os


def main():
    if len(sys.argv) <2:
        print('Usage s <search query>')
        return
    query = " ".join(sys.argv[1:])
    encodedQuery = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={encodedQuery}"
    firefoxPath = r'C:\Program Files\Firefox Developer Edition\firefox.exe'

    if os.path.exists(firefoxPath):
        subprocess.run([firefoxPath, "-new-tab",url])


if __name__ == "__main__":
    main()