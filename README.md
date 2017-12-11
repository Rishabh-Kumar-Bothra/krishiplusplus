# Krishi++
Krishi++ - Connecting farmers

Website Link : https://api.combatant32.hasura-app.io/

**Note**: _The website is not yet optimized for mobile devices(due to time constraints) and may give UI glitches on mobile devices. It works real fine on tablet or dektop computers._ 

**Note**: _When entering the SH number for website use **'93456'** or **'21234'** and any **random pincode**._

There are various portal related to agriculture for providing solutions to problem of farmers, but there are generalized solutions given to them mostly. Also, sometimes apps are dealing with one or two components of farming only. So we are trying to integrate all these components int one and give detailed and scheduled solutions to farmers, integrating packages of practices. In this application real time info will be given to farmers from feild preparation to their predicted yield.

* Provide analysis like sowing rate, spacing, fertlizers to be used to farmers on basis of soil health card.
* Risk management, giving message to famers when floo or cyclone is about to hit.
* Giving suggestions to farmers for plating best crop and their variety and intercrops and variety.
* Giving farmers yield prediction and profit prediction using **random forest model fitting.**

The present Apps only give generalized option about crops and farmers but our app gives targeted ressult to farmers analysing their **S**oil **H**ealth **C**ard and predicting their yield per hectare if they follow our suggestion. 

**Simply speaking our app leverages Soil Health Card information for farmers. The Soil Health card, issued by Govt. of India does not have much useful for information that farmers can directly use. Our app uses SH info and provides info like Variety, inter-crop, seed spacing and sowing period. Using these info we predict the yield and predicted profit to farmer using random forest model. We also provide real time prediction of cyclone and flood to farmers.**

Example of Soil Health Card
![SHC](http://www.soilhealth.dac.gov.in/Content/blue/soil/assets/img/slider/slider5.png)
 
Soil Health Card is prepared by agricultural scientist under Soil Health Card scheme of Govt. of India. It contains information like the variety of crops and intercrop that can be grown on a farmers land based on its agro-climatic region and value of N,P,K ratio of farmer's land. This info is pretty rudimentary considering farmer's view.

So our App's aim is to use this SHC infomation and make it directly useful to farmers. Based on SHC data we provide info like **variety of crops, intercrop and their sowing period**. We also provide info of **land prepration, fertilizer to be used, spacing between crops and rate of sowing seed**. Thesee information and nation wide standars based on the agro climatic region where the farm is. The USP of our app is **yield prediction and cyclone and flood forecasting**.

Based on past data of an agro-climatic region we are predicting the yield using random forest model fitting which can be obtained if farmer follows guidelines given by our app. Therefore, a farmer can plan his invesment accordingly taking in consideration the predicted yield hence the forecasted profit. Additionaly we also scrape data from Govt. websites for flood and cyclone forecasting. Flood and cyclone forecasting can be much beneficial info for farmer because if they know they can be affected they can move their harvested grain to safe place hence saving him from future losses.

Due to time and data constraints, we have not deployed the machine learning and flood forecasting files. They were just run once and their data was directly stored in database, using databse api provided by Hasura.

* server.js -- server file
* public folder, error.html, -- static file with index.html and error page repectively
* View folder -- User template 
* yield.R -- random forest yield prediction
* data.csv -- data used for yield prediction, based on agro climatic region of west Gujarat
* flood-cyclone.py -- script for scraping wesite for flood and cyclone forecast

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

