
def get_variant(task_number, data):
    answer = data[task_number][1]
    answer = answer[answer.index(" ") + 1:]
    return data[task_number][0], answer


def check_answer(message, answer):
    return message.lower() in answer.split('|')
        