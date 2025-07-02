from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Tarea

class TareaTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='sun', password='12345678')
        self.client.force_authenticate(user=self.user)
        Tarea.objects.create(titulo='Tarea 1', descripcion='Descripción', usuario=self.user, completado=False)

    def test_create_tarea(self):
        data = {'titulo': 'Tarea 2', 'descripcion': 'Nueva tarea', 'completado': False, 'usuario': self.user.id}
        response = self.client.post('/tareas/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Tarea.objects.count(), 2)

    def test_usuario_no_autenticado(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/tareas/')
        self.assertEqual(response.status_code, 403)
