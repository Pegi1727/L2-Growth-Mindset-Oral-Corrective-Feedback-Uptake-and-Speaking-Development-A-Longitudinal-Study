# Multiple regressions and variance inflation factors
if (!requireNamespace("pacman", quietly=TRUE)) install.packages("pacman")
pacman::p_load(car)
df <- read.csv("Longitudinal_Data_120.csv")
m1 <- lm(Feedback_Uptake ~ Growth_Mindset + Proficiency,data=df); cat("=== MODEL 1 ===\n"); print(summary(m1))
m2 <- lm(Speaking_T3 ~ Feedback_Uptake + Growth_Mindset + Speaking_T1 + Proficiency,data=df); cat("=== MODEL 2 ===\n"); print(summary(m2)); cat("=== VIF ===\n"); print(car::vif(m2))
