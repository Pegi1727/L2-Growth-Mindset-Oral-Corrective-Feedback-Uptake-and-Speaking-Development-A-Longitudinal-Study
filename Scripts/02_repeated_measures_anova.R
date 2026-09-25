# Repeated-measures ANOVA and Bonferroni pairwise tests
if (!requireNamespace("pacman", quietly=TRUE)) install.packages("pacman")
pacman::p_load(tidyverse, rstatix)
df <- read.csv("Longitudinal_Data_120.csv")
id_col <- if ("ID" %in% names(df)) "ID" else if ("Learner_ID" %in% names(df)) "Learner_ID" else names(df)[1]
df_long <- df %>% pivot_longer(cols=c(Speaking_T1,Speaking_T2,Speaking_T3),names_to="Time",values_to="Speaking_Score") %>% mutate(Time=factor(Time,levels=c("Speaking_T1","Speaking_T2","Speaking_T3")))
print(anova_test(data=df_long,dv=Speaking_Score,wid=!!sym(id_col),within=Time) %>% get_anova_table())
print(df_long %>% pairwise_t_test(Speaking_Score~Time,paired=TRUE,p.adjust.method="bonferroni"))
