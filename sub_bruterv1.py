import requests
import sys

print("=========================================")
print("Welcome to SubBruter v1\n")

if sys.argv[1] == "-d" and sys.argv[3] == "-w" and sys.argv[4].endswith(".txt"):
        domain = sys.argv[2]
        wordlist = sys.argv[4]
        save = False
        with open(wordlist, "r") as f:
            words = f.readlines()
            for word in words:
                word = word.strip()
                try:
                    resp = requests.get("https://" + word.strip() + "." + domain.replace("www.", "").rstrip("/"), timeout=5)
                except:
                     continue
                code = resp.status_code
                if code in [200, 301, 302, 403]:
                    print("https://" + word.strip() + "." + domain.replace("www.", "").rstrip("/") + "--->", code)
                    if len(sys.argv) == 7 and sys.argv[5] == "-o" and sys.argv[6].endswith(".txt"):
                        save = True
                        output = sys.argv[6]
                        with open(output, "a") as o:
                            output.write("https://" + word + "." + domain.replace("www.", "").rstrip("/") + " ---> " + str(code) + "\n")
else:
        print("Usage: python sub_bruterv1.py -d <domain> -w <wordlist.txt> -o <output.txt>")
        sys.exit()

print("\n=========================================")
print("Developed by sudo_0xksh")