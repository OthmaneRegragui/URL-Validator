# URL-Validator

URL-Tester-Python is a Python script that allows you to quickly test the reachability of URLs listed in a text file. This script is particularly useful for checking the availability of web resources and ensuring that URLs are accessible from your network environment.

## URL Tester Python

URL Tester Python is a Python script that allows you to quickly test the reachability of URLs listed in a text file. This script is particularly useful for checking the availability of web resources and ensuring that URLs are accessible from your network environment.

### Features

- Tests the reachability of URLs listed in a text file.
- Saves reachable URLs to an output file for further analysis.
- Supports custom timeout settings for network requests.
- Provides clear feedback on reachable and unreachable URLs.

### Prerequisites

- Python 3.x installed on your system.
- `requests` library installed (can be installed via pip).

### Usage

1. **Prepare Input File:**
   - Create a text named "input.txt" file containing one URL per line.

2. **Run the Script:**
   - Execute the script providing the input file path and desired output file path.
     ```bash
     python main.py
     ```

### Results

The output.txt file will contain the reachable URLs:

google.com
example.com
nonexistent.example.com


