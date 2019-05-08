# Locust-skeleton

Take notes for the powerful load test tool- [Lucost](https://github.com/locustio/locust)

skeletons:
- sequence.py: tasks will be executed in order
- random.py: tasks will be executed randomly

## Command

with web UI:
```
locust --host=domain -f locust_files
```

locust server:
http://127.0.0.1:8089/

without web UI
```
locust --host=domain -f locust_files --no-web -c 1000 -r 100 -t 1h30m
```

-c: number of Locust users to spawn
-r: number of users to spawn per second
-t: time limit for the test


## Order of events
1. Locust setup
2. TaskSet setup
3. TaskSet on_start
4. TaskSet tasks
5. TaskSet on_stop
6. TaskSet teardown
7. Locust teardown

## parameter

min_wait/max_wait: simulated user will wait between executing each task,  default to 1000(in ms)


## Decorators

- @task: declaring a task
- @task(3): a task with weight argument=3 (execution ratio)
- @seq_task(1): tasks will be executed in order
