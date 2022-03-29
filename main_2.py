nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flatlist_generator(nested):
    for sub in nested:
        if isinstance(sub, list):
            yield from flatlist_generator(sub)
        else:
            yield sub


if __name__ == '__main__':
    for item in flatlist_generator(nested_list):
        print(item)

    flat_list = [item for item in flatlist_generator(nested_list)]
    print('\n', flat_list)