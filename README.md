# cooperative-scripts
Using generators to build scripts that you can edit and run without losing data between two runs. 
Not the best way to solve this problem, but I find generators a very elegant way to do so.

# Usage

Sometimes, I have to run a lot of tasks on a remote server. To avoid hammering the server and disrupting its normal workflow, I would usually write a script that looks like this:

```python
def run():
  huge_list_of_tasks = fetch_task_ids_from_db()
  for task in huge_list_of_tasks:
      run_remote(task)
      sleep(10)
```

But then I realize that I was too pessimistic and that a 5s sleep interval is better. I would then have to stop the running script, edit it and re-run it, losing track of already ran tasks.
The script exposed in the repo uses generators to solve this problem. 

The previous example would be re-written like this:

```python
def run():
    while True:
        data = (yield)  # get data from storage

        if data is None:  # first run, initialize
            data = fetch_task_ids_from_db()

        if not data:  # break condition
            break

        # Logic goes here
        run_remote(data.pop())
        sleep(10)
        ###

        yield data  # save data
```

Running the script is done by: python run.py path/to/file
If I want to switch from a 10s to a 5s sleep interval, I would just change sleep(10) to sleep(5), and then Ctrl+C the running python script.
The script will then be reloaded and resumed from where it stoped.

# Example
```python
data_init = range(10)

def run():
    while True:
        data = (yield)  # get data from storage

        if data is None:  # first run, initialize
            data = data_init

        if not data:  # break condition
            break

        # Logic goes here
        time_sleep = 2
        print data.pop()
        print 'sleeping %ss' % time_sleep
        sleep(time_sleep)
        ###

        yield data  # save data
```

Output:

```
9 <-- sleep interval is 2
sleeping 2s
8
sleeping 2s
7
sleeping 2s
6
sleeping 2s
^CYou have 2s to Keyboard interrupt the program for real. Otherwise, it will be reloaded and resumed <--- I switched to a 0.5 sleep interval
5 <--- resumes
sleeping 0.5s
4
sleeping 0.5s
3
sleeping 0.5s
2
sleeping 0.5s
1
sleeping 0.5s
0
sleeping 0.5s
byebye
```

