import socket
import requests
import ipaddress
import user_agent
from urllib.parse import urlparse , urljoin, parse_qs
from bs4 import BeautifulSoup
import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)

prm_say=0

cloudflare_ip={
"104.16.0.0/12",
"104.16.0.0/13",
"172.64.0.0/13",
"104.24.0.0/14",
"162.158.0.0/15",
"198.41.128.0/17",
"108.162.192.0/18",
"141.101.64.0/18",
"173.245.48.0/20",
"188.114.96.0/20",
"190.93.240.0/20",
"141.101.104.0/21",
"141.101.112.0/21",
"141.101.80.0/21",
"141.101.88.0/21",
"141.101.96.0/21",
"188.114.104.0/21",
"188.114.96.0/21",
"199.27.128.0/21",
"103.21.244.0/22",
"103.22.200.0/22",
"103.31.4.0/22",
"131.0.72.0/22",
"141.101.120.0/22",
"197.234.240.0/22",
"103.21.246.0/23",
"141.101.78.0/23",
"141.101.124.0/24",
"141.101.125.0/24",
"141.101.126.0/24",
"141.101.127.0/24",
"141.101.66.0/24",
"141.101.70.0/24",
"141.101.71.0/24",
"141.101.74.0/24",
"141.101.75.0/24",
"185.122.0.0/24",
"204.93.173.0/24"
    }

header = {
    "User-Agent": user_agent.generate_user_agent(),
    "Accept": "*/*"
}

Important_Ports = {
    # --- CORE / NETWORK ---
    7: "Echo Reflection & amplification DoS",
    20: "FTP-DATA Cleartext creds, brute force",
    21: "FTP Cleartext creds, brute force, anonymous access",
    22: "SSH Brute force, weak keys, outdated crypto",
    23: "TELNET Cleartext credentials",
    25: "SMTP Open relay, phishing, user enumeration",
    53: "DNS Zone transfer, cache poisoning",
    67: "DHCP Rogue server, starvation",
    68: "DHCP Client abuse",
    69: "TFTP Unauthenticated file access",
    80: "HTTP XSS, SQLi, LFI, RFI, uploads",
    81: "HTTP-ALT Misconfigurations",
    110: "POP3 Cleartext creds",
    111: "RPC Info leak",
    119: "NNTP Cleartext creds",
    123: "NTP Amplification DDoS",
    135: "MSRPC Enumeration",
    137: "NetBIOS Info leak",
    138: "NetBIOS Info leak",
    139: "SMB Enumeration",
    143: "IMAP Cleartext creds",
    161: "SNMP Public strings, info leak",
    179: "BGP Info leak",
    1900: "SSDP Amplification, UPnP info leak",
    194: "IRC Botnet C2",
    443: "HTTPS XSS, SQLi, auth issues",
    445: "SMB RCE, relay, misconfigurations",
    514: "SYSLOG Spoofing, info leak",
    # --- DATABASE ---
    1433: "MSSQL Auth bypass, weak creds",
    1434: "MSSQL Browser info leak",
    3306: "MySQL Weak creds, SQLi",
    3356: "MySQL SSL",
    3360: "MySQL X Protocol",
    3344: "MySQL Dump exposure",
    5432: "PostgreSQL Unauth access",
    5433: "PostgreSQL ALT",
    27017: "MongoDB Unauth access",
    27018: "MongoDB Shard",
    9042: "Cassandra Unauth access",
    # --- MAIL ---
    587: "SMTP Submission",
    993: "IMAPS",
    995: "POP3S",
    # --- ADMIN / PANELS ---
    2082: "cPanel",
    2083: "cPanel SSL",
    2095: "Webmail",
    2096: "Webmail SSL",
    5601: "Kibana Dashboard",
    6080: "Admin panels",
    9000: "Admin panels, SonarQube, PHP-FPM",
    9001: "Supervisor Admin",
    9443: "HTTPS Admin panels",
    # --- DEV / API / WEB ALT ---
    3000: "Node.js / React Dev Server",
    3001: "Dev APIs",
    4000: "API Gateway / GraphQL",
    5000: "Flask / API Server",
    5173: "Vite Dev Server",
    7001: "WebLogic RCE",
    7002: "WebLogic RCE",
    8080: "HTTP-ALT Web apps",
    8443: "HTTPS-ALT Web apps",
    8888: "Jupyter / Debug consoles",
    # --- REMOTE ACCESS ---
    3389: "RDP Brute force, weak crypto",
    5900: "VNC Brute force",
    # --- VOIP ---
    5060: "SIP Cleartext creds",
    5061: "SIPS",
    # --- CACHE / QUEUE ---
    6379: "Redis Unauth access, RCE",
    11211: "Memcached Unauth access",
    5672: "RabbitMQ",
    15672: "RabbitMQ Management UI",
    # --- CLOUD / CONTAINERS ---
    2375: "Docker API Unauth access",
    2376: "Docker API TLS",
    6443: "Kubernetes API Server",
    10250: "Kubelet API",
    10255: "Kubelet Read-only API",
    # --- FILE SHARING ---
    2049: "NFS Info leak",
    # --- LDAP / ENTERPRISE ---
    389: "LDAP Anonymous bind",
    636: "LDAPS",
    6369: "Global Catalog LDAP"
}
main_menu_logo=Fore.LIGHTGREEN_EX + r"""

                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

"""

def is_cloudflare(ip):
    ip_obj = ipaddress.ip_address(ip)
    for net in cloudflare_ip:
        if ip_obj in ipaddress.ip_network(net):
            return True
    return False

def is_ip_address(value):
    return value.count(".") == 3 and all(
        part.isdigit() and 0 <= int(part) <= 255
        for part in value.split(".")
    )

def reverse_dns(ip):
    try:
        host, aliases, ips = socket.gethostbyaddr(ip)
        return host
    except socket.herror:
        return None

while True:
    print(main_menu_logo)
    hedef = input("Enter site name: ").strip()
    site=hedef
    #Url Crawler
    founded_urls = set()
    visited_urls = set()
    #Ip Address kontrolu hatali
    if is_ip_address(hedef):
        print(Fore.YELLOW + "[+] IP address Detected\n")

        ip = hedef
        rev_dns = reverse_dns(ip)

        if rev_dns:
            site = rev_dns.rstrip('.')
            print(Fore.LIGHTGREEN_EX + f"[+] Reverse DNS Lookup: {rev_dns}\n")
        else:
            ip = site
            print(Fore.LIGHTRED_EX + "[-] Can't get Reverse IP Lookup.\n")
            
    else:
        site = hedef.replace("https://","").replace("http://","")
        ip = socket.gethostbyname(site)
    if is_cloudflare(ip):
        print(Fore.LIGHTRED_EX + f"[-] {site} is using Cloudflare Protection!\n")
        print("Do you want continue? (y/n): ", end="")
        secim = input()
        if secim.lower() == "y":    
            print("Admin Panel Finding ...\n")
            response =requests.get(f"https://{site}", headers=header)
            if response.status_code != 404:
                print(Fore.LIGHTGREEN_EX + f"[+] Website is Up: https://{site}")
                with open("Wordlist.txt","r") as wordlist:
                    for i in wordlist:
                        i = i.strip()
                        ad_url = f"https://{site}/{i}"
                        resadmin = requests.get(ad_url, headers=header, timeout=3)
                        if resadmin.status_code != 404:
                            print(Fore.LIGHTGREEN_EX + f"[+] Admin Panel Found: {ad_url}")
                        else:
                            print(Fore.LIGHTRED_EX + f"[-] Admin Panel Not Found")
            else:
                print(Fore.LIGHTRED_EX + f"[-] Website is Down: https://{site}")
        elif secim.lower() == "n":
            break
        else:
            print(Fore.LIGHTRED_EX + "[-] Invalid choice!")
            continue

    else:
        print(Fore.LIGHTBLUE_EX + f"[+] IP Adress: {ip}\n")
        print("Admin Panel Finding ...\n")
        response =requests.get(f"https://{site}", headers=header)
        if response.status_code != 404:
            print(Fore.LIGHTGREEN_EX + f"[+] Website is Up: https://{site}\n")
            with open("Wordlist.txt","r") as wordlist:
                for i in wordlist:
                    i = i.strip()
                    ad_url = f"https://{site}/{i}"
                    resadmin = requests.get(ad_url, headers=header, timeout=3)
                    if resadmin.status_code == 200:
                        txt = resadmin.text.lower()
                        if ('type="password"' in txt) or ('type="email"' in txt) or ('type="username"' in txt) or ('password' in txt and "<form" in txt):
                            print(Fore.LIGHTGREEN_EX + f"[+] Admin Panel Found: {ad_url}\n")
                        elif resadmin.status_code in [301, 302]:
                            location = resadmin.headers.get9('Location', "").lower()
                            if any(x in location for x in ["login", "admin", "panel", "auth", "author", "dashboard", "controlpanel", "cpanel", "yonetici", "yonetim", "adminarea", "adminpanel","login", 'admin panel', 'administrator', 'admin login']).lower():
                                print(Fore.LIGHTGREEN_EX + f"[+] Admin Panel Found: {ad_url}\n")
                        elif resadmin.status_code == 403:
                            print(Fore.LIGHTCYAN_EX + f"[?] Possible Admin Panel (403 Forbidden): {ad_url}\n")
                    else:
                        print(Fore.LIGHTRED_EX + f"[-] Admin Panel Not Found: {ad_url}\n")
            print("Port Scan Starting...\n")
            for port, service in Important_Ports.items():
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                    
                sock.settimeout(1)
                result = sock.connect_ex((ip,port))
                if result == 0:
                    print(Fore.LIGHTGREEN_EX + f"[+] Port {port} - {service} is Open\n")
                    '''burada banner grabber var yeni ekledim hatali
                            banner = sock.recv(1024) 
                            if banner:
                                print(Fore.LIGHTCYAN_EX + f"[+] Banner: {banner.decode().strip()}\n")
                            else:
                                print(Fore.LIGHTYELLOW_EX + "[*] No banner received.\n")
                            '''
                else:
                    print(Fore.LIGHTRED_EX + f"[-] Port {port} - {service} is Closed\n")
                    sock.close()
                         #-------------------------------------------
        else:
            print(Fore.LIGHTRED_EX + f"[-] Website is Down: https://{site}\n")
            break
    #Url Crawller
    print("URL Crawling Starting...\n")
    visit = [f"https://{site}"]
    while visit and len(founded_urls)<500:
        url = visit.pop(0)
        if url in visited_urls:
            continue
        visited_urls.add(url)
        try:
            r = requests.get(url, headers=header, timeout=5)
            if r.status_code != 200:
                continue
        except requests.RequestException:
            continue
        soup = BeautifulSoup(r.text, 'html.parser')
        for etk in soup.find_all('a', href=True):
            link = etk['href']
            if link.startswith(("mailto:", "javascript:", "#")):
                continue
            full_url = urljoin(url, link)
            prsd_link = urlparse(full_url)
            if prsd_link.netloc == site:
                cln_url = prsd_link.scheme + "://" + prsd_link.netloc + prsd_link.path
                if cln_url not in founded_urls:
                    founded_urls.add(cln_url)
                    visit.append(cln_url)
                    print(Fore.LIGHTGREEN_EX + f"[+] Found {len(founded_urls)} URLs:\n")
                    with open("founded_urls.txt","a", encoding="utf-8", errors="replace") as yaz:
                        yaz.write(cln_url + "\n")
                        print(Fore.LIGHTGREEN_EX + f"[+] Urls saved to {Fore.LIGHTRED_EX}founded_urls.txt{Fore.LIGHTGREEN_EX} file.\n")
                        if cln_url not in founded_urls:
                            founded_urls.add(cln_url)
                            with open("founded_urls.txt","a", encoding="utf-8", errors="replace") as yaz:
                                yaz.write(cln_url + "\n")
    print(Fore.LIGHTGREEN_EX + f"[+] URL Crawling Completed. Total URLs Found: {len(founded_urls)}\n")
    print(Fore.LIGHTGREEN_EX + f" Do You Want Filter URLs By Extinsion? (y/n): ", end="")
    secim = input()
    if secim.lower() == "y":
        print("[?] Enter The Extinnsion (e.g., .php, .html): ", end="")
        ext = input()
        filtered_urls = [filterurl for filterurl in founded_urls if filterurl.endswith(ext)]
        print(Fore.LIGHTGREEN_EX + f"[+] Found {len(filtered_urls)} URLs with extension {ext}:\n")
        with open("filtered_urls.txt","w", encoding="utf-8") as filter:
            for url in filtered_urls:
                filter.write(url + "\n")
                print(Fore.LIGHTGREEN_EX + f"[+] Filtered URLs saved to {Fore.LIGHTRED_EX}filtered_urls.txt{Fore.LIGHTGREEN_EX} file.\n")
    elif secim.lower() == "n":
        print(Fore.LIGHTGREEN_EX + "[+] No filtering applied.\n")
        print(Fore.LIGHTYELLOW_EX + f"[?] Do You Want Continue? (y/n): ", end="")
        continue_choice = input()
        if continue_choice.lower() == "y":
            
            # possiblity sql ve xss parametre tarama 
            print("Parameter Scanning Starting...\n")
            for url in founded_urls:
                if "?" in url and "=" in url:
                    parsed_url = urlparse(url)
                    sorgu_param = parse_qs(parsed_url.query)
                    k += 1
                    for param in sorgu_param:
                        if prm_say>0:
                            print(Fore.LIGHTGREEN_EX + f"[+] Parameter Founded In URL: {url} -> Parameter: {param}\n")
                        else:
                            print(Fore.LIGHTRED_EX + f"[-] Parameters Not Found In URLs.\n")
                    print(Fore.LIGHTYELLOW_EX + f"[?] Do You Want To Save Parameters To File? (y/n): ", end="")
                    save_choice = input()
                    if save_choice.lower() == "y":
                        with open("found_parameters.txt","w", encoding="utf-8") as param_file:
                            for url in founded_urls:
                                if "?" in url and "=" in url:
                                    parsed_url = urlparse(url)
                                    sorgu_param = parse_qs(parsed_url.query)
                                    for param in sorgu_param:
                                        param_file.write(f"URL: {url} -> Parameter: {param}\n")
                    else:
                        print(Fore.LIGHTGREEN_EX + "[+] Parameters not saved.\n")
        else:
            break