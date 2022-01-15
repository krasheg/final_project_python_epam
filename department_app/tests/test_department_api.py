from test_base import BaseTestCase
import http
import unittest
import json
from department_app.models.department import Department
from mockup_data import department_1, department_2, department_3


class TestDepartmentApi(BaseTestCase):
    """
    class for testing department api
    """

    def test_get_departments(self):
        """
        get all departments from db in json
        :return:
        """
        client = self.app.test_client()
        dep_1 = department_1
        dep_2 = department_2
        dep_1.save_to_db()
        dep_2.save_to_db()
        response = client.get('/api/departments')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertEqual(response.json, [department_1.json(), department_2.json()])

    def test_post_department(self):
        """
        test for post new department
        """
        client = self.app.test_client()
        new_data = {
            'name': 'New Name',
            'organisation': 'New Organisation'
        }
        response = client.post('/api/departments', data=json.dumps(new_data), content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        self.assertEqual(response.json, {'message': 'Department has been successfully added'})

        #: Call {'message': 'Empty request'}, 400
        new_data = None
        response = client.post('/api/departments', data=json.dumps(new_data), content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.json, {'message': 'Empty request'})

        #: Call Bad request, 400

        new_data = {"name": "New"}
        response = client.post('/api/departments', data=json.dumps(new_data), content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.json, {'message': 'Bad request'})

    def test_get_department_by_id(self):
        """
        test for get_department_by_id
        """
        department = department_3
        department.save_to_db()
        client = self.app.test_client()
        response = client.get("/api/departments/1")
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertEqual(response.json, department_3.json())

    def test_put_department(self):
        """
        test for replace department with new data
        """
        department = Department("Old name", "Old organisation")
        new_data = {"name": "New"}
        department.save_to_db()
        client = self.app.test_client()
        response = client.put("/api/departments/1", data=json.dumps(new_data), content_type='application/json')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        department.name = "New"
        self.assertEqual(response.json, {'message': 'Department has been successfully updated'})

    def test_delete_department(self):
        """
        test for deleting department
        """
        department = Department("dep", "To delete")
        department.save_to_db()
        client = self.app.test_client()
        response = client.delete("/api/departments/1")
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
        self.assertEqual(response.json, {"message": "Department has been deleted"})

        #: Call error
        response = client.delete("/api/departments/3")
        self.assertEqual(response.status_code, http.HTTPStatus.NOT_FOUND)
        self.assertEqual(response.json, {'message': 'Cannot delete department'})


if __name__ == '__main__':
    unittest.main()
