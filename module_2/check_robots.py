# Confirm robo.txt file permits scraping
import urllib.robotparser

# Initialize RobotFileParser
rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.thegradcafe.com/robots.txt")
rp.read()

agent = "samira"
base_path = "https://www.thegradcafe.com/survey/?page="

# Check access for each page
disallowed_pages = []
for page_num in range(1, 501):
    full_url = f"{base_path}{page_num}"
    if not rp.can_fetch(agent, full_url):
        disallowed_pages.append(full_url)

if len(disallowed_pages) > 0:
    print(f"{len(disallowed_pages)} page(s) are disallowed:")
    for url in disallowed_pages:
        print(url)
else:
    print("All 500 survey pages are allowed for scraping.")