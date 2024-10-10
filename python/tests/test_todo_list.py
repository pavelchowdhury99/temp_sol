import unittest
from todo_list import ToDoList


class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.todo_list_obj = ToDoList()

    def test_add_task(self):
        self.todo_list_obj.add_task("Task 1")
        self.assertIn("Task 1", self.todo_list_obj.tasks_dict)

    def test_add_existing_task(self):
        self.todo_list_obj.add_task("Task 1")
        with self.assertRaises(ValueError):
            self.todo_list_obj.add_task("Task 1")

    def test_remove_task(self):
        self.todo_list_obj.add_task("Task 1")
        self.todo_list_obj.remove_task("Task 1")
        self.assertNotIn("Task 1", self.todo_list_obj.tasks_dict)

    def test_remove_nonexistent_task(self):
        with self.assertRaises(ValueError):
            self.todo_list_obj.remove_task("Task 1")

    def test_complete_task(self):
        self.todo_list_obj.add_task("Task 1")
        self.todo_list_obj.complete_task("Task 1")
        self.assertTrue(self.todo_list_obj.tasks_dict["Task 1"])

    def test_complete_nonexistent_task(self):
        with self.assertRaises(ValueError):
            self.todo_list_obj.complete_task("Task 1")

    def test_get_tasks_dict(self):
        self.todo_list_obj.add_task("Task 1")
        self.todo_list_obj.add_task("Task 2")
        self.todo_list_obj.complete_task("Task 1")
        tasks_dict = self.todo_list_obj.get_tasks()
        self.assertEqual(len(tasks_dict), 2)
        print(tasks_dict)
        self.assertEqual(tasks_dict[0][0], "Task 1")
        self.assertEqual(tasks_dict[0][1]['status'], "Done")
        self.assertEqual(tasks_dict[1][0], "Task 2")
        self.assertEqual(tasks_dict[1][1]['status'], "TODO")

if __name__ == '__main__':
    unittest.main()