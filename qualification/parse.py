from collections import defaultdict
from unparse import write_output

class Contributor:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def __repr__(self):
        repr = f"Contributor '{self.name}' with {len(self.skills)} skill{'s' if (len(self.skills) != 1) else ''}:\n"
        for skill, level in self.skills.items():
            repr += f"\t{skill} with level {level}\n"
        return repr

class Project:
    def __init__(self, name, skills, days, score, bb):
        self.name = name #str
        self.skills = skills # dict {skill name: skill level}
        self.days = days # int
        self.score = score # int
        self.bb = bb # int

    def __repr__(self):
        repr = f"Project '{self.name}' with {len(self.skills)} role{'s' if len(self.skills) != 1 else ''}:\n" 
        for skill, level in self.skills.items():
            repr += f"\t{skill} with level {level} required\n"
        return repr

class Graph:
    def __init__(self, project, contributors):
        self.roles = project.skills.items()
        self.fulfilled = dict()
        self.can_learn = dict()

        for contributor in contributors:
            pass


def parse(filename):
    with open(filename) as input_file:
        line = input_file.readline().rstrip('\n').split(' ')
        contributor_amt = int(line[0])
        project_amt = int(line[1])

        projects = list()
        contributors = list()

        for _ in range(contributor_amt):
            line = input_file.readline().rstrip('\n').split(' ') # Anna 1
            contributor_name = line[0]
            skill_amt = int(line[1])
            skills = defaultdict(int)

            for _ in range(skill_amt):
                line = input_file.readline().rstrip('\n').split(' ') # C++ 2
                skills[line[0]] = int(line[1])

            contributors.append(Contributor(contributor_name, skills))

        for _ in range(project_amt):
            line = input_file.readline().rstrip('\n').split(' ') # Logging 5 10 5 1
            
            name = line[0]
            days = int(line[1])
            score = int(line[2])
            bb = int(line[3])
            roles_amt = int(line[4])

            skills = defaultdict(int)

            for _ in range(roles_amt):
                line = input_file.readline().rstrip('\n').split(' ') # C++ 2
                skills[line[0]] = int(line[1])

            projects.append(Project(name, skills, days, score, bb))

    return projects, contributors

def schedule(projects, contributors):
    schedule = dict()


if __name__ == "__main__":
    projects, contributors = parse("a_an_example.in.txt")
    s = schedule(projects, contributors)
    # for project, assignments in s.items():
    #     print(f"Project {project}: {', '.join(assignments.values())}")
    write_output(s)

