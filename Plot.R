# Cleaning the environment
rm(list = ls())

# Loading the necessary libraries
library(corrplot)
library(psych)

# Setting the working directory
setwd("D:/UC3M/2nd year/2nd Semester/Data Protection and Cybersecurity")
getwd()

# PLOT: NUMBER_ATTRIBUTES V. TIME_ELAPSED

# Loading the dataset
time_vs_attributes <- read.table("time_vs_attributes.txt", sep = ",",
                                 dec = ".", header = FALSE)
colnames(time_vs_attributes) <- c("Number_attributes","Time_elapsed")

# Plotting the observation points
plot(time_vs_attributes$Number_attributes,time_vs_attributes$Time_elapsed,
main = "Encrypt-decrypt time w/ respect to the no. of attribs",
xlab = "Number of attributes", ylab = "Time elapsed (in seconds)")
# Plotting their interpolation
lines(spline(time_vs_attributes$Number_attributes,time_vs_attributes$Time_elapsed),col="green")
# Plotting a similar linear function
abline(a=2.192, b=0.139,col="red")
legend("topleft", legend=c("Interpolation of observations", "Linear function"),
       col=c("green", "red"), lty=1, cex=1)

# PLOT 2: NUMBER_ATTRIBUTES V. USER_0 (PRIVATE) KEY SIZE
time_vs_keys <- read.table("time_vs_priv_key_size.txt", sep = ",",
                                 dec = ".", header = FALSE)
colnames(time_vs_keys) <- c("Length_priv_keys","Time_elapsed")

# Plotting the observation points
plot(time_vs_keys$Length_priv_keys,time_vs_keys$Time_elapsed,
     main = "Encrypt-decrypt time w/ respect to the length of the priv. keys",
     xlab = "Length of private keys", ylab = "Time elapsed (in seconds)")
# Plotting their interpolation
lines(spline(time_vs_keys$Length_priv_keys,time_vs_keys$Time_elapsed),col="green")
# Plotting a similar linear function
abline(a=46.518, b=152.296,col="red")
legend("topleft", legend=c("Interpolation of observations", "Linear function"),
       col=c("green", "red"), lty=1, cex=1)

# PLOT 3: CORRELATIONS

# New unified dataset
unified <- time_vs_attributes
unified$Length_priv_keys = time_vs_keys$Length_priv_keys

# First correlation plot
cplot <- corrplot(cor(unified))
cplot

# Second correlation plot
cplot2 <- pairs.panels(unified)
cplot2
