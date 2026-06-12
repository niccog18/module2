# Data Processing Pipeline
import os
import re

import pandas as pd
import numpy as np

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

# Step 1: Class pipelines
class DataPipeline:

    DEPT_MAP = {
        "engineering": "Engineering",
        "eng": "Engineering",
        "marketing": "Marketing",
        "mktg": "Marketing",
        "sales": "Sales",
        "hr": "HR",
        "human resources": "HR",
        "h.r.": "HR",
        "finance": "Finance",
        "fin": "Finance"
    }

    LOC_MAP = {
        "new york": "New York",
        "nyc": "New York",
        "chicago": "Chicago",
        "chi": "Chicago",
        "austin": "Austin",
        "austin, tx": "Austin",
        "atx": "Austin",
        "seattle": "Seattle",
        "sea": "Seattle",
        "remote": "Remote",
        "work from home": "Remote"
    }

    def __init__(self, filepath):

        self.filepath = filepath
        self.df = None

        try:

            self.df = pd.read_csv(filepath)

            print(
                f"Loaded {self.df.shape[0]} rows and "
                f"{self.df.shape[1]} columns."
            )

        except FileNotFoundError:

            print(f"File not found: {filepath}")

        except Exception as e:

            print(f"Error loading file: {e}")

# Step 2: Clean data
    def clean(self):

        df = self.df.copy()

        original_rows = len(df)

    # Track cleaning metrics
        missing_before = df.isna().sum().sum()

        negative_salaries_fixed = 0
        invalid_scores_fixed = 0
        experience_outliers_fixed = 0

        # Remove duplicate employee IDs
        df = df.drop_duplicates(
            subset=["employee_id"],
            keep="first"
        )

        duplicates_removed = (
            original_rows - len(df)
        )

        # Clean names
        df["name"] = df["name"].str.strip()
        df["name"] = df["name"].str.title()

        # Clean departments
        df["department"] = df["department"].str.strip()
        df["department"] = df["department"].str.lower()
        df["department"] = df["department"].map(self.DEPT_MAP)

        # Clean office locations
        df["office_location"] = (
            df["office_location"].str.strip()
        )

        df["office_location"] = (
            df["office_location"].str.lower()
        )

        df["office_location"] = (
            df["office_location"].map(
                self.LOC_MAP
            )
        )

        # Count negative salaries
        salary_numeric = pd.to_numeric(
            df["salary"]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False),
            errors="coerce"
        )

        negative_salaries_fixed = (
            salary_numeric < 0
        ).sum()

        # Salary helper
        def clean_salary(value):
            try:
                value = re.sub(
                    r"[$,]",
                    "",
                    str(value)
                )
                value = float(value)
                if value < 0:
                    return None
                return value
            except:
                return None

        df["salary"] = df["salary"].apply(
            clean_salary
        )

        # Years experience
        df["years_experience"] = (
            pd.to_numeric(
                df["years_experience"],
                errors="coerce"
            )
        )

        experience_outliers_fixed = (
            df["years_experience"] > 50
        ).sum()

        df.loc[
            df["years_experience"] > 50,
            "years_experience"
        ] = np.nan

        # Satisfaction score
        df["satisfaction_score"] = (
            pd.to_numeric(
                df["satisfaction_score"],
                errors="coerce"
            )
        )

        invalid_scores_fixed = (
            ~df["satisfaction_score"].between(
                1,
                10
            )
        ).sum()

        df.loc[
            ~df["satisfaction_score"].between(
                1,
                10
            ),
            "satisfaction_score"
        ] = np.nan

        # Date helper
        def parse_date(value):

            formats = [
                "%m/%d/%Y",
                "%Y-%m-%d",
                "%d-%m-%Y"
            ]
            for fmt in formats:
                try:
                    return pd.to_datetime(
                        value,
                        format=fmt
                    )
                except:
                    continue
            return pd.NaT

        df["survey_date"] = (
            df["survey_date"].apply(
                parse_date
            )
        )

        # Missing value strategy
        df["salary"] = (
            df["salary"].fillna(
                df["salary"].median()
            )
        )

        df["years_experience"] = (
            df["years_experience"].fillna(
                df["years_experience"].median()
            )
        )

        df["satisfaction_score"] = (
            df["satisfaction_score"].fillna(
                df["satisfaction_score"].median()
            )
        )

        df["comments"] = (
            df["comments"].fillna(
                "No Comment"
            )
        )

        # Calculate fixed missing values
        missing_after = (
            df.isna().sum().sum()
        )

        missing_fixed = (
            missing_before - missing_after
        )

        self.df = df

        print("\n=== Cleaning Summary ===")

        print(
            f"Removed {duplicates_removed} duplicate rows."
        )

        print(
            f"Fixed {missing_fixed} missing values."
        )

        print(
            f"Corrected {negative_salaries_fixed} negative salaries."
        )

        print(
            f"Corrected {invalid_scores_fixed} invalid satisfaction scores."
        )

        print(
            f"Corrected {experience_outliers_fixed} experience outliers."
        )

        print("\nRemaining Missing Values:")

        print(df.isna().sum())

        return self
    
# Step 3: Analyse data
    def analyze(self):

        df = self.df

        avg_salary_by_dept = (
            df.groupby("department")
            ["salary"]
            .mean()
            .round(0)
        )

        avg_satisfaction_by_dept = (
            df.groupby("department")
            ["satisfaction_score"]
            .mean()
            .round(2)
        )

        headcount_by_location = (
            df["office_location"]
            .value_counts()
        )

        corr_df = df[
            [
                "salary",
                "years_experience"
            ]
        ]

        corr_df = corr_df.dropna()

        experience_salary_correlation = (
            corr_df["salary"].corr(
                corr_df["years_experience"]
            )
        )

        avg_satisfaction_by_location = (
            df.groupby("office_location")
            ["satisfaction_score"]
            .mean()
            .round(2)
        )

        results = {

            "avg_salary_by_dept":
                avg_salary_by_dept.to_dict(),

            "avg_satisfaction_by_dept":
                avg_satisfaction_by_dept.to_dict(),

            "headcount_by_location":
                headcount_by_location.to_dict(),

            "experience_salary_correlation":
                experience_salary_correlation,

            "avg_satisfaction_by_location":
                avg_satisfaction_by_location.to_dict()
        }

        return results
    
# Step 4: Visualize
    def visualize(
        self,
        output_path="output/charts.png"
    ):

        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True
        )

        fig, axes = plt.subplots(
            3,
            1,
            figsize=(10, 14)
        )

        avg_salary = (
            self.df.groupby("department")
            ["salary"]
            .mean()
        )

        avg_salary.plot(
            kind="bar",
            ax=axes[0]
        )

        axes[0].set_title(
            "Average Salary by Department"
        )

        self.df[
            "satisfaction_score"
        ].plot(
            kind="hist",
            bins=10,
            ax=axes[1]
        )

        axes[1].set_title(
            "Satisfaction Distribution"
        )

        location_counts = (
            self.df["office_location"]
            .value_counts()
        )

        location_counts.plot(
            kind="barh",
            ax=axes[2]
        )

        axes[2].set_title(
            "Headcount by Location"
        )

        plt.tight_layout()

        plt.savefig(
            output_path,
            dpi=120,
            bbox_inches="tight"
        )

        plt.close()

        print(
            f"Charts saved to "
            f"{output_path}"
        )

# Step 5: Export and run
    def export(
        self,
        output_path="output/clean_employees.csv"
    ):

        try:

            os.makedirs(
                os.path.dirname(
                    output_path
                ),
                exist_ok=True
            )

            self.df.to_csv(
                output_path,
                index=False
            )

            print(
                f"Data exported to "
                f"{output_path}"
            )

        except Exception as e:

            print(
                f"Export failed: {e}"
            )
    def run(self):

        output_dir = os.path.join(
            os.path.dirname(__file__),
            "output"
        )

        chart_path = os.path.join(
            output_dir,
            "charts.png"
        )

        csv_path = os.path.join(
            output_dir,
            "clean_employees.csv"
        )

        self.clean()

        results = self.analyze()

        self.visualize(chart_path)

        self.export(csv_path)

        return results

