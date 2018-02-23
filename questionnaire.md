## ETL Architecture Project Questionnaire

### Project Data Points
1. Across all reservation partners for January & February, how many completed reservations occurred?
	130

2. Which studio has the highest rate of reservation abandonement (did not cancel but did not check-in)?
	3 way tie:
	crossfit-control-jacksonville-beach	3
	orlando-yoga	3
	hive-athletics	3

3. Which fitness area (i.e., tag) has the highest number of completed reservations for February
	yoga 24

4. How many members completed at least 1 reservation and had no more than 1 canceled reservation in January?
	24

### Project Discussion
1. Describe what custom logic you chose to implement in your ETL solution and why?
	I implemented empty string to None conversions to make database inserts easier, and implemented a few basic
	date fixes based on some of the problems I notice, which was either missing date/time or a 2/30 date that doesn't exist.

2. What forecasting opportunities do you see with a dataset like this and why?
	With a monthly feed of these files, you could attempt to forecast cancellations and checkins for the given locations.

3. What other data would you propose we gather to make reporting/forecasting more robust and why?
	Additional member information (based on member_id) would allow additional analytics and forecasting of reservations/cancellations/abandonments by demographic so that clubs/instructors know which demographics are utliizing their services the most so they can optimize marketing dollars.


4. What was difficult and how might you have approached that obstacle differently next time?
	Getting acclimated to python was somewhat difficult, however I tried my best to keep it as simple as needed. In the future, I would take the lessons I learned in python here and try to learn about what gave me problems initially.