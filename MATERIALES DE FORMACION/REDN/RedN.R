install.packages("caTools")
library(caTools)
library(neuralnet)
library(NeuralNetTools)

dataset<-datasets::mtcars
dataset_sc<-data.frame(cbind(dataset$cyl,scale(dataset[,c(1,3:11)])))
names(dataset_sc)[1]<-"cyl"

sample<-sample.split(dataset_sc$cyl,SplitRatio = 0.7)
train <-subset(dataset_sc,sample==TRUE)
test <-subset(dataset_sc,sample==FALSE)

model.net<-neuralnet(
  formula = cyl ~ .,
  data = train,
  hidden = c(5,5),
  stepmax = 1e+05,
  linear.output = TRUE,
  act.fct = "logistic"
)
# http://127.0.0.1:10421/graphics/plot_zoom_png?width=725&height=636lt
  model.net$resu.matrix
  data_pred <- compute(model.net,test)$net.result
  test_df<-data.frame(cbind(round(data_pred),test$cyl))
plotnet(model.net)                    
olden(model.net)
