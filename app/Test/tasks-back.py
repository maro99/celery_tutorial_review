from celery import Celery
import time

#  'tasts' = name of the current module,
#  borkser =  pecifying the URL of the message broker you want to use. Here using RabbitMQ
# for RabbitMQ you can use amqp://localhost, or for Redis you can use redis://localhost.
app = Celery('tasks', broker="pyamqp://guest@localhost//")

@app.task
def add(x,y):
    time.sleep(5)
    return x+y
