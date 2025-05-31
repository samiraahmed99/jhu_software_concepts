# Confirm robo.txt file permits scraping
import urllib.robotparser

# Initialize RobotFileParser
rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.thegradcafe.com/robots.txt")
rp.read()

agent = "samira"
base_path = "https://www.thegradcafe.com/survey/?page="

# Check access for each page only print if a specific page is disallowed
# There are 20 entries per page, so 2500 pages total to get 50,000 entries
disallowed_pages = []
for page_num in range(1, 2501):
    full_url = f"{base_path}{page_num}"
    if not rp.can_fetch(agent, full_url):
        disallowed_pages.append(full_url)

if len(disallowed_pages) > 0:
    print(f"❌ {len(disallowed_pages)} page(s) are disallowed:")
    for url in disallowed_pages:
        print(url)
else:
    print("✅ All 2500 survey pages are allowed for scraping.")


# Scrape Data:

import requests
from bs4 import BeautifulSoup

class ScrapeData:
    def __init__(self):
        self.base_url = "https://www.thegradcafe.com/survey/?page="

    def fetch_page(self, page_number):
        url = f"{self.base_url}{page_number}"
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return BeautifulSoup(response.content, "html.parser")

    def extract_entries(self, soup):
        entries = []

        rows = soup.find_all("tr")
        for row in rows:
            try:
                # Universities:
                uni_div = row.find("div", class_="tw-font-medium tw-text-gray-900 tw-text-sm")
                university = uni_div.get_text(strip=True) if uni_div else None

                # Programs:
                td_program = row.find("td", class_="tw-px-3 tw-py-5 tw-text-sm tw-text-gray-500")
                span = td_program.find("span") if td_program else None
                program = span.get_text(strip=True) if span else None

                # Degree Type:
                degree_span = row.find("span", class_="tw-text-gray-500")
                degree = degree_span.get_text(strip=True) if degree_span else None

                # Decision and Date if given:
                tds = row.find_all("td")
                decision = tds[3].get_text(strip=True) if len(tds) > 3 else None

                # Date added to Grad Cafe
                added_on = tds[2].get_text(strip=True) if len(tds) > 2 else None


                if university and program:
                    entries.append({
                        "university": university,
                        "program": program,
                        "degree": degree,
                        "decision": decision,
                        "added_on": added_on
                    })

            except Exception:
                continue

        return entries

    def scrape_pages(self, start=1, end=2500):
        all_entries = []

        for page in range(start, end + 1):
            soup = self.fetch_page(page)
            if soup:
                page_entries = self.extract_entries(soup)
                all_entries.extend(page_entries)

        return all_entries

# Example usage
if __name__ == "__main__":
    scraper = ScrapeData()
    data = scraper.scrape_pages(start=1, end=1)  # test on 1 page
    print(data)

