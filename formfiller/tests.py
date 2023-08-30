from django.test import TestCase
from django.urls import reverse
from .models import UserInput
from .forms import UserFeedbackForm, SignupForm
from .views import feedback_form_view, submit_signup, homepage, internet_page, contact_page, thank_you, tv_page

class ViewsTest(TestCase):

    def test_feedback_form_data_saved(self):
        data = {
            'customer_name': 'Jane Smith',
            'customer_complaint': 'Another test complaint',
            'customer_email': 'jane@example.com',
        }
        response = self.client.post(reverse('feedback_form'), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

        # Verify that the data is saved in the database
        saved_input = UserInput.objects.last()  # Get the latest entry
        self.assertEqual(saved_input.customer_name, 'Jane Smith')
        self.assertEqual(saved_input.customer_complaint, 'Another test complaint')
        self.assertEqual(saved_input.customer_email, 'jane@example.com')

    def test_feedback_form_view_get(self):
        response = self.client.get(reverse('feedback_form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'input_form.html')

    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_internet_page_view(self):
        response = self.client.get(reverse('internet_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'internet_page.html')

    def test_contact_page_view(self):
        response = self.client.get(reverse('contact_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'input_form.html')

    def test_thank_you_view(self):
        response = self.client.get(reverse('thank_you'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thank_you.html')

    def test_tv_page_view(self):
        response = self.client.get(reverse('tv_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tv.html')
