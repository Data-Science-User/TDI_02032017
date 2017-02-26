## Libraries
library(plyr)

## Read CSV
df <-read.csv("PartD_Prescriber_PUF_NPI_14.txt", sep="\t", header=TRUE)

## Q1: In 2014, what was the average number of beneficiaries per provider? 
## Due to the suppression of data for those with view beneficiaries, we can only 
## include those with more than 10 beneficiaries.
count(df, 'NPI') # Check for duplicates

mean(df[df$BENE_COUNT >= 10, ],na.rm = TRUE) 
# The average number of beneficiaries per provider is 148.5

## Q2: For each provider, estimate the length of the average prescription from 
## the TOTAL_DAY_SUPPLY and TOTAL_CLAIM_COUNT. What is the median, in days, of the 
## distribution of this value across all providers?

median(df$TOTAL_CLAIM_COUNT/df$TOTAL_DAY_SUPPLY)
# The median distribution of average prescription's length across all providers is 0.03435978 days.

## Q3: Work out for each Specialty the fraction of drug claims that are for brand-name drugs. 
## Include only providers for whom the relevant information has not been suppressed, and 
## consider only specialties with at least 1000 total claims. What is the standard deviation 
## of these fractions?



## Q4: Find the ratio of beneficiaries with opioid prescriptions to beneficiaries with 
## antibiotics prescriptions in each state. Assume that each beneficiary attends only a 
## single provider. What is the difference between the largest and smallest ratios?

aggregate(OPIOID_BENE_COUNT/ANTIBIOTIC_BENE_COUNT ~ NPPES_PROVIDER_STATE, df, sum)
# The difference between the largest and smallest ratios is 39.62441.


## Q5: For each provider where the relevant columns are not suppressed, work out the 
## fraction of claims for beneficiaries age 65 and older, as well as the fraction of 
## claims for beneficiaries with a low-income subsidy. What is the Pearson correlation 
## coefficient between these values?
sub<-df[,c("BENE_COUNT_GE65","LIS_CLAIM_COUNT")]
c<-sub[complete.cases(sub),]
a<-as.vector(df$BENE_COUNT_GE65)
b<-as.vector(df$LIS_CLAIM_COUNT)
cor(a,b,use='complete.obs')

## Q6: Let's find which states have surprisingly high supply of opioids, conditioned 
## on specialty. Work out the average length of an opioid prescription for each provider. 
## For each (state, specialty) pair with at least 100 providers, calculate the average of 
## this value across all providers. Then find the ratio of this value to an equivalent 
## quantity calculated from providers in each specialty across all states. What is the 
## largest such ratio?


NPI
OPIOID_CLAIM_COUNT    NPPES_PROVIDER_STATE
