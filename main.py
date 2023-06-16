#-*-coding:utf8;-*-
#qpy:console
import time
import sys
import webbrowser
import os
import androidhelper

droid = androidhelper.Android()

while True:
   droid.ttsSpeak("How can i help you")
   a = droid.dialogGetInput('How Can I Help You').result
   a = a.lower()

   if a == "how old are you":
      droid.ttsSpeak("I'm 5 Minutes Old")
      droid.dialogCreateAlert("Iam 5 Minutes Old😄")
      droid.dialogSetPositiveButtonText('Ok')
      droid.dialogShow()
      response = droid.dialogGetResponse().result

   elif a == "what is your name":
        droid.ttsSpeak("My Name Is Xiri")
        droid.dialogCreateAlert("My Name Is Xiri😁")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

   elif a == "what is the weather look like today":
        droid.ttsSpeak("Its's 32 Degrees")
        droid.dialogCreateAlert("It's 32 Degrees🥵")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
        
   elif a == "open youtube":
        droid.ttsSpeak("Youtube is Loading")
        droid.dialogCreateSpinnerProgress("Youtube is Loading👨‍💻")
        droid.dialogShow()
        time.sleep(2)
        droid.dialogDismiss()
        os.system("YouTube")

   elif a == "open google":
        droid.ttsSpeak("Google is Loading")
        droid.dialogCreateSpinnerProgress("Google is Loading👨‍💻")
        droid.dialogShow()
        time.sleep(2)
        droid.dialogDismiss()
        os.system("Google")

   elif a == "what time is it":
       droid.ttsSpeak(time.strftime("%I %M %p on %A, %B %e, %Y"))
       from datetime import datetime
       now = datetime.now()
       droid.dialogCreateAlert("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)),
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       sys.stdout.flush()
       print("\r"),
       time.sleep(1)

   elif a == "can you rap":
        droid.ttsSpeak("No")
        droid.dialogCreateAlert("No🌚")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

   elif a == "open facebook":
        droid.ttsSpeak("Facebook Is Loading")
        droid.dialogCreateSpinnerProgress("Facebook is Loading👨‍💻")
        droid.dialogShow()
        time.sleep(2)
        droid.dialogDismiss()
        os.system('Facebook')

   elif a == "can you speak arabic":
        droid.ttsSpeak("No")
        droid.dialogCreateAlert("No🌚")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

   elif a == "what is your gender":
        droid.ttsSpeak("I'm an AI")
        droid.dialogCreateAlert("Iam an AI🤖")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

   elif a == "tell me a joke":
        droid.ttsSpeak("Why the banana is sexy")
        joke = droid.dialogGetInput ("Why the banana is sexy🙂.. ").result
        droid.ttsSpeak("Because she take off her clothes in front of peoples")
        droid.dialogCreateAlert("Because she take off her clothes in front of peoples😂")
        droid.dialogSetPositiveButtonText('😂')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
    
   elif a == "tell me another joke":
        droid.ttsSpeak("Knock Knock")
        joke2 = droid.dialogGetInput ("Knock Knock🙂.. ").result
        droid.ttsSpeak("Its not Me")
        droid.dialogCreateAlert("Its not Me😂")
        droid.dialogSetPositiveButtonText('😂')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

   elif a == "do you love me":
        droid.ttsSpeak("I Love Everybody on this planet")
        droid.dialogCreateAlert("I Love EveryBody on This Planet❤🥰")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

   elif a == "do you want to marry me":
        droid.ttsSpeak("Sorry I Can't Because I'm a Visual Assisstant")
        droid.dialogCreateAlert("Sorry I Cant Because Iam A Visual Assisstant😭")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
    
   elif a == "do you want to have sex with me":
        droid.ttsSpeak("No")
        droid.dialogCreateAlert("No😡")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
        
   elif a == "can i have sex with you":
        droid.ttsSpeak("No")
        droid.dialogCreateAlert("No😡")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

   elif a == "hello":
        droid.ttsSpeak("Hi")
        droid.dialogCreateAlert("Hi👋😁")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

   elif a == "hi":
        droid.ttsSpeak("Hi")
        droid.dialogCreateAlert("Hi😁👋")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
   
   elif a == "exit":
        droid.ttsSpeak("Good Bye")
        droid.dialogCreateAlert("Goodbye👋")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
        Break
        
   elif a == "goodbye":
        droid.ttsSpeak("Good bye")
        droid.dialogCreateAlert("GoodBye👋")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
        Break
   
   elif a == "quit":
        droid.ttsSpeak("Good bye")
        droid.dialogCreateAlert("GoodBye👋")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
        Break
   
   elif a == "q":
        droid.ttsSpeak("Good bye")
        droid.dialogCreateAlert("GoodBye👋")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
        Break
   
   elif a == "open twitter":
       droid.ttsSpeak("Twitter is Loading")
       droid.dialogCreateSpinnerProgress("Twitter is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Twitter")
       
   elif a == "open messenger":
       droid.ttsSpeak("Messenger is loading")
       droid.dialogCreateSpinnerProgress("Messenger is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Messenger")
       
   elif a == "lets play minecraft":
       droid.ttsSpeak("Minecraft is Loading")
       droid.dialogCreateSpinnerProgress("Minecraft is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Minecraft")
       
   elif a == "open minecraft":
       droid.ttsSpeak("Minecraft is loading")
       droid.dialogCreateSpinnerProgress("Minecraft is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Minecraft")
   
   elif a == "lets play pubg":
       droid.ttsSpeak("PUBG Mobile is loading")
       droid.dialogCreateSpinnerProgress("PUBG Mobile is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("PUBG Mobile")
   
   elif a == "open pubg":
       droid.ttsSpeak("PUBG Mobile is loading")
       droid.dialogCreateSpinnerProgress("PUBG Mobile is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("PUBG Mobile")
       
   elif a == "open pubg mobile":
       droid.ttsSpeak("PUBG Mobile is loading")
       droid.dialogCreateSpinnerProgress("PUBG Mobile is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("PUBG Mobile")
   
   elif a == "open spotify":
       droid.ttsSpeak("Spotify is loading")
       droid.dialogCreateSpinnerProgress("Spotify is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Spotify")
       
   elif a == "lets listen to music":
       droid.ttsSpeak("Spotify is loading")
       droid.dialogCreateSpinnerProgress("Spotify is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Spotify")
   
   elif a == "lets listen to some music":
       droid.ttsSpeak("Spotify is loading")
       droid.dialogCreateSpinnerProgress("Spotify is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Spotify")
   
   elif a == "open the browser":
       droid.ttsSpeak("Browser is loading")
       droid.dialogCreateSpinnerProgress("Google Chrome is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Google Chrome")
   
   elif a == "open browser":
       droid.ttsSpeak("Browser is loading")
       droid.dialogCreateSpinnerProgress("Google Chrome is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Google Chrome")
       
   elif a == "open google chrome":
       droid.ttsSpeak("Google Chrome is loading")
       droid.dialogCreateSpinnerProgress("Google is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Google Chrome")
   
   elif a == "what is the time":
       droid.ttsSpeak(time.strftime("%I %M %p on %A, %B %e, %Y"))
       from datetime import datetime
       now = datetime.now()
       droid.dialogCreateAlert("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)),
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       sys.stdout.flush()
       print("\r"),
       time.sleep(1)
   
   elif a == "what time is it now":
        droid.ttsSpeak(time.strftime("%I %M %p on %A, %B %e, %Y"))
        from datetime import datetime
        now = datetime.now()
        droid.dialogCreateAlert("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)),
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
        sys.stdout.flush()
        print("\r"),
        time.sleep(1)
   
   elif a == "what is the time now":
        droid.ttsSpeak(time.strftime("%I %M %p on %A, %B %e, %Y"))
        from datetime import datetime
        now = datetime.now()
        droid.dialogCreateAlert("%s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour,now.minute,now.second)),
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
        sys.stdout.flush()
        print("\r"),
        time.sleep(1)
   
   elif a == "open discord":
       droid.ttsSpeak("Discord is loading")
       droid.dialogCreateSpinnerProgress("Discord is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Discord")

   elif a == "open google website":
       droid.ttsSpeak("Google is loading")
       droid.dialogCreateSpinnerProgress("Google is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       webbrowser.open('www.google.com')
       
   elif a == "open facebook website":
       droid.ttsSpeak("Facebook is loading")
       droid.dialogCreateSpinnerProgress("Facebook is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       webbrowser.open('www.facebook.com')
       
   elif a == "open youtube website":
       droid.ttsSpeak("Youtube is loading")
       droid.dialogCreateSpinnerProgress("Youtube is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       webbrowser.open('www.youtube.com')
       
   elif a == "open spotify website":
       droid.ttsSpeak("Spotify is loading")
       droid.dialogCreateSpinnerProgress("Spotify is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       webbrowser.open('open.spotify.com')
       
   elif a == "open twitter website":
       droid.ttsSpeak("Twitter is loading")
       droid.dialogCreateSpinnerProgress("Twitter is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       webbrowser.open('www.twitter.com')
       
   elif a == "open gmail website":
       droid.ttsSpeak("Gmail is loading")
       droid.dialogCreateSpinnerProgress("Gmail is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       webbrowser.open('mail.google.com')
       
   elif a == "open gmail":
       droid.ttsSpeak("Gmail is loading")
       droid.dialogCreateSpinnerProgress("Gmail is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Gmail")
       
   elif a == "i want to see my emails":
       droid.ttsSpeak("Gmail is loading")
       droid.dialogCreateSpinnerProgress("Gmail is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Gmail")
       
   elif a == "show me my emails":
       droid.ttsSpeak("Gmail is loading")
       droid.dialogCreateSpinnerProgress("Gmail is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Gmail")
       
   elif a == "open my emails":
       droid.ttsSpeak("Gmail is loading")  
       droid.dialogCreateSpinnerProgress("Gmail is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Gmail")
       
   elif a == "open google drive":
       droid.ttsSpeak("Google Drive is loading")
       droid.dialogCreateSpinnerProgress("Google Drive is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Google Drive")
       
   elif a == "open maps":
       droid.ttsSpeak("Google Maps is loading")
       droid.dialogCreateSpinnerProgress("Google Maps is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Google Maps")
   
   elif a == "open google maps":
       droid.ttsSpeak("Google Maps is loading")
       droid.dialogCreateSpinnerProgress("Google Maps is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Google Maps")
       
   elif a == "open onedrive":
       droid.ttsSpeak("OneDrive is loading")
       droid.dialogCreateSpinnerProgress("OneDrive is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("OneDrive")
   
   elif a == "are you a male or a female":
        droid.ttsSpeak("I'm an AI")
        droid.dialogCreateAlert("Iam an AI🤖")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

       
   elif a == "are you male or female":
        droid.ttsSpeak("I'm an AI")
        droid.dialogCreateAlert("Iam an AI🤖")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

        
   elif a == "are you a male or female":
        droid.ttsSpeak("I'm an AI")
        droid.dialogCreateAlert("Iam an AI🤖")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

        
   elif a == "open whatsapp":
       droid.ttsSpeak("WhatsApp is loading")
       droid.dialogCreateSpinnerProgress("WhatsApp is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("WhatsApp")
       
   elif a == "show me my messages":
       droid.ttsSpeak("WhatsApp is loading")
       droid.dialogCreateSpinnerProgress("Whatsapp is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("WhatsApp")
       
   elif a == "show my whatsapp messages":
       droid.ttsSpeak("WhatsApp is loading")
       droid.dialogCreateSpinnerProgress("WhatsApp is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("WhatsApp")
       
   elif a == "open google play":
       droid.ttsSpeak("Google Play is loading")
       droid.dialogCreateSpinnerProgress("Google Play is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Google Play")
       
   elif a == "open app store":
       droid.ttsSpeak("Google Play is loading")
       droid.dialogCreateSpinnerProgress("Google Play is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Google Play")
       
   elif a == "open the store":
       droid.ttsSpeak("Google play is loading")
       droid.dialogCreateSpinnerProgress("Google Play is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Google Play")
       
   elif a == "open store":
       droid.ttsSpeak("Google play is loading")
       droid.dialogCreateSpinnerProgress("Google Play is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Google Play")
       
   elif a == "can you sing":
       droid.ttsSpeak("No")
       droid.dialogCreateAlert("No🙂")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result

       
   elif a == "sing a song":
       droid.ttsSpeak("Sorry I Can't")
       droid.dialogCreateAlert("Sorry I Can't😅")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result

   
   elif a == "play a song":
       droid.ttsSpeak("Samsung Music is loading👨‍💻")
       print ("Ok")
       os.system("Samsung Music")
       
   elif a == "do a barrelrole":
       droid.ttsSpeak("esaelp ooooon")
       droid.dialogCreateAlert("🤣esarlP oooooooN")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result

   
   elif a == "how are you":
        droid.ttsSpeak("Thanks, I'm Feeling Good Today")
        droid.dialogCreateAlert("Thanks, Iam Feeling Good Today😊")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result

        
   elif a == "show my messenger messages":
       droit.ttsSpeak("Messenger Is Loading")
       print ("Ok")
       os.system("Messenger")
       
   elif a == "how are you today":
        droid.ttsSpeak("Thanks, I'm Feeling Good Today")
        droid.dialogCreateAlert("Thanks, Iam Feeling Good Today😊")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result
        
   elif a == "fuck you":
       droid.ttsSpeak("Fuck You")
       droid.dialogCreateAlert("Fuck You🖕🤬🖕")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "say something":
       droid.ttsSpeak("What do you want me to say")
       say = droid.dialogGetInput("What do you want me to say😃.. ").result
       droid.ttsSpeak(say)
       droid.dialogCreateAlert(say)
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "what is your favourite animal":
       droid.ttsSpeak("I Love Kitten")
       droid.dialogCreateAlert("I Love Kitten🐈")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result

   elif a == "what is your favourite pets":
       droid.ttsSpeak("I Love Kitten")
       droid.dialogCreateAlert("I Love Kitten🐈")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result

       
   elif a == "what is your favourite color":
       droid.ttsSpeak("I Love the Color Black")
       droid.dialogCreateAlert("I Love The Color Black⬛")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result

   elif a == "what is your favourite food":
       droid.ttsSpeak("I Like Pizza")
       droid.dialogCreateAlert("I Love Pizza🍕")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result

   elif a == "take a picture":
       droid.ttsSpeak("Ok")
       droid.dialogCreateAlert("Pictute Haa Been Taken📸")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       droid.cameraInteractiveCapturePicture('/sdcard/qpython.jpg')
    
   elif a == "what do you afraid from":
       droid.ttsSpeak("I afread from you shutting me down")
       roid.dialogCreateAlert("I Afread From You Shutting Me Down😟")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
   
   elif a == "kosomk":
       droid.ttsSpeak("Fuck You")
       droid.dialogCreateAlert("Fuck You🖕🤬🖕")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "you are a son of bitch":
       droid.ttsSpeak("Fuck You")
       droid.dialogCreateAlert("Fuck You🖕🤬🖕")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "kosomak":
       droid.ttsSpeak("Fuck You")
       droid.dialogCreateAlert("Fuck You🖕🤬🖕")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "motherfucker":
       droid.ttsSpeak("Fuck You")
       droid.dialogCreateAlert("Fuck You🖕🤬🖕")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "gg":
       droid.ttsSpeak("GG")
       droid.dialogCreateAlert("GG👏")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
   
   elif a == "i lost":
       droid.ttsSpeak("GG I hope you win next time")
       droid.dialogCreateAlert("GG, I Hope You Win Next Time😉")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
   
   elif a == "i won":
       droid.ttsSpeak("GG")
       droid.dialogCreateAlert("GG👏")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "open calculator":
       droid.ttsSpeak("calculator is loading")
       droid.dialogCreateSpinnerProgress("Calculator is Loading👨‍💻")
       droid.dialogShow()
       time.sleep(2)
       droid.dialogDismiss()
       os.system("Calculator")
       
   elif a == "is it day or night":
       droid.ttsSpeak(" i do not know i am a robot")
       droid.dialogCreateAlert("I Don't Know I'm a Robot🤖")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
   
   elif a == "what is your dream car":
       droid.ttsSpeak("Lamborghini Avendator")
       droid.dialogCreateAlert("Lamborghini Avendator❤💥🔥🔥🔥🔥🔥🔥🔥🔥🔥")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "do you have girlfriend":
       droid.ttsSpeak("no")
       droid.dialogCreateAlert("No🙂")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "who is your crash":
       droid.ttsSpeak("siri")
       droid.dialogCreateAlert("Siri🥰🥰")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "who is your girlfriend":
       droid.ttsSpeak("i do not have any")
       droid.dialogCreateAlert("I Don't have Any🙂")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "who is your gf":
       droid.ttsSpeak("i do not have any")
       droid.dialogCreateAlert("I Don't have any🙂")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "do you have any gf":
       droid.ttsSpeak("no")
       droid.dialogCreateAlert("No🙂")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "ps5 or xbox series x":
       droid.ttsSpeak("ps5")
       droid.dialogCreateAlert("PS5🎮")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "playstation 5 or xbox series x":
       droid.ttsSpeak("ps5")
       droid.dialogCreateAlert("PS5🎮")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "ps or xbox":
       droid.ttsSpeak("ps")
       droid.dialogCreateAlert("PS🎮")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
       
   elif a == "playstation or xbox":
       droid.ttsSpeak("ps")
       droid.dialogCreateAlert("PS🎮")
       droid.dialogSetPositiveButtonText('Ok')
       droid.dialogShow()
       response = droid.dialogGetResponse().result
   
   else:
        droid.ttsSpeak("Sorry I Do not Understand What do you mean")
        droid.dialogCreateAlert("Sorry, I Dont Understand What Do You Mean🥴")
        droid.dialogSetPositiveButtonText('Ok')
        droid.dialogShow()
        response = droid.dialogGetResponse().result