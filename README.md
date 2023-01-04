# AI you can speak to using Open AI
Created an early prototpye AI that uses Open AI to generate responses, to your queries. 
Features:
-Can understand two languages at the same time. (Currently English and Hindi). This can be changed in Body>Listen.py. Following is where the code would need to be changed

      try:
              print("Recognizing...")
              query = r.recognize_google(audio,language="hi")   #Change the "hi" to your suited lanuage
        
-Can send messages through whatsapp
-Can open desktop apps on your windows machine, I used windows power tools for this so make sure you have that setup. (win + space should open up search)
-Can google things by saying "google".
-Can visit websites by saying "visit" website_name
-Can generate responses to your questions.

I plan to add and implement many more features like
- YOLOR for object, face detection.
- More social media integration (instagram, facebook)
- Integrate smart home devices.

*I have included all the modules i had installed on requirements.txt. To install them open cmd in the folder and run pip install -r requirements.txt.
*You would also need to run this section from whatsapp.ppy shown below and scan the code it prompts to set it up. 

        from selenium import webdriver
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        import os
        from time import sleep
        from selenium import webdriver
        import pandas as pd
        from Body.Speak import Speak
        import pathlib
        from Body.Listen import MicExecution

        scriptDirectory = pathlib.Path().absolute()

        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--profile-directory=Default")
        options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
        os.system("")
        os.environ["WDM_LOG_LEVEL"] = "0"
        PathofDriver = "DataBase\\chromedriver.exe"
        driver = webdriver.Chrome(PathofDriver,options=options)
        driver.maximize_window()
        driver.get("https://web.whatsapp.com/")
        Speak("Initializing Whatsapp Software.")

*You may need to change the api key in Data>Api.txt. You can get the api key from https://beta.openai.com/account/api-keys. 


