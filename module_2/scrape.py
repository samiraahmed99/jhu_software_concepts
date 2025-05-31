import requests
from bs4 import BeautifulSoup
import re

# Scrape Data:
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

        table = soup.find("table")
        if not table:
            return entries

        rows = table.find_all("tr")
        i = 0

        while i < len(rows) - 1:
            main_row = rows[i]
            badge_row = rows[i + 1]

            # Skip rows without valid university divs (ads/comments)
            university_div = main_row.select_one("td div div.tw-font-medium")
            if not university_div:
                i += 1
                continue

            # Initialize fields
            university = program = degree = decision = added_on = None
            semester = nationality = gpa = gre = gre_v = gre_aw = comment = None

            # Main row parsing
            university = university_div.get_text(strip=True)

            program_span = main_row.select_one("td:nth-of-type(2) span")
            if program_span:
                program = program_span.get_text(strip=True)

            degree_span = main_row.select_one("span.tw-text-gray-500")
            if degree_span:
                degree = degree_span.get_text(strip=True)

            tds = main_row.find_all("td")
            if len(tds) > 3:
                decision = tds[3].get_text(strip=True)
            if len(tds) > 2:
                added_on = tds[2].get_text(strip=True)

            # Badge row parsing
            badges = badge_row.find_all("div", class_=lambda c: c and "tw-inline-flex" in c)
            for div in badges:
                text = div.get_text(strip=True).lower()

                if re.search(r"(fall|spring|summer)\s+\d{4}", text):
                    semester = text
                elif text in ["american", "international"]:
                    nationality = text
                elif "gpa" in text:
                    match = re.search(r"gpa\s+(\d\.\d+)", text)
                    if match:
                        gpa = match.group(1)
                elif re.search(r"gre\s*aw\s*([\d.]+)", text):
                    match = re.search(r"gre\s*aw\s*([\d.]+)", text)
                    if match:
                        gre_aw = match.group(1)
                elif re.search(r"gre\s*v\s*(\d{2,3})", text):
                    match = re.search(r"gre\s*v\s*(\d{2,3})", text)
                    if match:
                        gre_v = match.group(1)
                elif re.search(r"\bgre\s*(\d{2,3})", text) and "gre v" not in text and "gre aw" not in text:
                    match = re.search(r"\bgre\s*(\d{2,3})", text)
                    if match:
                        gre = match.group(1)

            # Comments:
            if i + 2 < len(rows):
                comment_row = rows[i + 2]
                comment_cell = comment_row.select_one("p.tw-text-gray-500.tw-text-sm.tw-my-0")
                if comment_cell:
                    comment = comment_cell.get_text(strip=True)

            # Applicant result URL
            result_url = None
            link_tag = main_row.select_one('a[href*="/result/"]')
            if link_tag:
                result_url = "https://www.thegradcafe.com" + link_tag['href']

            entries.append({
                "university": university,
                "program": program,
                "degree": degree,
                "decision": decision,
                "added_on": added_on,
                "semester": semester,
                "nationality": nationality,
                "gpa": gpa,
                "gre": gre,
                "gre_v": gre_v,
                "gre_aw": gre_aw,
                "comment": comment,
                "applicant_url": result_url
            })

            i += 2  # skip to the next entry
            # If we consumed a comment row, skip it too
            if i < len(rows):
                if rows[i].select_one("p.tw-text-gray-500.tw-text-sm.tw-my-0"):
                    i += 1

        return entries

    def scrape_pages(self, start=1, end=500):
        all_entries = []
        for page in range(start, end + 1):
            soup = self.fetch_page(page)
            if soup:
                page_entries = self.extract_entries(soup)
                all_entries.extend(page_entries)
        return all_entries


if __name__ == "__main__":
    scraper = ScrapeData()
    data = scraper.scrape_pages(start=1, end=500)
