from django.test import SimpleTestCase

class TestWSGIApplication(SimpleTestCase):
    def test_wsgi_application_import(self):
        try:
            from demo.wsgi import application
            self.assertIsNotNone(application)
        except Exception as e:
            self.fail(f"WSGI application import failed: {e}")
