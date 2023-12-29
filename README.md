# Fittbook Web Application
![Screenshot (9)](https://github.com/kpperez/Fittbook-Web-App/assets/123265217/9af167e8-9efb-4419-9b88-08b797748b8a)
## Table of Contents 
- [Description](https://github.com/kpperez/Fittbook-Web-App?tab=readme-ov-file#description)
  - [Overview](https://github.com/kpperez/Fittbook-Web-App?tab=readme-ov-file#overview)
  - [Technologies Used](https://github.com/kpperez/Fittbook-Web-App?tab=readme-ov-file#technologies-used)
  - [Challenges](https://github.com/kpperez/Fittbook-Web-App?tab=readme-ov-file#challenges)
  - [Future Modifications](https://github.com/kpperez/Fittbook-Web-App?tab=readme-ov-file#future-modifications)
- [Installation & Setup](https://github.com/kpperez/Fittbook-Web-App?tab=readme-ov-file#installation--setup)
- [Instructions](https://github.com/kpperez/Fittbook-Web-App?tab=readme-ov-file#instructions)

## Description
### Overview:
This comprehensive web application is designed to empower users in tracking and planning their fitness workouts. Each user benefits from a personalized, secure account accessible through the login portal. Leveraging relational databases, user warnings, and interactive JavaScript, this platform offers a robust and private environment for managing workout data.
### Technologies Used: 
-	Front End: Bootstrap, HTML, JavaScript
-	Back End: Python, SQLAlchemy, SQLite
### Challenges:
One notable challenge encountered during the development of this web application was the formulation of the accurate datetime format for seamless database storage. Additionally, overcoming complexities in user authentication and authorization mechanisms posed significant hurdles in ensuring a secure and streamlined user experience.
### Future Modifications:
In upcoming iterations, the plan is to introduce an additional database dedicated to diverse workouts, providing insights into targeted muscle groups as a dropdown menu. Additionally, a planned feature includes the development of a feed page, fostering a social element where users can share and view workouts of their connected friends within the application.
## Installation & Setup
Have the latest version of Python installed. 
```
git clone <repo-url>
```
```
pip install -r requirements.txt
```
Run the app in the terminal
```
python main.py
```
View the app in the Web browser<br/>
http://127.0.0.1:5000

## Instructions
1. Set up a new user account with an email, first name, and a 7-character password.
![Screenshot (7)](https://github.com/kpperez/Fittbook-Web-App/assets/123265217/15a70972-239a-461a-bb09-93779f1e9c32)
2. Once the new user is created you can add a new workout. The default date is set to today, you will get a confirmation message in the top left corner when your workout is added to the database.  
![Screenshot (8)](https://github.com/kpperez/Fittbook-Web-App/assets/123265217/664175b8-2917-412b-a148-cb5b917f90ce)
Note: The exercise must be at least one character long! If not you will receive an error message. The sets, reps, and weight dropdown menus can be left at zero. 
![Screenshot (13)](https://github.com/kpperez/Fittbook-Web-App/assets/123265217/919f1d14-de6d-477a-8538-eafb52ad63c0)
3. Achieve your fitness goals and share the App! 
