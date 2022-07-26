from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class SnacksTest(TestCase):
    def test_page_status(self):
        list_response = self.client.get(reverse('snack_list'))
        self.assertEqual(list_response.status_code, 200)

    def test_page_template(self):
        list_response = self.client.get(reverse('snack_list'))
        self.assertTemplateUsed(list_response, 'snack_list.html')

# Unable to test snack_detail as it needs some mock data.
