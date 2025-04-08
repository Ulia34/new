def parse_questions(file_path: str) -> list[dict[str, list[str]]]:
    questions: list[dict] = []
    with open(file_path, "r", encoding="utf-8") as file:
        lines: list[str] = file.readlines()

    current_question = None
    for line in lines:
        line: str = line.strip()
        if line:  # Если строка не пустая
            if not current_question:
                # Начинается новый вопрос
                current_question: dict[str, list[str]] = {
                    "question": line,
                    "answers": [],
                }
            else:
                # Это вариант ответа
                current_question["answers"].append(line)
        else:
            # Пустая строка означает конец текущего вопроса
            if current_question:
                questions.append(current_question)
                current_question = None

    # Добавляем последний вопрос, если файл не заканчивается пустой строкой
    if current_question:
        questions.append(current_question)

    return questions
