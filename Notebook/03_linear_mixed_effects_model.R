# Linear mixed-effects model of speaking trajectory
if (!requireNamespace("pacman", quietly=TRUE)) install.packages("pacman")
pacman::p_load(tidyverse,lme4,lmerTest,emmeans)
df <- read.csv("Longitudinal_Data_120.csv")
id_col <- if ("ID" %in% names(df)) "ID" else if ("Learner_ID" %in% names(df)) "Learner_ID" else names(df)[1]
df_long <- df %>% pivot_longer(cols=c(Speaking_T1,Speaking_T2,Speaking_T3),names_to="Time",values_to="Speaking_Score") %>% mutate(Time=factor(Time,levels=c("Speaking_T1","Speaking_T2","Speaking_T3")))
form <- as.formula(paste("Speaking_Score ~ Time * Growth_Mindset + Proficiency + (1 |",id_col,")"))
fit <- lmer(form,data=df_long); print(summary(fit))
print(emmeans(fit,~Time|Growth_Mindset,at=list(Growth_Mindset=mean(df$Growth_Mindset)+sd(df$Growth_Mindset)*c(-1,0,1))))
