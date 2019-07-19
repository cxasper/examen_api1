from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        self.client.post('/api/login/', {'username':'cxasper23', 'password':'qweasd23Q'})

    @task(1)
    def productos(self):
        self.client.get('/api/productos')

    @task(2)
    def personas(self):
        self.client.get('/api/personas')

    @task(3)
    def list_creditos(self):
        self.client.get('/api/tipo-creditos')

    @task(4)
    def create_creadito(self):
        self.client.post('/api/tipo-creditos/', {'descripcion': 'prueba de carga' })

    @task(4)
    def plazos(self):
        self.client.get('/api/plazos')

    @task(5)
    def relaciones(self):
        self.client.get('/api/tipo-relacion')

    @task(6)
    def test_charge(self):
        self.client.post('/api/tipo-relacion/', {'descripcion': 'prueba'} )

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    max_wait = 9000
