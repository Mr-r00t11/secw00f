# secw00f

## Description

**secw00f** is a tool designed to detect and analyze security configurations in web applications. Similar to **wafw00f**, which identifies Web Application Firewalls (WAFs), **secw00f** focuses on detecting security headers and verifying if web applications are protected against threats such as XSS, SQLi, CSRF, among others.

## Features

- **WAF Detection**: Identifies if a web application is protected by a WAF and specifies the name of the detected WAF.
- **Security Headers Analysis**: Checks for the presence of key security headers like `Content-Security-Policy`, `X-Content-Type-Options`, `X-XSS-Protection`, `Strict-Transport-Security`, among others.
- **Colored Output**: Presents results in the console with colors for easy reading. Present headers are shown in green, while missing headers are shown in red.

## Requirements

- Python 3.x
- `requests` library
- `colorama` library

You can install the required libraries with the following command:

`pip install requests colorama`

## Usage

### Installation

1. Clone this repository:

`git clone https://github.com/yourusername/secw00f.git` 
`cd secw00f`

2. Ensure you have the dependencies installed:

`pip install -r requirements.txt`

### Running the Tool

To run **secw00f** on a list of URLs stored in a text file:


`python secw00f.py -l urls.txt`

- `-l`, `--list`: Specifies the file containing the URLs to be analyzed. The file should have one URL per line.

### Example

If you have a `urls.txt` file with the following content:

```bash
http://example1.com 
http://example2.com 
http://example3.com
```

Run the following command to analyze the URLs:

`python secw00f.py -l urls.txt`

![[Pasted image 20240727183651.png]](https://raw.githubusercontent.com/Mr-r00t11/secw00f/main/img/Pasted%20image%2020240727183651.png)

The tool will print the results in the console and also save them to a file named `wafw00f_results.txt`.

## Output

The output includes:

- The detected WAF (if any).
- The presence or absence of the following security headers:
    - `Content-Security-Policy`
    - `X-Content-Type-Options`
    - `X-XSS-Protection`
    - `Strict-Transport-Security`
    - `X-Frame-Options`
    - `Set-Cookie`

Present headers will be shown in green, and missing headers will be shown in red.
