from locust import HttpLocust, TaskSet, task

class ProductAPITasks(TaskSet):
  @task(1)
  def iabg_zh(self):
    headers={'content-type': 'application/json'}
    self.client.post("/product", json={"lang": "zh-tw", "bg": "IABG"}, headers=headers)

  @task(2)
  def iabg_cn(self):
    headers={'content-type': 'application/json'}
    self.client.post("/product", json={"lang": "zh-cn", "bg": "IABG"}, headers=headers)

class FaQTest(HttpLocust):
  task_set = ProductAPITasks
  min_wait = 5
  max_wait = 15
