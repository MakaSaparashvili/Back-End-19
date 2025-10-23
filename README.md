Python 3.13.5

Task
1. Create the Product Model
Create a Django model named Product with fields:

 from django.db import models

 class Product(models.Model):
    name = models.CharField(max_length=100)
    expiration_date = models.DateField()
    is_active = models.BooleanField(default=True)
    
2. Implement a Periodic Celery Task
The task should run once a day (using Celery Beat).
Query products whose expiration_date is less than or equal to today and is_active is True.
For each expired product, set is_active to False and save.
Print or log how many products were marked inactive.

4. Add Task Timeout Handling
Simulate a long task by adding a sleep (e.g., time.sleep(30)) inside the task.
Set a soft timeout of 10 seconds and a hard timeout of 15 seconds for the task.
Catch the SoftTimeLimitExceeded exception and log a warning that the task timed out.
Ensure the task exits gracefully without crashing.
