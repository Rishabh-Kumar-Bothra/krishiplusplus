# Krishi++
Krishi++ - Connecting farmers

There are various portal related to agriculture for providing solutions to problem of farmers, but there are generalized solutions given to them mostly. Also, sometimes apps are dealing with one or two components of farming only. So we are trying to integrate all these components int one and give detailed and scheduled solutions to farmers, integrating packages of practices. In this application real time info will be given to farmers from feild preparation to selling of their product.

* Provide analysis like sowing rate, spacing, fertlizers to be used to farmers on basis of soil health card.
* Risk management, giving message to famers when floo or cyclone is about to hit.
* Giving suggestions to farmers for plating best crop and their variety and intercrops and variety.
* Giving farmers yield prediction and profit prediction using **random forest model fitting.**

The present Apps only give geeralized option about crops and farmers but our app gives targeted ressult to farmers analysing their **S**oil **H**ealth **C**ard and predicting their yield per hectare if they follow our suggestion. 

**Simply speaking our app leverages Soil Health Card information for farmers. The Soil Health card, issued by Govt. of India does not have much useful for information that farmers can directly use. Our app uses SH info and provides info like Variety, inter-crop, seed spacing and sowing period. Using these info we predict the yield and predicted profit to farmer using random forest model. Additionally we use low cost, low powered temp and humidity sensors deployed in the field for better real time analysis and prediction with cyclone or flood forecast.**
 
This app also gives risk management based on cyclone and flood forecast from Govt. of India website.

### Images 
![First](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/1.png)
![Fifth](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/2.png)
![Second](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/3.png)
![Third](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/4.png)
![Fourth](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/5.png)
![nine](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/6.png)
![Sixth](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/7.png)
![Seven](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/8.png)
![Eight](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/9.png)

### Crop Yield Prediction using Machine learning
We used **random forest** algorithm for yield prediction and using the predicted yield we can found forecasted profit. As the data is too much scattered, multiple linear regression gives error of 30% - 40%. Thus random forest suits best and according to many research papers. Our implemented model gave error about 10 % - 11% for predicted yield. Images shown below.

![First](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/s4.png)
![Second](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/s1.png)
![Third](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/s2.png)
![Fourth](https://raw.githubusercontent.com/geekychaser/krishiplusplus/master/images/s3.png)

