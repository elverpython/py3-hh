from django.test import TestCase
from .models import Worker, Resume, Comment

class WorkerTestCase(TestCase):
    def test_create_worker_should_success(self):
        my_data = {
            "name": "Test 1",
            "specialization": "Test 2",
            "expected_salary": "test expected_salary 1",
            "is_searching": "test 3",

        }

        response = self.client.post('/workers/', my_data)
        self.assertEqual(response.status_code, 200)

        new_worker = Worker.objects.first()
        self.assertEqual(new_worker.name, my_data["name"])
        self.assertEqual(new_worker.specialization, my_data["specialization"])
        self.assertEqual(new_worker.expected_salary, int(my_data["expected_salary"]))
        self.assertEqual(new_worker.is_searching, my_data["is_searching"])

        worker_name = my_data["name"]
        response_homepage = self.client.get("/")
        self.assertContains(response_homepage, worker_name)


class ResumeTestCase(TestCase):
    def test_create_resume_should_success(self):
        my_data = {
            "title": "Test 1",
            "text": "100",
            "created_at": "test created_at 1",
            "profile_photo": "test profile_photo",

        }

        response = self.client.post('/add-resume/', my_data)
        self.assertEqual(response.status_code, 302)

        new_resume = Resume.objects.first()
        self.assertEqual(new_resume.title, my_data["title"])
        self.assertEqual(new_resume.text, my_data["text"])
        self.assertEqual(new_resume.created_at, my_data["created_at"])
        self.assertEqual(new_resume.profile_photo, my_data["profile_photo"])

        resume_title = my_data["title"]
        response_homepage = self.client.get("/")
        self.assertContains(response_homepage, resume_title)

class CommentTestCase(TestCase):
    def test_create_comment_should_success(self):
        my_data = {
            "text": "Test 1",
            "created_at": "test created_at 1",
        }

        response = self.client.post('/workers/', my_data)
        self.assertEqual(response.status_code, 200)

        new_comment = Comment.objects.first()
        self.assertEqual(new_comment.text, my_data["text"])
        self.assertEqual(new_resume.created_at, my_data["created_at"])

        comment_text = my_data["text"]
        response_homepage = self.client.get("/")
        self.assertContains(response_homepage, comment_text)
