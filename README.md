# RESTaurant API
RESTful API that takes order for breakfast, lunch and dinner following specific ruleset given.

Instructions for use:
1. Download Zip file from github
2. Unzip file
3. Navigate into file with bash
4. Run ./buildproject.sh
5. If Pip3 is not currently installed, you will need to enter in password for sudo apt install

I am currently working full time as a Delivery Driver for FedEx Thursday though Sunday in Bellingham, WA so I did not have the amount of time I would have liked to put into this project. This is my first time creating an API- learned a lot! Very fun project altogether and definitely plan to make more APIs in the future.

Known issues:
1. I did not meet all rules required, I have parsed the request information and with a few more hours I believe I could handle the remaining rules.
2. I did not utilize reqparser, I discovered this REST API feature late and wish I could have implemented this rather than my solution of creating a method to parse the data myself.
3. My test cases are very much lacking. With another hour I would go about solving this issue by creating a randomized testfile generator so I could generate a few 100 lines of code, run them through my API and any tests that failed, flag and make sure they were failing under the right conditions.
4. I did not get to use SQLAlchemy, I created a database for my demoAPI project but didn't have time to implement for this (I wanted to finish my request parser and validation before creating the database).

Overall, fun project and I am pretty excited to say I completed my first API, albeit one that can use a bit of TLC ;)