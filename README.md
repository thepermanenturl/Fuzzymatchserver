# Fuzzymatchserver
## Fuzzy string matching, publicly callable using API


Enclosed are two folders.

1. client side code(test, request)
	1. client.py
	1. variable.py
1. server side code
	1. flask server.py
	1. Fuzz.py

### Simply execute (1.1) client.py to test if server is live, and works correctly.
	Input data is stored in (1.2) variable.py

Change variable.py, within given format, to test different data with (1.1).

Server is already set up, thus is enclosed for invesigation purposes only

(2.1) flask server.py, is the flask server code that works in 
pythonanywhere.com

(2.2) Fuzz.py, called by flask server.py, is the actual algorithm.

Issues and improvements
- No frontend, although can be added. As its an API, no real need.
- The Fuzz algorithm can be optimised depending on the sort of recieved data.
  Currently, its made for very generalised data
- Server not permanent, will need to be renewed every three months, 
  although free of cost. Last renewed on 24 July 2020. Next renewal
  24 October 2020.

Technologies Used
- Python
- python modules 
	- flask, for server
	- fuzzwuzzy, for string matching
- pythonanywhere.com for hosting

Dev - Spandan Bhattacharya, 24 July 2020
