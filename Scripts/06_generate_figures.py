"""Create 300-dpi longitudinal trajectory and mindset/uptake figures."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_all_plots(data_path="Longitudinal_Data_120.csv"):
    df=pd.read_csv(data_path)
    plt.rcParams["axes.edgecolor"]="#333333"
    times=["T1 (Baseline)","T2 (Immediate)","T3 (Delayed)"]
    cols=["Speaking_T1","Speaking_T2","Speaking_T3"]
    means=[df[c].mean() for c in cols]; stds=[df[c].std() for c in cols]
    fig,ax=plt.subplots(figsize=(7,5),dpi=300)
    ax.errorbar(times,means,yerr=stds,fmt="-o",color="#1f77b4",lw=2.5,capsize=5,markersize=8)
    ax.set_ylabel("Speaking Competence Score",fontweight="bold"); ax.set_title("Figure 1: Trajectory of Speaking Performance")
    fig.tight_layout(); fig.savefig("Figure_1_Generated.png",dpi=300); plt.close(fig)
    fig,ax=plt.subplots(figsize=(6,5),dpi=300)
    sns.regplot(x="Growth_Mindset",y="Feedback_Uptake",data=df,color="#2ca02c",scatter_kws={"alpha":.6},line_kws={"lw":2},ax=ax)
    ax.set_xlabel("L2 Growth Mindset Score",fontweight="bold"); ax.set_ylabel("Corrective Feedback Uptake Rate",fontweight="bold"); ax.set_title("Figure 2: Mindset vs Feedback Uptake")
    fig.tight_layout(); fig.savefig("Figure_2_Generated.png",dpi=300); plt.close(fig)
    print("Figures saved at 300 DPI.")

if __name__ == "__main__": generate_all_plots()
