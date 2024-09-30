
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary



class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department



class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language



class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


def test_teamlead_attributes():
    team_lead = TeamLead("Alice", 5000, "IT", "Python", 5)

    assert team_lead.name == "Alice"
    assert team_lead.salary == 5000
    assert team_lead.department == "IT"
    assert team_lead.programming_language == "Python"
    assert team_lead.team_size == 5

    print("Усі атрибути присутні")


if __name__ == "__main__":
    test_teamlead_attributes()
