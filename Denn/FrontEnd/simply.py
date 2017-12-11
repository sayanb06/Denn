from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
<!DOCTYPE html>
<html>
<head>
    <script src="https://apis.google.com/js/platform.js" async defer></script>
    <meta name="google-signin-client_id" content="67037978831-8fi98q8434cq31n0j2gjmh2e28363rs7.apps.googleusercontent.com">
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
            document.getElementById("hi").innerHTML = "Hello " + profile.getName();
        }
    </script>
</head>
<body background="https://github.com/arch1904/Denn/blob/master/Denn/FrontEnd/Logout_files/bglogin.jpg?raw=true">
    <link rel="stylesheet" type="text/css" href="https://raw.githubusercontent.com/arch1904/Denn/master/Denn/FrontEnd/Logout_files/Style%20Sheet.css">

    <div id="Header">

    </div>
    <div id="logo">
        <center><img src="https://github.com/arch1904/Denn/blob/master/Denn/FrontEnd/logo.png?raw=true" width="600" height="256"></center>
    </div>

    <div id="login-option-top">
        <div class="g-signin2" data-onsuccess="onSignIn"></div>        
    </div>
    

    <a href="#" onclick="signOut();">Sign out</a>
    <script>
        function signOut() {
            var auth2 = gapi.auth2.getAuthInstance();
            auth2.signOut().then(function () {
                document.getElementById("hi").innerHTML = "";
                console.log('User signed out.');
            });
        }

    </script>
    <h3 id="hi" style="text-align:center; color:springgreen" ></h3>
    <div id="login-option">
        <img id="login-logo" src="facebook.svg" alt="Facebook logo">
    </div>
    <script>onSignIn();</script>
    <iframe src="https://tokbox.com/embed/embed/ot-embed.js?embedId=de42f0bd-1dc0-4ef0-925b-6128a2db7bfd&room=DEFAULT_ROOM&iframe=true" width="800px" height="640px" ></iframe>
</body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)