# Health Tracking Application

This project is a health tracking application written with Python, HTML and CSS. The project utilizes Django as its web framework.

## Group Members
- **Ryan Baker**
- **Kevin O'Malley**
- **Benjamin Raidman**
- **Mason Russo**

## How to Download and Run The Application
### Clone Repo From GitHub
```
git clone https://github.com/KevinOMalley/COP4521_FitnessApp.git
```
### Install Dependencies
```
pip install -r requirements.txt
```
### Run Program
In the root directory, run:
```
python manage.py runserver
```
Depending on your system/python version the command could be:
```
python3 manage.py runserver
```
Then navigate to the following address in your web browser to see the application: 
http://127.0.0.1:8000/

### Distribution Plan
Distributed program paper:
Right now, our database runs on MySQL hosted by Amazon RDS. We chose to use these because some of us are familiar with Amazon services and MySQL. But should our user base and demands grow, we would need to step up our game to ensure our application can handle it. So, our plan would be to transition to a more distributed server architecture. What does that mean? Well, instead of relying on one server, we would spread out our main server across multiple Amazon servers worldwide. We can do this by using Amazon Web Service(AWS) EC2 instances to host our server. This way, we can boost our computing power and make sure our service is fast and accessible globally. By spreading out our servers like this, we're aiming to make our system more flexible and resilient. It means we can handle more users and keep things running smoothly, even during "peak" times. And, since AWS has a solid infrastructure, we're confident we can make this transition smoothly. For example: If your application needs to handle high traffic or if you want to ensure high availability, you can configure auto-scaling and load balancing using AWS services like Elastic Load Balancing (ELB) and Auto Scaling Groups. We can also implement backup servers in different regions should any of our non-backup servers get physically destroyed. I'd say this puts us in a pretty good place should we ever need to actually implement a more distributed server architecture.
