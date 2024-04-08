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
   - Create a text file containing one URL per line.

2. **Run the Script:**
   - Execute the script providing the input file path and desired output file path.
     ```bash
     python url_tester.py input.txt output.txt
     ```
     Optionally, you can specify a timeout (in seconds) for each request:
     ```bash
     python url_tester.py input.txt output.txt --timeout 5
     ```

3. **View Results:**
   - Open the output file specified. The file will contain reachable URLs.

### Example

Suppose you have an input file `urls.txt` with the following content:
Certainly! Here's the updated README content as code:

markdown

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


