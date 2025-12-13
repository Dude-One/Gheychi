 hey dude i use to see afew points here to tell you about when coding this :
 
 - first one was when i started coding on it as any dev dose i wanted to use uuid for shorten version of each url to make sure its unique i even coded it that way then saw that you put maximum limit 5 char in there so you bitch 
 - then i wanted to use epoch time to make each record unique but there was a limitation of 5 char so the number of records would be 1 to 99999 so i gone for adding characters in it a new method i used base 62 chars combination to create short link for each url in this case i had around of 916 000 000 short links i know i can add more chars and combos but it dose prove the point 

next one is the write concurrency or race condition : [IF YOU DONT READ THE REST DOSENT MATTER JUST PLZ READ THIS ONE MULTIPLE TIMES]

- as the dude asked me in the interview how do you want to fix race condition i did here using transactional db management how i have 2 queries that write on db one update one insert 
- first thing first i create the short key using id and base 62 encoder so id must be unique per each record and the most important thing is i dont generate the id in the code that will fix the race condition how read the next line
- when i add each record to db i return the id of it to the code the point of this is im using .begin() transaction method of db SQL will ensure each id is unique base on im using this method and im returning this to the logic to continue 
- then i will create the shorten url base on the id we got from the insert transactional method and use it with base 62 encoder to create a shorten url and then update the record in db to have the shorten url in there 
- the key point i found when i was coding this is i cant put logic on shorten url to check if i already have this in my db or not reason was i am using a query to add the record and an other one to update it and if this code scales up and other instance might exactly get the record between the update and insert
- so i crated a hash method to create a hash for each record to check with that if this record is already exists or not 
- also the hash can help for later on to make get queries consume less time and process to find the record but its not the key point of adding the hash record in db


CODE STRUCT 
- Model = DATA Transfer Objects its just a validator i could put in object parser or creation of json objects for other apis in complex projects its also serializer can be here inside each DTO as well or in an other dir its kind of taste of each person 
- Controller =  URLS and Routes of this app are here if i used message brokers i could put the events or end point of them here too the observer pattern of all frameworks are checking this end points 
- DAL = [DATA ACCESS LAYER] bunch of Queries and db structure) i know i need to make a new file for db schema and build it there but i didnt have time for this also we could add migrations to it for later on
- LOGIC = The most sexiest module always all the good stuf and probably most of the bugs happen here the pure logic of application is handled here 
- View - We dont have any on this app 


