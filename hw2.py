import Techniovision


def keywithmaxval(d):
    v = list(d.values())
    j = list(d.keys())
    return j[v.index(max(v))]


def inside_contest(faculty, file_name):
    file = open(file_name, 'r')
    inside_dict = {}
    faculty_dict = {}
    # start reading the file
    compare_strings = ['inside', 'techniovision', 'staff']

    for line in file:
        clean_line = line.split()
        if line.split(' ', 1)[0] == compare_strings[0]:
            if not clean_line[2] in inside_dict:
                inside_dict[clean_line[2]] = clean_line[3]

        if line.split(' ', 1)[0] == compare_strings[2]:
            if clean_line[-1] == faculty:
                for e in clean_line[2::]:  # cut the identifier
                    faculty_dict[e] = 0
                faculty_dict[clean_line[2]] += 20  # add judge score
    file.close()
    return keywithmaxval(faculty_dict)


input_name = 'input.txt'
f = open(input_name, 'r')
faculty_dict_results = {}

comp_strings = ['inside', 'techniovision', 'staff']
for line_in_f in f:
    processed_line = line_in_f.split()
    if line_in_f.split(' ', 1)[0] == comp_strings[2]:
        faculty_dict_results[inside_contest(processed_line[-1], input_name)] = processed_line[-1]  # Name mapper
f.close()

tech_ptr = Techniovision.TechniovisionCreate()
f = open(input_name, 'r')

for line_in_f in f:
    processed_line = line_in_f.split()
    if line_in_f.split(' ', 1)[0] == comp_strings[1]:
        if processed_line[2] in faculty_dict_results:
            Techniovision.TechniovisionStudentVotes(tech_ptr, int(processed_line[1]), str(processed_line[3]),
                                                    str(faculty_dict_results[processed_line[2]]))

f.close()
Techniovision.TechniovisionWinningFaculty(tech_ptr)
Techniovision.TechniovisionDestroy(tech_ptr)
