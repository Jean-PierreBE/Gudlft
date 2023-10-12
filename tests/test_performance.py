from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task(3)
    def home(self):
        self.client.get("/")

    @task(3)
    def dashboard(self):
        self.client.get("/dashboard")

    @task(3)
    def access(self):
        self.client.post("/showSummary", data={
            "email": "admin@irontemple.com",
        })

    @task(3)
    def book(self):
        self.client.get('/book/Spring Festival/Simply Lift')

    @task(3)
    def purchase_ok(self):
        self.client.post("/purchasePlaces", data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "submit_button": "Book",
            "places": 5,
        })
