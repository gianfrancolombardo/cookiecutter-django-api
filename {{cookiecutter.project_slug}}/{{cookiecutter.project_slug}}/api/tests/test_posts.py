""" Post tests. """

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Model
from {{cookiecutter.project_slug}}.api.models import Post

class PostAPITestCase(APITestCase):
    """ Posts API test case. """

    def setUp(self):
        self.url = '/posts/'
        self.data = {
            'title': 'Im a title',
            'body': 'Im a great body'
        }
        self.data_error = {
            'body': 'Im a great body'
        }

    def test_list_post_response_success(self):
        """ List of post with successful response. """
        request = self.client.get(self.url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_detail_post_response_success(self):
        """ Detail of a post with successful response. """
        post = Post.objects.create(**self.data)
        
        request = self.client.get(self.url + str(post.id) + "/")
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_create_new_post_response_success(self):
        """ Create new post with successful response. """
        request = self.client.post(self.url, self.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    def test_create_new_post_response_error(self):
        """ Create new post without title field, and with error response. """
        request = self.client.post(self.url, self.data_error)
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_post_response_success(self):
        """ Create new post with successful response. """
        request = self.client.post(self.url, self.data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)

    