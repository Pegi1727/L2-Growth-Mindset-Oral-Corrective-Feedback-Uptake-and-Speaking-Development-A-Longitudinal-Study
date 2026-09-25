"""OLS regressions predicting feedback uptake and T3 speaking, with VIF diagnostics."""
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

def run_regression_and_vif(data_path="Longitudinal_Data_120.csv"):
    df=pd.read_csv(data_path)
    x1=sm.add_constant(df[["Growth_Mindset","Proficiency"]]); m1=sm.OLS(df["Feedback_Uptake"],x1).fit()
    print("MODEL 1: FEEDBACK UPTAKE
",m1.summary())
    cols=["Feedback_Uptake","Growth_Mindset","Speaking_T1","Proficiency"]
    x2=sm.add_constant(df[cols]); m2=sm.OLS(df["Speaking_T3"],x2).fit()
    print("
MODEL 2: T3 SPEAKING
",m2.summary())
    print("
VIF
",pd.DataFrame({"Feature":cols,"VIF":[variance_inflation_factor(df[cols].values,i) for i in range(len(cols))]}).round(2))

if __name__ == "__main__": run_regression_and_vif()
