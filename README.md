Smart Chat portal 
===================

<strong><em>Learn It Girl Third edition.</em></strong>
<div style="color:#0000FF">
<strong>Language: Python</strong>
  
The project that I will be working on along with my mentor is titled as "Smart Chat Portal". 
The application will detect the emotions of the person with whom we are chatting based on the typing speed, kind of words being used etc. This can be very important generic feature for any chat application, that can be combined with AI for further exploitation near in future. Analyzing the sentiments in an efficient manner. 
The primary language that i will be using is python. 
Apart from that the front end will comprise of HTML, CSS and JavaScript. 
Overall the chat will be powered with web sockets and further it will be integrated with AI algorithms to make an end to end application.
</div><br>

<h2> How to run the application </h2>

<p>To run this application install the requirements in a virtual environment, run `python chat.py` and visit `http://localhost:5000` on one or more browser tabs.</p> 

<p>or by using server using the Flask cli: $ FLASK_APP=chat.py flask run</p>

<strong> Getting started with chat between two clients (using web sockets)</strong>
<ul><li>Alpha and Beta enters the chat room</li></ul>
<img src="https://github.com/sayantikabanik/SmartChatPortal/blob/master/smartchatportal%20output/alpha%20entering.png" alt="loading" height="400" width="800"/>
<img src="https://github.com/sayantikabanik/SmartChatPortal/blob/master/smartchatportal%20output/beta%20entering.png" alt="loading" height="300" width="500"/>

<ul><li> The clients communicate with each other via web sockets (Flask SocketIO)
<img src="https://github.com/sayantikabanik/SmartChatPortal/blob/master/smartchatportal%20output/client%20server%20communicating.png" alt="loading" height="300" width="500"/>

<strong><p>The sentiments are analysed based on the content and typing speed.
The anaysis of speed along with the content makes the entire conversation portal smart and more efficient.The javaScript funtion calculates user’s typing speed and
converts into a feature for intensity recognition. A very
high typing speed indicates Very Excited user and a very
low speed indicates a Very Muted or least intense user.</p></strong>
<img src="https://github.com/sayantikabanik/SmartChatPortal/blob/master/smartchatportal%20output/alpha%20analysis.png" lt="loading" height="300" width="500"/>  