def parse(filename):
    with open(filename) as input_file:
        line = input_file.readline().rstrip('\n').split(' ')
        contributor_amt = int(line[0])
        project_amt = int(line[1])

        for i in range(contributor_amt):
            line = input_file.readline().rstrip('\n').split(' ')
            contributor_name = line[0]
            skill_amt = int(line[0])

            for j in range(skill_amt):
                line = input_file.readline().rstrip('\n').split(' ')
                skill_name = line[0]
                skill_level = int(line[1])
