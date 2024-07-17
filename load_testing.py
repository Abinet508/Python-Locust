from locust import task, between,TaskSet, LoadTestShape
import pandas as pd,os
from locust.runners import LocalRunner
from locust.user.task import TaskSet
from locust import LoadTestShape
from locust import task, FastHttpUser

class MyLoadTestShape(LoadTestShape):
    time_limit = 600
    spawn_rate = 10

    def tick(self):
        run_time = self.get_run_time()

        if run_time < self.time_limit:
            user_count = self.spawn_rate * run_time
            return (user_count, self.spawn_rate)

        return None

class UserBehavior(TaskSet):
    host = "http://staging.bootcamp.store.supersqa.com"
    wait_time = between(1, 2)
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, 'Data')
    df = pd.read_excel(os.path.join(data_dir,'url_list.xlsx'))
    Urllist = df['URL'].tolist()

    @task
    def index(self):
        for url in self.Urllist:
            with self.client.get(url, name='Load Test', catch_response=True) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure('Failed to load page')

class User(FastHttpUser):
    tasks = [UserBehavior]
    wait_time = UserBehavior.wait_time
    host = UserBehavior.host

class MyLocustRunner(LocalRunner):
    def shape_class(self):
        return MyLoadTestShape

if __name__ == "__main__":
    runner = MyLocustRunner()
    runner.add(User)
    runner.start()