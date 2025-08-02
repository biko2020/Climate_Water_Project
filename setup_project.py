import os
import pandas as pd

from config.regions import moroccan_regions
from config.regions import clean_filename

# Create folders for project structure
def setup_folders():
    folders = [
        "data/raw", "data/processed", "data/final",
        "analysis", "visualizations", "documentation", "results"
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

# Generate a CSV template for each region
def create_csv_templates(regions_dict):
    for region, (lat, lon) in regions_dict.items():
        filename = clean_filename(region) + ".csv"
        filepath = os.path.join("data/raw", f"spei_{filename}")
        df = pd.DataFrame(columns=["date", "SPEI"])
        df.to_csv(filepath, index=False)

# Print region info for manual download
def print_download_instructions(regions_dict):
    instructions = []
    for region, (lat, lon) in regions_dict.items():
        instructions.append(f"- {region}: Latitude = {lat}, Longitude = {lon}")
    instruction_text = "\n".join(instructions)

    guide_path = os.path.join("documentation", "manual_download_guide.md")
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write("# Manual SPEI Data Download Guide\n\n")
        f.write("Follow these steps for each region:\n\n")
        f.write("1. Visit [https://spei.csic.es/map/maps.html](https://spei.csic.es/map/maps.html)\n")
        f.write("2. Choose 'SPEI-12' as the timescale.\n")
        f.write("3. Input the coordinates listed below.\n")
        f.write("4. Select time range: January 2000 – December 2024.\n")
        f.write("5. Export as CSV and save it to `data/raw/` with the name `spei_<region>.csv`\n\n")
        f.write("### Region Coordinates:\n\n")
        f.write(instruction_text)

# Main setup function
def setup_project():
    print("Setting up Climate_Water_Project...")
    setup_folders()
    create_csv_templates(moroccan_regions)
    print_download_instructions(moroccan_regions)
    print("Project structure and CSV templates created.")
    print("Manual download instructions saved in documentation/manual_download_guide.md")

# Entry point
if __name__ == "__main__":
    setup_project()
