# Load Testing Script

This script is used for load testing a list of URLs. It uses the Locust library for Python to simulate user behavior and measure the performance of the web pages.

## How it works

The script reads a list of URLs from a DataFrame and simulates user behavior by sending GET requests to these URLs. The response of each request is checked, and if the status code is 200, the request is marked as successful. Otherwise, it is marked as a failure.

## Classes

- `UserBehavior`: This class defines the behavior of a simulated user. It includes a task that sends GET requests to the URLs and checks the response.

- `User`: This class represents a user in the load test. It uses the tasks and wait time defined in the `UserBehavior` class.

- `MyLocustRunner`: This class is a custom runner for the load test. It uses the `MyLoadTestShape` class to shape the load test.

## How to Run the Script
To run the script, navigate to the directory containing the script in your terminal and run the following command:

```
locust -f load_test_script.py

```
### NOTE: 
> The script will run on http://localhost:8089 by default. You can access the Locust web interface by opening a browser and going to http://localhost:8089.
 - make sure to add the subdomains to Data/url_list.xlsx file replacing the existing subdomains.

> The script will prompt you to enter the number of users and the hatch rate for the load test if you do not provide these values as command-line arguments when running the script. to do so, run the following command:

    ```
    locust -f load_test_script.py --users 10 --hatch-rate 2

    ```
    > This command will run the load test with 10 users and a hatch rate of 2 users per second.

> You can also specify the host URL for the load test by using the `--host` option. For example:

    ```
    locust -f load_test_script.py --host http://example.com

    ```