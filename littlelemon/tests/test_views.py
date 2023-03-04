from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APIClient, force_authenticate
from rest_framework.authtoken.models import Token
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testemail@test.com', password='testpassword', username='testname')
        # self.user.is_superuser = True
        # self.user.save(update_fields=["is_superuser"])
        self.user.save()
        
        # self.client = Client()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.menu1 = Menu.objects.create(title="IceCream", price=6, inventory=100)
        self.menu2 = Menu.objects.create(title="Drink", price=4, inventory=200)
        self.serializer = MenuSerializer(instance=[self.menu1,self.menu2], many=True)

    def test_getall(self):
        response = self.client.get(reverse('menu'))
        self.assertEquals(response.data, self.serializer.data)
