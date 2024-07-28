import subprocess
import argparse
import re
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def run_wafw00f(url):
    try:
        result = subprocess.run(['wafw00f', url], capture_output=True, text=True)
        output = result.stdout
        match = re.search(r'is behind (.+?) WAF', output)
        if match:
            waf_name = match.group(1).strip()
            print(f"{Fore.GREEN}[+]{Fore.CYAN} {url}{Style.RESET_ALL} is behind {Fore.MAGENTA}{waf_name}{Style.RESET_ALL} WAF")
            return f"{url} is behind {waf_name} WAF\n"
        else:
            print(f"{Fore.RED}[-] {Style.RESET_ALL}No WAF detected for {Fore.CYAN}{url}{Style.RESET_ALL}")
            return f"No WAF detected for {url}\n"
    except Exception as e:
        error_message = f"Error executing wafw00f for {url}: {e}"
        print(error_message)
        return error_message + '\n'

def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        security_headers = {
            'Content-Security-Policy': (Fore.CYAN, 'CSP (Content Security Policy)'),
            'X-Content-Type-Options': (Fore.CYAN, 'X-Content-Type-Options (NoSniff)'),
            'X-XSS-Protection': (Fore.CYAN, 'X-XSS-Protection (XSS Protection)'),
            'Strict-Transport-Security': (Fore.CYAN, 'HSTS (HTTP Strict Transport Security)'),
            'X-Frame-Options': (Fore.CYAN, 'X-Frame-Options (Clickjacking Protection)'),
            'Set-Cookie': (Fore.CYAN, 'Set-Cookie (CSRF Protection with HttpOnly, Secure, SameSite)')
        }

        results = []
        for header, (color, description) in security_headers.items():
            if header in headers:
                result = f"{color}{description}: {Fore.GREEN}Present{Style.RESET_ALL}"
                results.append(result)
                print(f"  - {result}")
            else:
                result = f"{color}{description}: {Fore.RED}Missing{Style.RESET_ALL}"
                results.append(result)
                print(f"  - {result}")
                
        print("--------" * 10)
        return "\n".join(results) + "\n"

    except requests.RequestException as e:
        error_message = f"Error fetching headers for {url}: {e}"
        print(error_message)
        return error_message + '\n'

def main(input_file):
    output_file = 'wafw00f_results.txt'

    with open(input_file, 'r') as file:
        urls = [line.strip() for line in file.readlines()]

    with open(output_file, 'w') as file:
        for url in urls:
            if url:
                result = run_wafw00f(url)
                file.write(result)

                headers_result = check_security_headers(url)
                file.write(f"Security headers for {url}:\n")
                file.write(headers_result)
                file.write("\n")
    print(f"\n{Fore.YELLOW}[!] Results have been saved to {Style.RESET_ALL}{Fore.BLUE}{output_file}{Style.RESET_ALL}")

if __name__ == '__main__':
    print(f"""{Fore.LIGHTMAGENTA_EX}
███████╗███████╗ ██████╗██╗    ██╗ ██████╗  ██████╗ ███████╗
██╔════╝██╔════╝██╔════╝██║    ██║██╔═████╗██╔═████╗██╔════╝
███████╗█████╗  ██║     ██║ █╗ ██║██║██╔██║██║██╔██║█████╗  
╚════██║██╔══╝  ██║     ██║███╗██║████╔╝██║████╔╝██║██╔══╝  
███████║███████╗╚██████╗╚███╔███╔╝╚██████╔╝╚██████╔╝██║     
╚══════╝╚══════╝ ╚═════╝ ╚══╝╚══╝  ╚═════╝  ╚═════╝ ╚═╝     
{Style.RESET_ALL}_________ identifies WAF and security headers ________ {Fore.LIGHTGREEN_EX}by Mr r00t{Style.RESET_ALL}
""")
    parser = argparse.ArgumentParser(description="Run wafw00f and check security headers on multiple URLs from a file.")
    parser.add_argument('-l', '--list', required=True, help='Path to the file containing the list of URLs.')

    args = parser.parse_args()
    main(args.list)
