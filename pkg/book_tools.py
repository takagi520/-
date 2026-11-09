import json

def read_books(file_name: str) -> list:
    """讀取 JSON 書籍資料並回傳。"""
    with open(file_name, "r", encoding="utf-8") as file:
        books = json.load(file)

    return books


def write_books(books: list, file_name: str) -> None:
    """將書籍資料寫入 JSON 檔案。"""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(
            books,
            file,
            ensure_ascii=False,
            indent=4
        )

def search_books(books: list, keyword: str) -> list:
    """依書名關鍵字查詢書籍並回傳結果。"""
    result = [
        book
        for book in books
        if keyword.lower() in book["title"].lower()
    ]

    return result   


def show_books(books: list) -> None:
    """顯示書籍資料。"""
    if not books:
        print("目前沒有書籍資料")
        return

    print(
        f"{'編號':<6}"
        f"{'書籍編號':<12}"
        f"{'書名':<24}"
        f"{'作者':<16}"
        f"{'價格':>10}  狀態"
    )

    for index, book in enumerate(books, 1):
        status = "已借出" if book["borrowed"] else "可借閱"

        print(
            f"{index:<6}"
            f"{book['id']:<12}"
            f"{book['title']:<24}"
            f"{book['author']:<16}"
            f"{book['price']:>10,}  "
            f"{status}"
        )

def input_required(prompt: str) -> str:
    """取得不可為空的文字輸入。

    Args:
        prompt: 輸入提示文字。

    Returns:
        str: 使用者輸入的文字。
    """
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("欄位不可為空")

def add_book(books: list) -> None:
    """新增一本書籍。

    Args:
        books: 目前的書籍資料。
    """
    while True:
        book_id = input_required("請輸入書籍編號：")

        exists = False

        for book in books:
            if book["id"] == book_id:
                exists = True
                break

        if exists:
            print("書籍編號已存在，請重新輸入。")
        else:
            break

    title = input_required("請輸入書名：")
    author = input_required("請輸入作者：")

    while True:
        try:
            price = int(input("請輸入價格：").strip())

        except ValueError:
            print("價格須為大於 0 的整數，請重新輸入。")
            continue

        if price <= 0:
            print("價格須為大於 0 的整數，請重新輸入。")
            continue

        break

    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "price": price,
        "borrowed": False
    }

    books.append(new_book)

    print("新增成功。")

def change_status(books: list) -> None:
    """切換指定書籍的借閱狀態。

    Args:
        books: 目前的書籍資料。
    """
    book_id = input("請輸入書籍編號：").strip()

    for book in books:
        if book["id"] == book_id:
            book["borrowed"] = not book["borrowed"]

            status = "已借出" if book["borrowed"] else "可借閱"

            print(
                f"「{book['title']}」的狀態已變更為：{status}"
            )

            return

    print("查無此書籍編號")

def show_last_and_stats(books: list) -> None:
    """顯示最後三筆書籍及所有書籍統計。

    Args:
        books: 目前的書籍資料。
    """
    if not books:
        print("目前沒有書籍資料")
        return

    print("--- 最後 3 筆書籍 ---")

    show_books(books[-3:])

    available_count = 0
    borrowed_count = 0
    total_price = 0

    for book in books:
        if book["borrowed"]:
            borrowed_count += 1
        else:
            available_count += 1

        total_price += book["price"]

    total = len(books)
    average_price = total_price / total

    print("--- 書籍統計 ---")
    print(f"書籍總數：{total}")
    print(f"可借閱：{available_count}")
    print(f"已借出：{borrowed_count}")
    print(f"價格合計：{total_price:,} 元")
    print(f"平均價格：{average_price:.2f} 元")


