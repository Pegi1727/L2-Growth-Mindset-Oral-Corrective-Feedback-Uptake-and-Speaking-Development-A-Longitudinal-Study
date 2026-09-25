# Bootstrap mediation model with lavaan
if (!requireNamespace("pacman", quietly=TRUE)) install.packages("pacman")
pacman::p_load(lavaan)
df <- read.csv("Longitudinal_Data_120.csv")
med_model <- '
 Feedback_Uptake ~ a*Growth_Mindset + Proficiency + Speaking_T1
 Speaking_T3 ~ b*Feedback_Uptake + cp*Growth_Mindset + Proficiency + Speaking_T1
 indirect := a*b
 total := cp + (a*b)
'
fit <- sem(med_model,data=df,se="bootstrap",bootstrap=1000)
print(summary(fit,standardized=TRUE,ci=TRUE,rsquare=TRUE))
