
---

## SECTION 1 : PROJECT TITLE
## Image Based Traffic Density Real Time Prediction using SG LTA Traffic Cameras

<img src="website_outlook.png"
     style="float: left; margin-right: 0px;" />

---
## SECTION 2 : Requirements


---
## SECTION 3 : EXECUTIVE SUMMARY / PAPER ABSTRACT
There are many route planning apps in the market. Some help their users plan their trips by using maps to find the shortest path. However, if real traffic conditions are not 
factored in, even if they use the most accurate map available, frequently what appeared to be the faster route ends taking up a much longer time than anticipated.

Other route planning apps tried to overcome this issue by having their users turn on GPS. Based on the accumulated users' GPS in specific location, the app can "see" the traffic density there. In addition to this, some apps also incorporate traffic reports and tweets into their optimization model.

However, these methods depend on the user agreeing to turn on their GPS and tweeting about traffic conditions. Some users may wish to use the app in an offline mode and not turn on their GPS due to privacy concerns, and we cannot depend on users to always tweet about traffic situation consistenly and in every instance. How many users are displined or motivated to call in traffic report after report, day after day. Moreover, categorization of traffic density is subjective. One user's definition of heavy traffic is what another deem to be normal traffic

In Singapore, there are around 87 LTA traffic cameras installed all over the island. By utilizing the LTA traffic cameras to measure traffic density, we providue an addition method of providing traffic density that is not dependent on users' GPS and reports.

My goal is not to replace route planning apps but to provide a serice as assistance which they can use to improve the existed route planning.

At the end, I have developed a real-time web application to predict the causeway traffic density using Falsk framework and trained CNN nueral network.

As this is a proof-of-concept and not the full-blown implementation, the trained neural network is not able to recognize other road's traffic condition and it is only applicable on JB-SG causeway
 

---
## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| ANI SIVARAM PORKALANGAD AYYAPPAN | A0195404E | Project Planning, Requirement Specifications, Project Report, System Design, Testing, Project Video| E0385035@u.nus.edu |
| GARY NG JIAN ZHE | A0195367N | System Design, System Architecture, Rules definition, Optaplanner solver building, Integration of front-end & back-end, Bug fixing and back-end code development, Testing & Project Report | E0384998@u.nus.edu |
| MOHANADAS GANGA SOOREJ | A0195397J |Frontend Code development, Bug fixing and back-end code development, Integration of front-end & back-end| E0385028@u.nus.edu |
| RITESH MUNJAL | A0195304H | System Design & System Architecture, Optaplanner solver building, Bug fixing and back-end code development, Integration of front-end & back-end, Testing & Project report| E0384935@u.nus.edu |
| SANTHIYAPILLAI RAJEEVAN PAUL | A0195399E |System Design & System Architecture, Optaplanner solver building, Bug fixing and back-end code development, Integration of front-end & back-end, Testing| E0385030@u.nus.edu |
| YONG QUAN ZHI, TOMMY | A0195353Y | System Design & System Architecture, Frontend Code development, Bug fixing and back-end code development, Integration of front-end & back-end, Testing, User manual & Project Report| E0384984@u.nus.edu |

---
## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

[![INTELLIGENT EMPLOYEE SCHEDULER](https://img.youtube.com/vi/y03K28tAMV4/0.jpg)](https://www.youtube.com/watch?v=y03K28tAMV4)

---
## SECTION 5 : USER GUIDE


### To run the system in local machine

First ensure you have all dependencies :
* Apache Maven
* Java JDK 1.8
* NPM package manager
* Angular 6
* NodeJS

Prepare back-end of the service
1. Open up your command prompt/terminal
2. Do ``git clone`` https://github.com/nus-iss-2019-gameofthrones/RosterPlanner
3. Go into the ‘Services’ project folder
4. Run ``mvn clean install -U`` to compile the project
5. Run ``mvn spring-boot:run`` to start the application
6. Now back-end is deployed on *localhost:8082*

Prepare front-end of the service
1. Open up your command prompt/terminal
2. Go into the ‘Frontend’ project folder
3. ``Npm install``
4. ``Ng serve`` 
5. No fornt-end is started on *localhost:4200*
6. Open a browser and got to *localhost:4200*

For more detailed guide, please read the user guide attached on below link

<https://github.com/nus-iss-2019-gameofthrones/RosterPlanner/blob/master/Throne_UserManual_TestCase.pdf>

---
## SECTION 6 : PROJECT REPORT / PAPER

<https://github.com/nus-iss-2019-gameofthrones/RosterPlanner/blob/master/Reasoning%20systems%20project%20report%20final.pdf>


---
