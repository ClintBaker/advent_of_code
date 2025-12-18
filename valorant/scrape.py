from playwright.sync_api import sync_playwright
import csv
import time
URLS = ['https://www.vlr.gg/event/stats/2282/valorant-masters-toronto-2025','https://www.vlr.gg/event/stats/2281/valorant-masters-bangkok-2025','https://www.vlr.gg/event/stats/1999/champions-tour-2024-masters-shanghai','https://www.vlr.gg/event/stats/1921/champions-tour-2024-masters-madrid','https://www.vlr.gg/event/stats/1494/champions-tour-2023-masters-tokyo','https://www.vlr.gg/event/stats/1188/champions-tour-2023-lock-in-s-o-paulo','https://www.vlr.gg/event/stats/1657/valorant-champions-2023','https://www.vlr.gg/event/stats/2097/valorant-champions-2024', 'https://www.vlr.gg/event/stats/2283/valorant-champions-2025']
URL = URLS[5]
FILENAME = 'lock_in.csv'

def scrape_vlr_event_stats():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=50)
        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        )

        # Load page and wait for the stats table to appear
        page.goto(URL, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_timeout(2000)  # small buffer
        page.wait_for_selector("table.wf-table")  # VLR uses this class for tables

        data = page.evaluate(
            """
            () => {
              // Grab the first VLR table on the page.
              // If there are multiple, you can refine this later with more specific selectors.
              const statsTable = document.querySelector("table.wf-table");
              if (!statsTable) {
                return { headers: [], rows: [] };
              }

              const rows = Array.from(statsTable.querySelectorAll("tr"))
                .filter(r => r.querySelectorAll("th, td").length > 0);

              if (rows.length === 0) {
                return { headers: [], rows: [] };
              }

              // Assume the first non-empty row is the header row
              const headerCells = Array.from(rows[0].querySelectorAll("th, td"));
              const headers = headerCells.map(c =>
                c.textContent.trim().replace(/\\s+/g, " ")
              );

              const dataRows = [];

              for (const row of rows.slice(1)) {
                const cells = Array.from(row.querySelectorAll("td"));
                if (!cells.length) continue;

                const obj = {};
                for (let i = 0; i < Math.min(cells.length, headers.length); i++) {
                  const header = headers[i] || `col_${i}`;
                  const value = cells[i].textContent.trim().replace(/\\s+/g, " ");
                  obj[header] = value;
                }

                // Filter out totally empty rows
                const hasAnyValue = Object.values(obj).some(v => v && v.length > 0);
                if (hasAnyValue) {
                  dataRows.push(obj);
                }
              }

              return { headers, rows: dataRows };
            }
            """
        )

        browser.close()
        return data


def save_to_csv(data, filename=FILENAME):
    headers = data["headers"]
    rows = data["rows"]

    if not headers or not rows:
        print("No data found – check selectors or page structure.")
        return

    # Ensure "Player" is first, just for readability (optional)
    if "Player" in headers:
        headers = ["Player"] + [h for h in headers if h != "Player"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"Saved {len(rows)} rows to {filename}")


if __name__ == "__main__":
    scraped = scrape_vlr_event_stats()
    print("Headers:", scraped["headers"])
    print("First 3 rows:")
    for r in scraped["rows"][:3]:
        print(r)
    save_to_csv(scraped)
