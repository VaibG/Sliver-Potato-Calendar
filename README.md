# Sliver-Potato-Calendar
## Description
If you have ever visited in Berkeley, you are probably familiar with Sliver, a pizza restaurant that serves a single-type vegetarian pizza every day. This means every day consists of a new pizza with different ingredients. However, there is one unorthodox ingredient that makes people fall in love with this restaurant and that is the Roasted Yukon Gold Potatoes. You must be thinking, potatoes on pizza?!? ew. But trust me, it's really good!  

In an effort to utilize my skills to automate different parts of my life, I created this script which scrapes the pizza flavors for the week using Beautiful Soup and adds events to my Google Calendar when the pizza contains Roasted Yukon Gold Potatoes using the Google Calendar API. This script runs twice a week using a cronjob and will automatically update my calendar with an event, without requiring authorization. 

## Usage
If you just want to view the calendar (and you are a Berkeley student): click <a href="https://calendar.google.com/calendar?cid=YmVya2VsZXkuZWR1X285YTA3cms3NG50NWgwM2E5Z2trdnI1NXBrQGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20" target="_blank">here</a>

Otherwise, follow these steps:
1. Download the script and `pip install` the dependancies that you may not have.  
2. Set up a service account through the steps <a href="https://medium.com/@ArchTaqi/google-calendar-api-in-your-application-without-oauth-consent-screen-4fcc1f8eb380" target="_blank">here</a> and download the JSON.  
3. Once you have set up the service account, create a calendar and share it with the client_email that you can find in the service account JSON.  
4. Find the calendar id and service account JSON path and edit `sliver.py` in the commented places.  
5. Set up a cron job using `crontab -e` to run twice a week.  
6. Enjoy eating those potatoes at Sliver!
