import pandas as pd
import matplotlib.pyplot as plt

#ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = "../data/exoplanets.csv"
OUTPUT_PATH = "../reports/"

# NASA Exoplanet Archive export includes 96 lines of metadata before
# the actual CSV header row.
SKIP_ROWS = 96

def load_data(path, skip_rows):
    #from pathlib import Path

    #path = Path("../data/exoplanets.csv")  # or use your DATA_PATH

    #with open(path, "r", encoding="utf-8") as f:
    #    for i in range(100):
    #        line = f.readline()
    #        if 88 <= i <= 98:
    #            print(f"{i+1}: {repr(line)}")

    #print(path)
    #print(path.exists())

    df = pd.read_csv(path, skiprows=skip_rows)
    return df

def plot_discovery_methods(df):
    plt.figure()

    df["discoverymethod"].value_counts().head(10).plot(kind="bar")

    plt.title("Exoplanet Discovery Methods")
    plt.tight_layout()

    plt.savefig("../reports/discovery_methods.png")
    plt.close()

def main():
    df = load_data(DATA_PATH, SKIP_ROWS)

    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    plot_discovery_methods(df)

    print("Report saved to /reports")


if __name__ == "__main__":
    main()