from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    f = open("Tok.txt","r") #opens file with name of "test.txt"
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <script src="http://static.opentok.com/webrtc/v2.0/js/TB.min.js" type="text/javascript" charset="utf-8"></script>
	    <script>
            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.min.js"></script>
            <script type="text/javascript" charset="utf-8">
            $(document).ready(function(){
              $("#link").attr('value',document.URL);
            })
          TB.addEventListener("exception", exceptionHandler);
          var session = TB.initSession("2_MX40NjAxODc0Mn5-MTUxMzA1NTMwODcyMX5PYTY3bitzd2g4VGQzUjhoQTYwb2U5Unh-fg");
          session.addEventListener("sessionConnected", sessionConnectedHandler);
          session.addEventListener("streamCreated", streamCreatedHandler);
          session.connect(46018742, "T1==cGFydG5lcl9pZD00NjAxODc0MiZzZGtfdmVyc2lvbj1kZWJ1Z2dlciZzaWc9MjQ5YTNmM2RmZGM3MjI5YmYyMGE0MjBiM2QzNWNkZTlhZmVkNGRhZTpzZXNzaW9uX2lkPTJfTVg0ME5qQXhPRGMwTW41LU1UVXhNekExTlRNd09EY3lNWDVQWVRZM2JpdHpkMmc0VkdRelVqaG9RVFl3YjJVNVVuaC1mZyZjcmVhdGVfdGltZT0xNTEzMDU1MzA4JnJvbGU9bW9kZXJhdG9yJm5vbmNlPTE1MTMwNTUzMDguNzMwNTY3MTI2MTUzJmV4cGlyZV90aW1lPTE1MTU2NDczMDg=");
          function sessionConnectedHandler(event) {
             subscribeToStreams(event.streams);
             session.publish();
          }
      
          function streamCreatedHandler(event) {
            subscribeToStreams(event.streams);
          }
      
          function subscribeToStreams(streams) {
            for (var i = 0; i < streams.length; i++) {
              var stream = streams[i];
              console.log(stream.connection.connectionId+"&"+session.connection.connectionId);
              if (stream.connection.connectionId != session.connection.connectionId) {
                session.subscribe(stream);
              }
            }
          }
      
          function exceptionHandler(event) {
            alert(event.message);
          }
      
        </script>
        <script src="https://apis.google.com/js/platform.js" async defer></script>
        <meta name="google-signin-client_id" content="""+f.readline()+""">
        <title>
            Welcome to Denn!
        </title>
        <script>
            function onSignIn(googleUser) {
                var profile = googleUser.getBasicProfile();
                console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
                console.log('Name: ' + profile.getName());
                console.log('Image URL: ' + profile.getImageUrl());
                console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
                document.getElementById("Greeting").innerHTML = "Hello " + profile.getName();
		        document.getElementById("GoogleSignIn").style.visibility = 'hidden'
		        document.getElementById("GoogleSignOut").style.visibility = 'visible'
            }
        </script>
    </head>
    <body background="https://github.com/arch1904/Denn/blob/master/Denn/FrontEnd/Logout_files/bglogin.jpg?raw=true" id = "back">
    <div id="login-option-top">
            <div class="g-signin2" data-onsuccess="onSignIn" id="GoogleSignIn" style="float: right;"></div>        
    </div>
    <p></p>
    <a href="#" onclick="signOut();" style="float: right;visibility: hidden; color: green;" id = "GoogleSignOut">Sign out</a>    
    <link rel="stylesheet" type="text/css" href="https://raw.githubusercontent.com/arch1904/Denn/master/Denn/FrontEnd/Logout_files/Style%20Sheet.css">

        <div id="Header">

        </div>
        <div id="logo">
            <center><img src="https://github.com/arch1904/Denn/blob/master/Denn/FrontEnd/logo.png?raw=true" width="600" height="256"></center>
        </div>

        
    

        
        <script>
            function signOut() {
                var auth2 = gapi.auth2.getAuthInstance();
                auth2.signOut().then(function () {
                    document.getElementById("Greeting").innerHTML = "";
                    console.log('User signed out.');
		            document.getElementById("GoogleSignIn").style.visibility = 'visible'
                    document.getElementById("GoogleSignOut").style.visibility = 'hidden'
                });
            }

        </script>
        <h3 id="Greeting" style="text-align:center; color:springgreen" ></h3>
        <script>onSignIn();</script>
	    <h1 style= "text-align: center; color:red">Denn ChatRoom</h1>
        <iframe id = "Tok" src=""" + f.readline() + """ width="840px" height="640px" style = "display:inline-block"></iframe>
        <fakee id="Video" style = "display:inline-block"></fakee>
        <input type="text" id="myTextBox" cols="50" rows="1" placeholder="Enter YouTube Link">
        <script>
            function sendVideo() {
                    var url = document.getElementById("myTextBox").value
                    url = url.replace("watch?v=", "embed/");
		            document.getElementById("Video").innerHTML = "<iframe src=\\\""+url+"\\\?autoplay=1\\\" width=\\\"840\\\" id = \\\"YTPlayer\\\" height=\\\"473\\\" frameborder=\\\"0\\\" gesture=\\\"media\\\" allow=\\\"encrypted-media\\\" allowfullscreen></iframe>";
                    var button = document.getElementById("button1");
                    var pplace = document.getElementById("placehold");
                    var back = document.getElementById("back");
                    var texting = document.getElementById("myTextBox");
                    back.removeChild(button);
                    back.removeChild(pplace);
                    back.removeChild(texting);

                }
            function getHalfWidth() {
                return window.innerWidth/2;
                }
        </script>
	    <button onclick=sendVideo() style="color: blue;" id="button1">Watch YouTube Video</button>
        
        <p id = "placehold"></p>	
    
    
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)