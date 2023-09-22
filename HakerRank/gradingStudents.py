def gradingStudents(grades):

    x = 0
    lista_nova = []

    for i, nota in enumerate(grades):
        x = nota
        while (x % 5) != 0:
            x += 1
        if grades[i] < 38 or (x - grades[i]) > 2:
            lista_nova.append(grades[i])
        else:
            lista_nova.append(x)
    return lista_nova


print(gradingStudents([93, 38, 38, 99]))
