"""Bootstrap indirect effect: mindset -> feedback uptake -> T3 speaking."""
import numpy as np
import pandas as pd
import statsmodels.api as sm

def run_bootstrap_mediation(data_path="Longitudinal_Data_120.csv",n_boot=5000,seed=42):
    df=pd.read_csv(data_path); rng=np.random.default_rng(seed); n=len(df); effects=[]
    for _ in range(n_boot):
        s=df.iloc[rng.integers(0,n,n)]
        xa=sm.add_constant(s[["Growth_Mindset","Speaking_T1","Proficiency"]]); ya=s["Feedback_Uptake"]
        xb=sm.add_constant(s[["Feedback_Uptake","Growth_Mindset","Speaking_T1","Proficiency"]]); yb=s["Speaking_T3"]
        a=sm.OLS(ya,xa).fit().params["Growth_Mindset"]
        b=sm.OLS(yb,xb).fit().params["Feedback_Uptake"]
        effects.append(a*b)
    point=float(np.mean(effects)); lo,hi=np.percentile(effects,[2.5,97.5])
    print(f"Indirect effect (ab): {point:.3f}
95% percentile bootstrap CI: [{lo:.3f}, {hi:.3f}]")

if __name__ == "__main__": run_bootstrap_mediation()
