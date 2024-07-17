from locust import task, run_single_user
from locust import FastHttpUser


class myrecording(FastHttpUser):
    host = "https://en.wikipedia.org"
    default_headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "dnt": "1",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://en.wikipedia.org/wiki/Special:Search",
        "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/w/index.php?search=python&title=Special%3ASearch&profile=default&fulltext=1",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/w/index.php?fulltext=1&profile=default&search=python&title=Special%3ASearch&ns0=1",
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(myrecording)
