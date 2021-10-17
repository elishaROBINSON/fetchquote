from celery import task 
 

@task(name='scheduled_update_pair') 
def send_import_summary():
     print("update the pair")