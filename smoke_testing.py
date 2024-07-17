
from locust import HttpUser, FastHttpUser, TaskSet, LoadTestShape, between, task
from locust import run_single_user
import argparse
import argparse

class SmokeTesting(TaskSet):
    @task
    def index(self):
        self.client.get("/")

class User(HttpUser):
    tasks = [SmokeTesting]
    wait_time = between(1, 3)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="http://staging.bootcamp.store.supersqa.com")
    args = parser.parse_args()

    User.host = args.host
    run_single_user(User)