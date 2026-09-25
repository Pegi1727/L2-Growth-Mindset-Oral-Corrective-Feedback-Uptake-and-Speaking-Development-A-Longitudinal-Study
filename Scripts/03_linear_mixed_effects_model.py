"""Linear mixed-effects model of speaking trajectory and growth mindset."""
import pandas as pd
import statsmodels.formula.api as smf

def run_lmm(data_path="Longitudinal_Data_120.csv"):
    df=pd.read_csv(data_path)
    id_var="ID" if "ID" in df.columns else ("Learner_ID" if "Learner_ID" in df.columns else df.columns[0])
    long=df.melt(id_vars=[id_var,"Growth_Mindset","Proficiency"],value_vars=["Speaking_T1","Speaking_T2","Speaking_T3"],var_name="TimePoint",value_name="Speaking_Score")
    long["Time_Num"]=long.TimePoint.map({"Speaking_T1":0,"Speaking_T2":1,"Speaking_T3":2})
    result=smf.mixedlm("Speaking_Score ~ Time_Num * Growth_Mindset + Proficiency",data=long,groups=long[id_var]).fit()
    print(result.summary())

if __name__ == "__main__": run_lmm()
