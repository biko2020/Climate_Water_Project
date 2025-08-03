import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
import seaborn as sns

def load_all_spei_data(data_folder):
    all_files = glob.glob(os.path.join(data_folder, "*.csv"))
    df_list = []

    for file in all_files:
        region_name = os.path.basename(file).replace("spei_", "").replace("_2000_2024.csv", "")
        df = pd.read_csv(file, parse_dates=["date"])
        df["region"] = region_name
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

if __name__ == "__main__":
    raw_path = "data/raw"
    df = load_all_spei_data(raw_path)

    # Save combined file
    df.to_csv("data/processed/combined_spei_data.csv", index=False)
    print("Combined SPEI data saved to data/processed/combined_spei_data.csv")

    # Plotting
    sns.set(style="whitegrid")
    plt.figure(figsize=(14, 6))

    for region in df["region"].unique():
        regional_data = df[df["region"] == region]
        plt.plot(regional_data["date"], regional_data["SPEI"], label=region)

    plt.title("SPEI Trends (2000–2024)")
    plt.xlabel("Year")
    plt.ylabel("SPEI")
    plt.legend(loc="upper right", ncol=2)
    plt.tight_layout()
    plt.savefig("visualizations/spei_trends_by_region.png")
    plt.show()
