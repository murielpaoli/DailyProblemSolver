def study_schedule(permanence_period, target_time):
    # Verifica se target_time é vazio
    if not target_time:
        return None

    # Inicializa o contador de estudantes
    student_count = 0

    # Percorre cada período de permanência
    for start_time, end_time in permanence_period:

        # Verifica se o período é válido
        if isinstance(start_time, int) and isinstance(end_time, int):

            # Verifica se target_time está dentro do período
            if start_time <= target_time <= end_time:
                student_count += 1
        else:
            return None

    return student_count
