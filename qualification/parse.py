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


class ProjectGraph:
    def __init__(self, project, contributors):
        self.name = project.name
        self.days = project.days
        self.required_roles = dict() # project.skills.items()
        self.assignment = set()
        for name, level in project.skills.items():
            self.required_roles[name] = {'fulfilled': set(), 'mentor': set(), 'learn': set()}
            for contributor in contributors:
                if contributor.skills[name] > level:
                    self.required_roles[name]['fulfilled'].add(contributor.name)
                elif contributor.skills[name] == level-1:
                    self.required_roles[name]['mentor'].add(contributor.name)
                elif contributor.skills[name] == level:
                    self.required_roles[name]['learn'].add(contributor.name)

    def assign(self, contributor):
        self.assignment.add(contributor.name)

    def num_edges(self, key):
        return sum([len(requirement[key]) for requirement in self.required_roles.values()])

    def update(self, learned): # learned: [(contributor, role)]
        for contributor, role in learned:
            if contributor in self.required_roles[role]['mentor']:
                self.required_roles[role]['mentor'].remove(contributor)
                self.required_roles[role]['learn'].add(contributor)
            elif contributor in self.required_roles[role]['learn']:
                self.required_roles[role]['learn'].remove(contributor)
                self.required_roles[role]['fulfilled'].add(contributor)

    def schedule(self):
        learned = set()
        for role, edges in self.required_roles.items():
            learn_non_ass = list(edges['learn'] - self.assignment)
            if len(learn_non_ass) > 0:
                self.assign(learn_non_ass[0])
                learned.add((learn_non_ass[0], role))
                continue
            fulfilled_non_ass = list(edges['fulfilled'] - self.assignment)
            if len(fulfilled_non_ass) > 0:
                self.assign(fulfilled_non_ass[0])
            else:
                return False
        return self.assignment, learned

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
    graphs = [ProjectGraph(project, contributors) for project in projects]
    graphs.sort(key=lambda x: (x.num_edges('learn'), x.num_edges('mentor'), x.days), reverse=True)
    prev_length = len(graphs) + 1
    while len(graphs) > 0 and prev_length > len(graphs):
        scheduled = list()
        for graph in graphs:
            scheduling = graph.schedule()
            if not scheduling:
                continue
            scheduled.append(graph.name)
            
            for graph in graphs:
                if graph.name not in scheduled:
                    graph.update(learned)
                
        


if __name__ == "__main__":
    projects, contributors = parse("a_an_example.in.txt")
    s = schedule(projects, contributors)
    # for project, assignments in s.items():
    #     print(f"Project {project}: {', '.join(assignments.values())}")
    # write_output(s)

