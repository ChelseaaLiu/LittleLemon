from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu2 = Menu.objects.create(title="Drink", price=90, inventory=1000)
        self.serializer = MenuSerializer(instance=[self.menu1,self.menu2], many=True)

    def test_getall(self):
        # token = ""
        response = self.client.get(reverse('menu'))
        self.assertEquals(response.data, self.serializer.data)
