# BDMH_Project
This repo contains code about heart disease prediction system using Machine Learning and website development using Django

#### RESULTS
|  **Models**		                |	**Accuracy**	| 	
| ------------- 	              | ------------- 	|    
| Decision Tree |     75.63 %| 
| Random Forest |     74.78 %| 
| SVM|                82.35 %| 
| KNN    |            80.67 %| 
| Multilayer Perceptron |   85.71 %| 

Inside the website Folder
Steps to run:
1. **create a virtual environment using:** </br>
             conda create --name <name_of_env> django
2. **Activate the above environment:** </br>
              activate <name_of_env>
3. **run:** </br>
     python -r requirements.txt
4. **cd into the website_work directory**.
5. **run:** </br>
      python manage.py migrate </br>
      python manage.py makemigrations </br>
      python manage.py migrate </br>
      python manage.py runserver </br>
      
      

