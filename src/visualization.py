from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.lines import Line2D


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Input file
CLEANED_DATA_FILE = (
    PROJECT_ROOT / "data" / "processed" / "cleaned_sales_data.csv"
)

# Output directory
FIGURES_DIR = PROJECT_ROOT / "outputs" / "figures"


def load_cleaned_data():
    """Load the cleaned sales dataset."""

    df = pd.read_csv(CLEANED_DATA_FILE)

    return df


def create_sales_histogram(df):
    """Create and save a histogram showing the distribution of Sales."""

    plt.figure(figsize=(10, 6))

    plt.hist(df["Sales"], bins=50)

    plt.xlabel("Sales")
    plt.ylabel("Frequency")
    plt.title("Distribution of Sales")

    output_file = FIGURES_DIR / "sales_histogram.png"

    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"Sales histogram saved to: {output_file}")


def create_profit_boxplot(df):
    """Create and save a box plot of Profit by Product Category."""

    plt.figure(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x="Category",
        y="Profit"
    )

    plt.xlabel("Product Category")
    plt.ylabel("Profit")
    plt.title("Profit Distribution by Product Category")

    output_file = FIGURES_DIR / "profit_boxplot.png"

    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"Profit box plot saved to: {output_file}")


def create_sales_profit_scatter(df):
    """Create and save a scatter plot of Sales vs Profit by Category."""

    category_colors = {
        "Furniture": 0,
        "Office Supplies": 1,
        "Technology": 2
    }

    colors = df["Category"].map(category_colors)

    plt.figure(figsize=(10, 6))

    plt.scatter(
        df["Sales"],
        df["Profit"],
        c=colors,
        alpha=0.7
    )

    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.title("Sales vs Profit by Product Category")

    legend_elements = [
        Line2D(
            [0],
            [0],
            marker="o",
            linestyle="",
            label=category,
            markerfacecolor=plt.cm.viridis(color_value / 2),
            markeredgecolor="none"
        )
        for category, color_value in category_colors.items()
    ]

    plt.legend(
        handles=legend_elements,
        title="Product Category"
    )

    output_file = FIGURES_DIR / "sales_profit_scatter.png"

    plt.savefig(
        output_file,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"Sales vs Profit scatter plot saved to: {output_file}")


def create_all_visualizations():
    """Create all required assignment visualizations."""

    # Make sure the output directory exists
    FIGURES_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # Load cleaned data
    df = load_cleaned_data()

    print("Cleaned dataset loaded successfully.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print()

    # Create all three visualizations
    create_sales_histogram(df)
    create_profit_boxplot(df)
    create_sales_profit_scatter(df)

    print()
    print("All visualizations created successfully.")


if __name__ == "__main__":
    create_all_visualizations()