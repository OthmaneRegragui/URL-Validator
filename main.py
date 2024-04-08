import requests

def test_urls(file_path, output_file, timeout=5):
    reachable_urls = []
    unreachable_urls = []

    with open(file_path, 'r') as file:
        urls = file.readlines()

    for url in urls:
        url = f"https://{url.strip()}"
        print(url)
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                reachable_urls.append(url)
            else:
                unreachable_urls.append(url)
        except requests.ConnectionError:
            unreachable_urls.append(url)
        except requests.Timeout:
            unreachable_urls.append(url)

    with open(output_file, 'w') as file:
        file.write("Reachable URLs:\n")
        for url in reachable_urls:
            file.write(url + '\n')

    print("Testing completed. Results saved in", output_file)

if __name__ == "__main__":
    input_file_path = "input.txt"
    output_file_path = "output.txt" 
    test_urls(input_file_path, output_file_path, timeout=5)
