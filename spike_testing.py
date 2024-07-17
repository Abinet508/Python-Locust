import argparse
import random
from locust import FastHttpUser, LoadTestShape, TaskSet, between, task

class MyCustomShape(LoadTestShape):
    """
    This class defines a custom load test shape for Locust. It will create a load test scenario where the number of users

    Args:
        LoadTestShape (class): The base class for all load test shapes in Locust.

    Returns:
        tuple: A tuple with two values: the number of users to spawn and the spawn rate.
    """
    time_limit = 600
    spawn_rate = 10

    def tick(self):
        """
        This method defines a custom load test shape for Locust. It will create a load test scenario where the number of users
        to spawn is calculated based on the current time.
        
        Returns:
            tuple: A tuple with two values: the number of users to spawn and the spawn rate.
        """
        run_time = self.get_run_time()
        if run_time < self.time_limit:
            user_count = random.randrange(13288)
            return (user_count, self.spawn_rate)

        return None
    
class UserBehavior(TaskSet):
    host = "http://staging.bootcamp.store.supersqa.com"
    wait_time = between(1, 2)
    
    @task
    def index(self):
        response = self.client.get("/")
        if response.status_code == 200:
            response.success()
        else:
            response.failure('Failed to load page')
class User(FastHttpUser):
    tasks = [UserBehavior]
    wait_time = UserBehavior.wait_time
    host = UserBehavior.host
    
if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--host", type=str, default="http://staging.bootcamp.store.supersqa.com")
    args = args.parse_args()
    UserBehavior.host = args.host
    