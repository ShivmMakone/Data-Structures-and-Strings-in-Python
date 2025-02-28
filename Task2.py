def lists():
    ori_list = list(range(1, 11))
    print(f"Original list: {ori_list}")

    ext_list = ori_list[:5]
    print(f"Extracted first five elements: {ext_list}")

    rev_list = ext_list[::-1]
    print(f"Reversed extracted elements: {rev_list}")

if __name__ == "__main__":
    lists()

