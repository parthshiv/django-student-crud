from django.test import TestCase
from enroll.models import Student

class StudentTestCase(TestCase):
    
    # this function will auto call all the time we run the test
    def setUp(self):
        # Create a sample student for update, delete, and get tests
        self.student = Student.objects.create(
            name='John Doe',
            email='john@example.com',
            password='password123'
        )

    def test_add_student(self):
        # Simulate adding a new student
        new_student = Student.objects.create(
            name='Jane Smith',
            email='jane@example.com',
            password='mypassword'
        )

        # Fetch the student from the database
        added_student = Student.objects.get(id=new_student.id)

        # Assertions
        self.assertEqual(added_student.name, 'Jane Smith')
        self.assertEqual(added_student.email, 'jane@example.com')
        self.assertEqual(added_student.password, 'mypassword')

    def test_update_student(self):
        # Simulate updating the existing student
        self.student.name = 'John Updated'
        self.student.email = 'johnupdated@example.com'
        self.student.password = 'newpassword123'
        self.student.save()  # Save changes to the database

        # Fetch the student from the database again
        updated_student = Student.objects.get(id=self.student.id)

        # Assertions
        self.assertEqual(updated_student.name, 'John Updated')
        self.assertEqual(updated_student.email, 'johnupdated@example.com')
        self.assertEqual(updated_student.password, 'newpassword123')

    def test_delete_student(self):
        # Delete the student
        student_id = self.student.id
        self.student.delete()

        # Check that the student no longer exists
        with self.assertRaises(Student.DoesNotExist):
            Student.objects.get(id=student_id)

    def test_get_student(self):
        # Retrieve the student
        fetched_student = Student.objects.get(id=self.student.id)

        # Assertions
        self.assertEqual(fetched_student.name, 'John Doe')
        self.assertEqual(fetched_student.email, 'john@example.com')
        self.assertEqual(fetched_student.password, 'password123')
