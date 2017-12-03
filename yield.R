library(party)
library(randomForest)
output.forest <-  randomForest(yield ~ Nitrogen + Phosphorous + potassium + organiccarbon + pH + temp, 
                               data = data)
print(output.forest)
x_test = data[1:100,1:6]
print(x_test)

predicted = predict(output.forest,x_test)
print(predicted)
