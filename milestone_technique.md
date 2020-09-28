---

## MILESTONE 1 : Exploring the Data

In this milestone, we are going to explore API provided by Data.gov.sg. Subsequently, we will screen the dataset and select the bestv location to do "Traffic Condition Classification". For individual location, it will return us the parameter as below:

1) Timestamp
2) Location (latitude and longitude)
3) Camera Id
4) Height and Width of the Image

As definition of trafic condition is subjective, one user's definition of heavy traffic is what another would deem to be normal traffic. besides, high traffic flow does not mean that the road is having traffic jam. Having said that, there might be high density of vehicle in the road, but they are moving smoothly without encountering the traffic jam. With all these considerations, I decide to select causeway for my project. As every vehicle must be stopped and checked by the custom oficer, and this process is likely using the same duration for each vehcle. Therefore, the definition of traffic jam is relatively easier to be defined. For causeway, if there are high density of vehicles, it is defnitely that we must queue longer time to cross the checkpoint.

As a result, the two causeway cemeras (id:2701 and id:2702) are selected.

<img src="Image/Image1.png"
     style="float: left; margin-right: 0px;" />

---
## SECTION 2 : REQUIREMENTS
