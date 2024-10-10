from collections import defaultdict


class ToDoList:
    """
    Class for a TODO list
    """

    def __init__(self):
        """
        creates an empty dict
        """
        self.tasks_dict = dict()  # using dict for faster access

    def add_task(self, task: str):
        """
        adds a tasks
        """
        if task not in self.tasks_dict:
            self.tasks_dict.update({task: {"status": "TODO"}})
        else:
            raise ValueError("Task already exists.")

    def remove_task(self, task: str):
        """
        removes a tasks
        """
        if task in self.tasks_dict:
            del self.tasks_dict[task]
        else:
            raise ValueError("Task does not exist.")

    def get_tasks(self):
        """
        returns all tasks
        """
        return [i for i in self.tasks_dict.items()]

    def complete_task(self, task: str):
        """
        marks a tasks complete
        """
        if task in self.tasks_dict:
            self.tasks_dict[task]["status"] = "Done"
        else:
            raise ValueError("Task does not exist.")
