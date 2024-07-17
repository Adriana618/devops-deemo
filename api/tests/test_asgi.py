from django.test import SimpleTestCase

class TestASGIApplication(SimpleTestCase):
    def test_asgi_application_import(self):
        try:
            from demo.asgi import application
            self.assertIsNotNone(application)
        except Exception as e:
            self.fail(f"ASGI application import failed: {e}")
