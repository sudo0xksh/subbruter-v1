# 🌐🔥 SubBruter v1 🔥🌐

SubBruter v1 is a simple Python CLI tool that brute-forces subdomains for a given domain
using a wordlist and HTTP requests 😈🌍

If a subdomain exists, this tool will knock.
If it doesn’t, it quietly moves on.

---

## 👀 Overview

Big websites rarely live on a single domain.
They hide admin panels, APIs, old services, and test environments
behind subdomains 👀🌐

SubBruter v1 takes a target domain and a wordlist,
then tries each word as a subdomain
to see what actually responds.

Simple recon.
Real results.

---

## 🚀 Features

- Brute-forces subdomains 🌍  
- Uses a custom wordlist 📜  
- Detects interesting HTTP responses  
- Shows status codes like 200, 301, 302, 403 🧠  
- Optional output saving to a file 💾  
- Beginner-friendly and easy to understand ⚡  

---

## ⚙️ How It Works

The tool reads each word from the wordlist,
appends it as a subdomain to the target domain,
and sends an HTTP request.

If the server responds with an interesting status code,
the subdomain is printed.

If output saving is enabled,
results are written to a file automatically.

No DNS magic.
Just brute logic.

---

## 🧪 Usage

Run the tool exactly like this  
python sub_bruterv1.py -d <domain> -w <wordlist.txt> -o <output.txt>

Example  
python sub_bruterv1.py -d example.com -w subdomains.txt -o results.txt

The tool will print live results as it discovers subdomains 😎

---

## 📤 Example Output

https://admin.example.com ---> 200  
https://api.example.com ---> 403  
https://test.example.com ---> 302  

Discovery completed.

---

## 📦 Requirements

- Python 3.x  
- requests library  

Install requests if needed  
pip install requests

---

## 🧠 What You Learn From This Project

- Subdomain enumeration basics  
- Wordlist-based recon  
- Understanding HTTP response behavior  
- Automating recon with Python  
- Why subdomains matter in security  

---

## 🗿 Final Words

Domains hide.
Subdomains expose.
Wordlists reveal.

If you can enumerate smartly,
you can find interesting attack surfaces 🔥🌐
