RoadMap for geo-replay
======================

Configuration Management
------------------------
1. GeoIP Database Source Manager and Automatic Updates
2. AWS Credential Manager
3. Django Settings

GeoIP Component
---------------
* IP to Country Translator API

Web Log Generator Component
--------------------------
* Web Log Parser
 * IP, Target, Payload
* Get Requests Only for Now
* Pluggable Parser Implementation for different web server log formats

### Generate Traffic Files
* Basic Map Transform and Reduce by IP, Order by Timestamp
* Pluggable Request Sampler (Later)
* Session Generation and Request Order (Intitally One to One Mapping, Ordered by Log Order)

### Traffic Files to be partitioned by datacenter
* Map (IP, {Target,Payload}) - > AWS Region
* Upload to S3 Location


Cloud Component and Test Administration
---------------------------------------
* Launch X LGs in each of the identified regions. (Initially One)
* Each LG to have a Rest API 
	* (S3 Location of Traffic File), 
	* Load Generation Description and Schedule
	* Test Control (Start or Stop Test)
	* Progress / Status Reporting
	* Start Test and Sample Latency of Web Requests
* Write Result Files


Report Generation and Analysis
------------------------------
### Export Traffic Results into a Database or Django ORM


### Generate Reports
* Latency by Region 
* Top 10 Fastest Pages and Slowest Pages loaded by region.

### Export of Data to CSV and other formats
	
Dashboarding Component
----------------------
Web Interface for Log Ingestion, Test Administration and Result Analysis (Last)
Configuration and Update Pages
