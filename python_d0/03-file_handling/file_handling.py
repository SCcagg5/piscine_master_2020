from typing import IO, Union, List

author = "courte_e"


def creator(filename: str) -> IO:
    try:
        f = open(filename, "x")
    except Exception:
        f = None
    if f is None:
        f = open(filename, "r")
        text = f.read()
        f.close()
        if len(text) > 0:
            raise ValueError
        f = open(filename, "w")
        f.write("old")
        f.close()
    return open(filename, "w")


def writer(opened: IO, data: Union[str, List[str]]) -> int:
    return opened.write(data if isinstance(data, str) else '\n'.join(data))


def closer(opened: IO) -> IO:
    try:
        opened = opened.close()
        f = True
    except Exception:
        f = False
    if not f:
        raise RuntimeError
    return opened


"""
opened = creator('sample.txt')
written = writer(opened, 'ton')
written2 = writer(opened, ['ton', 'test'])
closer(opened)
print(written)
print(written2)
"""