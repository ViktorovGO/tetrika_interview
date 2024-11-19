def appearance(intervals: dict[str, list[int]]) -> int:
    def merge_intervals(intervals):
        """Объединяет пересекающиеся интервалы."""
        sorted_intervals = sorted(intervals)
        merged = []
        for start, end in sorted_intervals:
            if merged and start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged

    def calculate_intersection(intervals1, intervals2):
        """Вычисляет общее время пересечения двух списков интервалов."""
        total_time = 0
        i, j = 0, 0
        while i < len(intervals1) and j < len(intervals2):
            start1, end1 = intervals1[i]
            start2, end2 = intervals2[j]

            # Пересечение интервалов
            start = max(start1, start2)
            end = min(end1, end2)

            if start < end:
                total_time += end - start

            # Двигаем указатели
            if end1 < end2:
                i += 1
            else:
                j += 1

        return total_time

    lesson_start, lesson_end = intervals["lesson"]
    pupil_intervals = [
        [max(intervals["pupil"][i], lesson_start), min(intervals["pupil"][i + 1], lesson_end)]
        for i in range(0, len(intervals["pupil"]), 2)
        if intervals["pupil"][i + 1] > lesson_start and intervals["pupil"][i] < lesson_end
    ]
    tutor_intervals = [
        [max(intervals["tutor"][i], lesson_start), min(intervals["tutor"][i + 1], lesson_end)]
        for i in range(0, len(intervals["tutor"]), 2)
        if intervals["tutor"][i + 1] > lesson_start and intervals["tutor"][i] < lesson_end
    ]

    merged_pupil_intervals = merge_intervals(pupil_intervals)
    merged_tutor_intervals = merge_intervals(tutor_intervals)

    return calculate_intersection(merged_pupil_intervals, merged_tutor_intervals)

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
                   'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                   'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117},
    {'intervals': {'lesson': [1594702800, 1594706400],
                   'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                             1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                             1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                             1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                   'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577},
    {'intervals': {'lesson': [1594692000, 1594695600],
                   'pupil': [1594692033, 1594696347],
                   'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565},
]

for i, test in enumerate(tests):
    test_answer = appearance(test['intervals'])
    assert test_answer == test['answer'], f"Error on test case {i}, got {test_answer}, expected {test['answer']}"