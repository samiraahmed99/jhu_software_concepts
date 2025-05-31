## robots.txt Compliance

Scraper complies with `robots.txt` rules from TheGradCafe.

### Paths Checked: `/survey/`
- `robots.txt` does **not** disallow `/survey/` for any user-agent.
- Only `/cgi-bin/` and `/index-ad-test.php` are disallowed.
- Therefore, accessing `/survey/?page=1` to `/survey/?page=500` is allowed.

### Screenshot Evidence
See ![Screen Shot of ](robot_sc.png) showing the full screenshot that we comply with `robots.txt` file.

### Code Evidence
Below is the Python code used to programmatically verify this which is also located in `check_robots.py`

### Python Code (Compliance Check)

```python
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