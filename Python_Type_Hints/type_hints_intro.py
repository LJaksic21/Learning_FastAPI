def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def process_items(items: list[str]):
    for item in items:
        print(item)


def process_items2(items_t: tuple[int, int, str], item_s: set[bytes]):
    return items_t, item_s


def process_items3(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


print(get_full_name("john", "smith"))
print(process_items(["a", "b", "c"]))
print(process_items2((1, 2, "John Smith"), {b"1", b"2", b"3"}))
print(process_items3({"apple": 0.5, "orange": 0.25, "banana": 0.75}))
