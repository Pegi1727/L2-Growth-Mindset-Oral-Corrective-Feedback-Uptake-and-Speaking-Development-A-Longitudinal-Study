# Descriptive statistics and Pearson correlations
if (!requireNamespace("pacman", quietly=TRUE)) install.packages("pacman")
pacman::p_load(tidyverse, psych, Hmisc)
df <- read.csv("Longitudinal_Data_120.csv")
cat("=== SAMPLE ===\n"); print(glimpse(df))
num_df <- df %>% select(where(is.numeric), -any_of(c("ID","Learner_ID")))
cat("=== DESCRIPTIVES ===\n"); print(round(psych::describe(num_df)[,c("n","mean","sd","median","min","max","skew","kurtosis")],3))
r <- Hmisc::rcorr(as.matrix(num_df), type="pearson")
cat("=== PEARSON R ===\n"); print(round(r$r,3)); cat("=== P VALUES ===\n"); print(round(r$P,3))
