from locust import HttpUser, task

class ProjectPerfTest(HttpUser):
    @task
    def home(self):
        self.client.get("/")

    @task
    def dashboard(self):
        self.client.get("/dashboard")