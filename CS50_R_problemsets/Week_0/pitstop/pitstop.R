# bahrain <-read.csv("bahrain.csv")
# imola <-read.csv("imola.csv")
# jeddah <-read.csv("jeddah.csv")
# melbourne <-read.csv("melbourne.csv")
# miami <-read.csv("miami.csv")
# shanghai <-read.csv("shanghai.csv")
# suzuka <-read.csv("suzuka.csv")
#
# bahrain$location <-"bahrain"
# imola$location <-"imola"
# jeddah$location <-"jeddah"
# melbourne$location <-"melbourne"
# miami$location <-"miami"
# shanghai$location <-"shanghai"
# suzuka$location <-"suzuka"
#
# F1_data <-rbind(bahrain, imola, jeddah, melbourne, miami, shanghai, suzuka)
#
# query

filename <- readline("What file would you like to be analised? ")
file <- read.csv(filename)

total_stops <-nrow(file)
shortest <-min(file$time)
longest <-max(file$time)
total_time <-sum(file$time)

result <- paste0("total stops made: ", total_stops, "\n", "shortest stop: ", shortest, "\n", "longest stop: ", longest, "\n", "total time in stops: ", total_time)
cat(result)