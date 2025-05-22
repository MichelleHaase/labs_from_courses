raw_data <-read.csv("tests.tsv", sep="\t")

# gender:	Participant's reported gender (0 = Unanswered, 1 = Male, 2 = Female, 3 = Other)
raw_data$gender <-factor(raw_data$gender, labels = c("Unanswered", "Male", "Female", "Other"))

raw_data$extroversion <-round(((raw_data$E1 + raw_data$E2 + raw_data$E3)/15), 2)
raw_data$neuroticism <-round(((raw_data$N1 + raw_data$N2 + raw_data$N3)/15), 2)
raw_data$agreeableness <-round(((raw_data$A1 + raw_data$A2 + raw_data$A3)/15), 2)
raw_data$conscientiousness <-round(((raw_data$C1 + raw_data$C2 + raw_data$C3)/15), 2)
raw_data$openness <-round(((raw_data$O1 + raw_data$O2 + raw_data$O3)/15), 2)

write.csv(raw_data, file= "analysis.csv")