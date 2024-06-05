# ****************** Currency Converter Chatbot ******************

# Telegram Name : CurrencyConvertBot    (https://t.me/Currency004bot)

# Tools and Framework 

'''
DialogFlow : Google Product for creation of the chatbot and also trani chatbot on dialogflow

ngrok : This is used for making our application online . (This is one type of terminal for the application for runing over server on online)
        -> This is only useable whenever your server is open on your machine.
        -> ngrok is used only for testing your chatbot it is not used for perment online of your chatbot.
        
    +>> Steps for Starting ngrok :

        1. You need to Download ngrok for windows 
        
        2. After You need to run ngrok.exe file
        
        3. Enter Authentication command : ngrok config add-authtoken 2hEU4QAUE26qNvDFiSD0x5F78cF_48yudnDQtL3bZDEXE5NtV
        
        4. After Authentication you need write command : ngrok http port_id
        
        
    =>> Now Your Application is runing online whenver server is runing on your machine .
'''


# Information about chatbot

'''
ChatBot : Chatbot is a software application design to "simulate human conversation" , enabling interaction between human and comupter through "text" or "voice" .

+>> Types of ChatBot :-

    1. Rule-Based Chatbot :

        - Predefiend Rules  : They follow scripted path and respond with predetermind answer
        
        - Limited Flexibility : Handdle only specific queries and scenarios.
        
        - Use case  : FAQ bots ,Simple customer service based
    
    
    2. AI-Powered Chatbot : 

        - Machine Learning and NLP based chatbot : use ML and NLP for understand of usre input and generate responses .

        - Context Awareness : Capable to understanding context ,Managing Conversations dynemically and learning from interections .
        
        - Use Case : 
        

+>> Application of Chatbots :-

    1. Customer Service  : 24/7 Support  , Efficiency
    
    2. E-commerce : Product Recommendation  ,Order Tracking 
    
    3. Helthcare :  Symptoms Checking ,Appointment Scheduling 
    
    4. Banking and Finance : Account Mangment , Financial Adviced 
    
    5. Entertainment : Content Discovery ,Intractive Games

'''


# Architecture of Currency Converter Chatbot

'''
              ----------
    User  --> | ChatBot| --> Intent  --> Entity  --> Fulfilment
              ----------                                |
                  |                                     |
                  -----<-----------<------------<--------
                                Responce
                                
                                
Intent : Process of Identifying and Classifying the users intent(intention) based on their "input" . (Understading of question by chatbot which is askd by user)
         
         Ex : 1. User Input: "Can you help me book a flight?"  --->  Recognized Intent: "Book Flight"
              2. User Input: "I want to check my account balance."  --->  Recognized Intent: "Check Balance"


Entity : Process of Identifying and extracting "specific data point(key word)" from the Intent (User input ).

         Ex : I want to convert 100USD to INR     --->  Entity :  100USD ,INR


Fulfilment : This is one type of API (Backend) which is used for generate responce using the extract Entitys. (Flsk API ,Pyton etc languages)
'''


# Steps for the creation of the chatbot in DialogFlow


'''
step-1 : First you need to make currency convertor agent. 

step-2 : After You need to create intents for your chatbot. (This is part of the training)

step-3 : Also You can add personality in chatbot using "Small talks" 

step-4 : After you need to create another intent "Currency_Convertor" which is provied json format data .
'''


# Chatbot Fulfilment Step 

'''
1. First You need to create vertual enviernement for your prject.

2. After You need to convert flask app for your chatbot. Which is provied backend for your chatbot.

3. After Creation of the our chatbot you need to create online link using "ngrok". (For Creation of the online link you can check above writen step into tools and Framework)

4. Add website link into the "fulfilment" section of the dialogflow. Also "Enable" webhook into your currency convertor intent.

5. Now you need to used currency converter api for conversion of the currency amount . [API Key For currency conversion  : https://rapidapi.com/airaudoeduardo/api/currency-converter241/playground/apiendpoint_6b4fc249-ae20-4dbe-ab3d-e55a5e1a8b3b]

6. After conversion of the amount you need to send response to the dialogflow chatbot.

    response = {
        'fulfillmentText':"{} {} is {} {}".format(amount ,source_currency ,final_amount ,target_currency)
    }               
    
=>>> Now Ready Your Chatbot

'''

# For Online Deployment of chatbot : 

'''
1. Create Webapplication for flask python on pythonanywhere.com (this is provide online url for your webapplication)


2. After add your application source code 

    pythonanywhere.com -> File -> mysite -> flask_app.py -> Add source code of your flask application
    
    
3. Now You need to install some dependencies for your application and run

4. After Your flask application is online for searching using : https://ronak004.pythonanywhere.com/

5. Add online link of chatbot into the fulfilment section of dialogflow chatbot  (Note  : Into Intent section "Enable" Webhook call for this intent)

    dialogflow -> Currency_converter agent -> fulfillment -> add online link into URL -> Save 

'''

# Summery For Chatbot Creation :

'''

1. you need to create agent and train on Dialogflow 

2. After You need to create flask application for working on input which is send by chatbot (In chatbot don't need to create frontend when you are used dialogflow)

3. Deployment of Your flask application on pythonanywhere.com for free ( create online link)

4. After connect your flask application with dialogflow chatbot using "fulfillment" (add online link in fulfilment url section so chatbot is send post request for user input)

5. After Connect application and chatbot now your chatbot is complete you can add into the telegram ,messneger , etc using "integration" section of dialogflow

    i. You need to create access token using : @BotFather   
    ii. Put Acesstoken into your telegram integration section and now your chatbot is open for anyone on tlegram

'''


# diaglogflow.com : crezyboy0123@gmail.com 
# Pythonanywhere.com  : ronakkantariya12@gmail.com
# Currency Converter api : https://rapidapi.com/airaudoeduardo/api/currency-converter241/playground/apiendpoint_6b4fc249-ae20-4dbe-ab3d-e55a5e1a8b3b
