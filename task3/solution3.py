def appearance(intervals: dict) -> int:
    # ���������� ���������� �����, ������� � ���������� �� �������� �������
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']

    # �������������� ��������� ����� � ������ ��������
    lesson_interval = [(lesson[0], lesson[1])]

    # ������� ��� �������������� ������ ������ � ���������
    def get_intervals(times):
        return [(times[i], times[i+1]) for i in range(0, len(times), 2)]

    # ����������� ������� ������� � ���������� � ���������
    pupil_intervals = get_intervals(pupil)
    tutor_intervals = get_intervals(tutor)

    # ������� ��� ������� ���������� � �������� ��������� �����
    def clip_intervals(intervals, lesson_interval):
        clipped = []
        for start, end in intervals:
            # �������� �������� �� �������� �����
            start_clipped = max(start, lesson_interval[0][0])
            end_clipped = min(end, lesson_interval[0][1])
            if start_clipped < end_clipped:
                clipped.append((start_clipped, end_clipped))
        return clipped

    # �������� ��������� ������� � ���������� �� ������ �����
    pupil_intervals = clip_intervals(pupil_intervals, lesson_interval)
    tutor_intervals = clip_intervals(tutor_intervals, lesson_interval)

    # ������� ��� ����������� �������������� ����������
    def merge_intervals(intervals):
        if not intervals:
            return []
        # ��������� ���������
        intervals.sort()
        merged = [intervals[0]]
        for current in intervals[1:]:
            prev_start, prev_end = merged[-1]
            curr_start, curr_end = current
            if curr_start <= prev_end:
                # ���� ��������� ������������, ���������� ��
                merged[-1] = (prev_start, max(prev_end, curr_end))
            else:
                merged.append(current)
        return merged

    # ���������� ��������� ��� ������� � ����������
    pupil_intervals = merge_intervals(pupil_intervals)
    tutor_intervals = merge_intervals(tutor_intervals)

    # ����� ����������� ���������� ������� � ����������
    total_overlap = 0
    i, j = 0, 0
    while i < len(pupil_intervals) and j < len(tutor_intervals):
        start_pupil, end_pupil = pupil_intervals[i]
        start_tutor, end_tutor = tutor_intervals[j]

        # ������� ����������� ������� ����������
        start_overlap = max(start_pupil, start_tutor)
        end_overlap = min(end_pupil, end_tutor)

        if start_overlap < end_overlap:
            # ���� ���� �����������, ��������� ��� ����� � ������ ����������
            total_overlap += end_overlap - start_overlap

        # ��������� � ���������� ���������
        if end_pupil <= end_tutor:
            i += 1
        else:
            j += 1

    # ���������� ����� ����� �����������
    return total_overlap

