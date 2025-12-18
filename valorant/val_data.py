import csv

def load_vlr_stats(csv_file="vlr_champions_2025_stats.csv"):
    data = []
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert empty strings to None if desired
            cleaned_row = {k: (v if v != "" else None) for k, v in row.items()}
            data.append(cleaned_row)
    return data

if __name__ == "__main__":
    stats = load_vlr_stats()
    print(f"Loaded {len(stats)} rows")

    # print first 3 rows as preview
    for row in stats[:3]:
        print(row)
