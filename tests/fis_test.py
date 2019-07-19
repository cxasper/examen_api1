from locust import HttpLocust, TaskSet, task

class Task(TaskSet):
    #def on_start(self):
        #self.login()

    #def login(self):
        #self.client.post('/api/login/', {'username':'cxasper23', 'password':'qweasd23Q'})

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



class WebsiteTest(HttpLocust):
    task_set = Task
    max_wait = 9000
