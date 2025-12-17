# tests_runner.py
import xmlrunner
from django.test.runner import DiscoverRunner

class XMLTestRunner(DiscoverRunner):
    def run_suite(self, suite, **kwargs):
        return xmlrunner.XMLTestRunner(output='reports').run(suite)
