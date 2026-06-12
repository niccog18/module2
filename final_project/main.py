from pipeline import DataPipeline

pipeline = DataPipeline(
    "data/messy_employee_survey.csv"
)

results = pipeline.run()

print("\n=== Analysis Results ===")

for key, value in results.items():

    print(f"\n{key}")

    print(value)