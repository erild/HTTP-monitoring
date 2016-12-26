HTTP-monitoring
===============
Simple console program to monitor HTTP traffic by analysing an w3c-formated HTTP access log

Every 10s, display a report with the most hits section, the most active users, and the traffic

If the hits in the last 2 min are above a threshold, display an alert

#Installation

Just clone the repository and verify you have python3 installed

#Compatibility
Tested on Linux: debian 7 and archlinux

Not tested on Windows but should work 

#Usage
 ```bash
 http_monitoring.py [-h] -i LOGFILE -l LIMIT
 ```
 
 LOGFILE is the path to the access log
 LIMIT is the alerting threshold in number of hits
 
#Test
 To run the test, just run the `test.py` file in the test directory
It will run a test scenario of about 4min that will generate an alert
 
#Improvement
 - Allow the user to chose the number of most hits path an most active user displayed
 - The program run on local time. Use the UTC time instead and use the timezone information of the w3c log for it
 - The program is dependant on the system time being the same as the program writting the logs. Remove that dependancy 
 - Interactive command line to allow user to change the threshold
 - Analyse and use the HTTP codes and type of request in the report
 
