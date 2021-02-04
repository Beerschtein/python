subj = []
with open('f_file_6.txt', 'r') as f:
    for str in f:
        subject, lecture, practice, lab = str.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')
