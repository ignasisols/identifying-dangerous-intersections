# Identifying dangerous intersections for conversion into roundabouts 

### Ignasi Sols

This project will be the next iteration of the project presented in the business model with the same title. I know aim to extend the analysis from Pennsylvania to the rest of the US.

#### Question/need:

* What is the framing question of your analysis, or the purpose of the model/system you plan to build? 
  The framing question of my analysis is to identify road junctions that should be prioritized for conversion to roundabouts, based on current scientific evidence of a meta-analysis of 44 studies showing a 65% reduction in fatal accidents when junctions are converted to roundabouts. (https://pubmed.ncbi.nlm.nih.gov/28064101/). The aim is to reduce the number of accidents in the US, and their severity, through infrastructure changes. 

* Who benefits from exploring this question or building this model/system?
  Drivers; local, state and federal government; insurance companies.
  
  

#### Data and Analyses description:

* What dataset(s) do you plan to use, and how will you obtain the data?
  https://www.kaggle.com/sobhanmoosavi/us-accidents
  This dataset is being updated every year and it includes accident data from 49 US states since 2016 and 2020. It currently includes data from 1,516,064 accidents (one accident per row). This dataset does not include fatalities and injuries information, so this time I plan to add information from another dataset from the Department of Transportation, using Google Big Query (NHTS Traffic Fatalities: https://console.cloud.google.com/marketplace/product/nhtsa-data/nhtsa-traffic-fatalities?project=us-nhtsa-car-crashes). 
  
* What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with? 
  The datasets I will work with have one specific accident on each row. As I did in the first iteration of this project, I plan to filter to keep only accidents that were reported to happened close to an traffic signal (which indicates and interesection). In this new iteration I plan to add stop signs as well. I plan to use the latitude and longitude information as inputs for the custom algorithm that I developed that groups accidents, identifying the location of specific intersections where at least two accidents occurred. In the previous iteration of this project, I used the number of accidents as a way to group intersections for visualization. This time, I plan to add injuries and fatalities for these intersections, if available. 

#### Tools:

* How do you intend to meet the tools requirement of the project? 

* Heroku, Streamlit + Plotly / Bokeh (In the previous iteration I had used Tableau).

* Spark.

* AWS.

* Google Big Query (NHTS Traffic Fatalities).

  

#### MVP Goal:

* What would a [minimum viable product (MVP)](./mvp.md) look like for this project?

  Scale up the previous iteration analysis to the whole U.S. and include accidents that occurred at stop signs.

#### If time allows it, I might explore some of these other questions:

* There might be accidents that occurred in dangerous intersections that had no traffic signals or stop signs that were excluded from the previous iteration analysis. I could investigate if such cases occurred by using the OpenStreetMap API (by assessing proximity to a map node). If such accidents exist, I will include them. 

* Using the OpenStreetMap API, I plan to label the intersections as two-way, three-way, four-way, etc... to identify which type of intersection are related to more accidents or to a higher number of accidents. 

* Using the Kittelson US roundabout dataset (https://roundabout.kittelson.com/Roundabouts):

  (a) Investigate the relationship between number of roundabouts in each US county and number of accidents (or the investment in road infrastructure) with accident numbers per 100,000 inhabitants. This could help prioritize some areas that have a higher ratio of accidents/money invested in infrastructure. Use federal and state data regarding investment in infrastructure. 

  (b) Investigate if there is evidence of a decrease in accidents when intersections are converted into roundabouts (some roundabouts in the Kittelson dataset, available as an XML, have the construction year reported).

* The user could reports a start and end locations of an itinerary (https://wiki.openstreetmap.org/wiki/Openlayers_Track_example), and the dashboard will report which intersections should be avoided.

* For these other ideas I would use OpenStreetMap API and Kittelson KLM roundabout dataset as well.



