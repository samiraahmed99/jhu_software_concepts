from scrape import ScrapeData
import json

# Instantiate and scrape data
scraper = ScrapeData()
data = scraper.scrape_pages(start=1, end=500)

# Export to JSON
with open("applicant_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Exported {len(data)} entries to applicant_data.json")