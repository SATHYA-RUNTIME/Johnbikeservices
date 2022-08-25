# Johnbikeservices
this is the project for booking the bike service.

# must do to run 


> #### 1.first you need to install django in your computer Goto Terminal And Run this Commands .
> > for Linux & Mac `python -m pip install Django`
> > for Windows  `py -m pip install Django`



> #### 2.i am using mysql. ` Must_Do (you need to create a new database called "johnservice" and must change mysql password in setting.py Line:82 put your mysql password . if your username is root skip that otherwise put your username instead of mine in Line:81  ) `
>> #### 2.1 you Don't worry about Database Schema because all Database Schema are mention in `models.py` you just create database and change username password all those things and run following command. 



> #### 3. Just open your terminal change directory to current path (EX: myfolder name is plan_B inside plan_B i have django project called johnbikeservice so in terminal **cd plan_B/johnbikeservice**) please move to your dir.





> #### 4.move your directory And type this command (if you use python old version just type **python**) otherwise run line by line.
    
    `python3 manage.py makemigrations`  
    
    `python3 manage.py migrate`
    
    `python3 manage.py runserver`
    
    
  > when you successfully run the python3 manage.py runserver in terminal a address shown **like** `http://127.0.0.1:8000` just copy and paste in your browser.
    
     
> #### 5. if you got any error with missing python module just try to install with pip (EX: pip install <missing package>),Check your internet connection because the mail sending services get blocked.
 
> ## `6. Admin username & Password : adminuser & dhoni07`
  
> #### 7. i create project like admin given services details and store it in a database no fresh db, so 0 service not avilable so Go to `Admin->admin login->Add&Edit_services(go inside)->create services` try to Add some services "like :oli change,water wash". 
  
  
  
  # project Workflow
  
  ### USER WORKFLOW
  
  >> First as a user you enter into the application and register your details and login go to services and book what service you want.when user book the every single booking the both user and owner recive mail regarding bike service booking.
  
  ### ADMIN WORKFLOW
  
  >> the Admin access  power gives To Owner and service_Worker, Use the admin login to come inside the admin panal,here we have the three different access for owner and worker.
  > When the People book bike services,the service Detail comes into the worker page when the worker complete the work and he just click the `Click TO Finish` Button and the same time In the owner Page one button arrive called `Ready For Delivery`. Before the work complete the button  like `Pending`.      Just click the `Ready For Delivery` to user recive mail regarding bike delivery. Inside `View Booking List` at the top corner one button shown called `View All Detail` once click that to view the all data of booking with the status.
  
> Inside the Add & Edit service admin can do the operation like `Create,Read,Update,Delete` , When Ever You add new service that particular service added into the service booking page.
> At the End of the Home page `showMore` Button arrive just click to view all service offer by company.
  
  
  >This is short note of my project and thankyou. 
