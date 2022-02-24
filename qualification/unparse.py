def write_output(schedule, output_file="output.txt"):
  with open(output_file, 'a+') as f:
    f.write(len(schedule))
    for project in schedule:
      f.write(project)
      f.write(" ".join(schedule[project]))