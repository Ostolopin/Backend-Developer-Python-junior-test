def strict(func):
    def wrapper(*args):
        # �������� ��������� ����� � ����� ����������
        annotations = func.__annotations__
        param_names = func.__code__.co_varnames
        
        # ��������� ������ ���������� ��������
        for i, (arg, name) in enumerate(zip(args, param_names)):
            if name in annotations:  # ���� ���� ��������� ����
                expected_type = annotations[name]
                if not isinstance(arg, expected_type):  # ���������� ���
                    raise TypeError(
                        f"Argument '{name}' at position {i} must be {expected_type.__name__}, "
                        f"but got {type(arg).__name__}."
                    )
        # �������� ������������ �������, ���� ��� �������� ������
        return func(*args)
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

# �����
print(sum_two(1, 2))       # >>> 3
print(sum_two(1, 2.4))     # >>> TypeError
