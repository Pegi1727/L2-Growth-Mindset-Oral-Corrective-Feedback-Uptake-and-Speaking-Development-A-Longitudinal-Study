"""Paired comparisons across speaking T1, T2, and T3 with Bonferroni adjustment."""
import pandas as pd
from scipy import stats

def run_rm_anova(data_path="Longitudinal_Data_120.csv"):
    df = pd.read_csv(data_path)
    pairs = [("T1", "T2", "Speaking_T1", "Speaking_T2"), ("T2", "T3", "Speaking_T2", "Speaking_T3"), ("T1", "T3", "Speaking_T1", "Speaking_T3")]
    results=[]
    for a,b,x,y in pairs:
        diff=df[y]-df[x]
        t,p=stats.ttest_rel(df[x],df[y],nan_policy="omit")
        dz=diff.mean()/diff.std(ddof=1)
        results.append((f"{a} vs {b}",diff.mean(),t,p,dz))
    m=len(results)
    print("Pairwise paired t tests; Bonferroni-adjusted p values")
    for label,mean_diff,t,p,dz in results:
        print(f"{label}: mean change={mean_diff:.3f}, t={t:.3f}, p_adj={min(p*m,1):.4g}, dz={dz:.3f}")

if __name__ == "__main__": run_rm_anova()
