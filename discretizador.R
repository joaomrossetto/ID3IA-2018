library("RWeka")

adult <- read.csv("adult.data.txt")
y1 <- Discretize(X50k.year ~. , data = adult, )

#Removendo formatações deixadas pela função Discretize

y1$age <- gsub("\\'", "", y1$age)
y1$age <- gsub("[:(:]", "", y1$age)
y1$age <- gsub("\\]", "", y1$age)

y1$fnlwgt <- gsub("\\'", "", y1$fnlwgt)

y1$education.num <- gsub("\\'", "", y1$education.num)
y1$education.num <- gsub("[:(:]", "", y1$education.num)
y1$education.num <- gsub("\\]", "", y1$education.num)

y1$capital.gain <- gsub("\\'", "", y1$capital.gain)
y1$capital.gain <- gsub("[:(:]", "", y1$capital.gain)
y1$capital.gain <- gsub("\\]", "", y1$capital.gain)

y1$capital.loss <- gsub("\\'", "", y1$capital.loss)
y1$capital.loss <- gsub("[:(:]", "", y1$capital.loss)
y1$capital.loss <- gsub("\\]", "", y1$capital.loss)

y1$hours.per.week <- gsub("\\'", "", y1$hours.per.week)
y1$hours.per.week <- gsub("[:(:]", "", y1$hours.per.week)
y1$hours.per.week <- gsub("\\]", "", y1$hours.per.week)

# Fim da Remoção

#A coluna fnlwgt não auxilia a classificação e é retirada
y1 <- subset( y1, select = -fnlwgt )


write.table(y1, file = 'adult_discretizado.data.txt', sep=", ", row.names = F, quote = F)



