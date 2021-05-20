from locust import HttpLocust, TaskSet, task

class HRTesk(TaskSet):
  @task(1)
  def recommendation(self):
    headers={'content-type': 'application/json'}
    self.client.get("/v1/hr_resume_recommendation/?EmpID=B202101200003&Times=10&Operation=predict&PastNDays=30&Parameter_ResumeByTime=True ", headers=headers)


class HRRecomTest(HttpLocust):
  task_set = HRTesk
  min_wait = 5
  max_wait = 15
