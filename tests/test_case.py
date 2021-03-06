import os
import subprocess
import unittest


class TestCase(unittest.TestCase):

    def tearDown(self):
        super(TestCase, self).tearDown()
        self.process = None

    def execute(self, file_path, user_input=None):
        self.process = subprocess.Popen(
            ["python", file_path],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )

        return self.process.communicate(user_input)[0]

    def file_get_contents(self, file_path):
        with open(file_path, 'r') as lines:
            return lines.read()

    def generateExpectedOutput(self, file, file_name):
        current_directory = os.path.dirname(os.path.realpath(file))
        case_path = os.path.join(current_directory, file_name)

        return self.file_get_contents(case_path)
