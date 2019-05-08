from locust import HttpLocust, TaskSequence, seq_task


class UserBehavior(TaskSequence):

    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        self.client.post("/login", json={"account": "account", "password": "password"})
        # self.client.post("/login", data={"account": "account", "password": "password"})

    def logout(self):
        self.client.post("/logout")

    @seq_task(2)
    def index(self):
        self.client.get("/")

    @seq_task(1)
    def profile(self):
        self.client.get("/note")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000
