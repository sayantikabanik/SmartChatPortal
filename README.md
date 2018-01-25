Smart Chat portal 
===================
**_Learn It Girl Third edition_**
* **Mentored by**:[@MeRajat](https://github.com/MeRajat)
#### Framework used-Flask
The application I developed is titled as "Smart Chat Portal ". It  has immense scope. Humans are build on the framework of emotions. Hence i have taken into account extra parameters to accurately determine it.
"Smart Chat Portal" detects the emotions of the person with whom we are chatting based on the typing speed, kind of words being used etc. This can be very important generic feature for any chat application, that can be combined with AI for further exploitation near in future. Analyzing the sentiments in an efficient manner. The primary language that i will be using is python. Apart from that the front end is made with jinja2 with parts of  JavaScript. Overall the chat is powered with web sockets and further it will be integrated with ML algorithms to make an end to end application.
Text Analysis -TextBlob combined with naivebayesclassifier.

#### Running the application
To run this application install the requirements in a **virtual environment**, run *python chat.py* and visit http://localhost:5000 on one or more browser tabs.
#### Using server using the Flask cli:
```fancy
$ FLASK_APP=chat.py flask run
```
**Getting started with chat between two clients (using web sockets)**
* Alpha and Beta enters the chat room :

  ```   fancy
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)
    ```

<img src="https://github.com/sayantikabanik/SmartChatPortal/blob/master/smartchatportal%20output/alpha%20entering.png"  width="400"/><img src="https://github.com/sayantikabanik/SmartChatPortal/blob/master/smartchatportal%20output/beta%20entering.png" width="400"/>

**The clients communicate with each other via web sockets (Flask SocketIO)**
<img src="https://github.com/sayantikabanik/SmartChatPortal/blob/master/smartchatportal%20output/client%20server%20communicating.png" alt="loading" height="300" width="500"/>

**The sentiments are analysed based on the content and typing speed.**
The anaysis of speed along with the content makes the entire conversation portal smart and more efficient.The javaScript funtion calculates user’s typing speed and converts into a feature for intensity recognition. A very high typing speed indicates Very Excited user and a very low speed indicates a Very Muted or least intense user.

#### code snippet for analysisng the sentiments based on the text and typing speed:
         
  ```fancy
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the room.'}, room=room)

      $(function() {
                $('input')
                    .keyup(checkSpeed);
            });

            
            function checkSpeed() {
                iTime = new Date().getTime();

                if (iLastTime != 0) {
                    iKeys++;
                    iTotal += iTime - iLastTime;
                    iWords = $('input').val().split(/\s/).length;
                    $('#CPM').html(Math.round(iKeys / iTotal * 6000, 2));
                    $('#WPM').html(Math.round(iWords / iTotal * 6000, 2));
                    
                    if((Math.round(iKeys / iTotal * 6000, 2))>=80){
                        $('#emo').html("you seem excited today");
                        //break;
                    }
                    else if((Math.round(iKeys / iTotal * 6000, 2))<=15){
                        $('#emo').html("you seem sad today");
                        //break;
                    }
                    else{
                        $('#emo').html("you seem in a good mood today");
                       // break;
                    }
              }

                    iLastTime = iTime;
              
            }
   ```
**The final analysis is done combining all the aspects and hence obtaining the desired result**
<img src="https://github.com/sayantikabanik/SmartChatPortal/blob/master/smartchatportal%20output/alpha%20analysis.png" lt="loading" height="400" width="700"/>  
