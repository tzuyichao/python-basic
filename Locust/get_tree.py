from locust import HttpLocust, TaskSet, task
import random

class TreeTest(TaskSet):
    def on_start(self):
        self.gids = ["Ga",
                     "GA",
                     "GE",
                     "GaZ",
                     "GfZ",
                     "Gkt",
                     "GoY",
                     "Gtr",
                     "GxU",
                     "GxY",
                     "Gy0",
                     "Gy4",
                     "GPU",
                     "GPY",
                     "G11k",
                     "G370",
                     "G3ea",
                     "G3iC",
                     "G3iN",
                     "G3ja",
                     "G3jG"
                    ]
        gid = self.gids[random.randint(0, len(self.gids)-1)]
        self.url = f"/v1/tree/{gid}"

    @task
    def get_orgGroup(self):
        my_header = {"AppKey": "a1d07066-bfd3-4fe4-b062-5219e9a2c7f0",
                 "Accept": "application/json;charset=UTF-8"}
        self.client.get(self.url, headers = my_header)

class WebsiteUser(HttpLocust):
    task_set = TreeTest
    min_wait = 5000
    max_wait = 9000

