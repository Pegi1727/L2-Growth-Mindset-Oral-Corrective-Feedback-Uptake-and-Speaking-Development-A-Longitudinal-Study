# Publication-style figure for mindset and feedback uptake
if (!requireNamespace("pacman", quietly=TRUE)) install.packages("pacman")
pacman::p_load(ggplot2)
df <- read.csv("Longitudinal_Data_120.csv")
theme_apa7 <- theme_classic(base_size=12)+theme(axis.text=element_text(color="black"),axis.title=element_text(face="bold"),legend.position="top")
p <- ggplot(df,aes(Growth_Mindset,Feedback_Uptake))+geom_point(color="#2E7D32",alpha=.6,size=2.5)+geom_smooth(method="lm",color="#1B5E20",fill="#A5D6A7")+labs(title="Figure 2. L2 Growth Mindset and Feedback Uptake Rate",x="L2 Growth Mindset Score",y="Corrective Feedback Uptake Rate")+theme_apa7
ggsave("Figure_2_R_ggplot2.png",plot=p,width=6,height=5,dpi=300)
