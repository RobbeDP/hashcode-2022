def write_output(schedule, output_file="output.txt"):
  with open(output_file, 'w') as f:
    f.write(str(len(schedule)))
    f.write("\n")
    for project in schedule:
      f.write(project)
      f.write("\n")
      f.write(" ".join(schedule[project]))
