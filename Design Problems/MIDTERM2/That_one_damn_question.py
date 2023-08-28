# That one exam question I can't do

emp_to_soft = {

    'mary': {'word', 'excel', 'wing101'},
    'sarah': {'solidworks', 'powerpoint'},
    'John': {'matlab', 'word', 'powerpoint'},
    'tom': {'wing101', 'solidworks'}

}

# Extract skills
software = list(emp_to_soft.values())
print(software)

# Make a set of all software
unique_software = set()
for skills in software:
    unique_software = unique_software.union(skills)
print(unique_software)

unique_software = list(unique_software)
print(unique_software)

soft_to_emps = {}
for skill in unique_software:
    soft_to_emps[skill] = set()
    for name in emp_to_soft:
        soft_to_emps[skill].add(name)
print(soft_to_emps)
