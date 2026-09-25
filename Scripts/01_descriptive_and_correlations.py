"""Descriptive statistics and Pearson/Spearman correlations for the L2 longitudinal study."""
import pandas as pd

def run_descriptives(data_path="Longitudinal_Data_120.csv"):
    df = pd.read_csv(data_path)
    cols = [c for c in df.select_dtypes(include="number").columns if c not in ("ID", "Learner_ID")]
    desc = df[cols].describe().T
    desc["skewness"] = df[cols].skew()
    desc["kurtosis"] = df[cols].kurtosis()
    print(f"Participants: {len(df)}
", df.head())
    print("
DESCRIPTIVES
", desc.round(3))
    for method in ("pearson", "spearman"):
        corr = df[cols].corr(method=method)
        print(f"
{method.upper()} CORRELATIONS
", corr.round(3))
        corr.to_csv(f"{method}_correlation_matrix.csv")
    desc.to_csv("descriptive_statistics.csv")

if __name__ == "__main__":
    run_descriptives()
