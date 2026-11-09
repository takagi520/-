import json

from pkg.book_tools import (
    read_books,
    write_books,
    input_required,
    search_books,
    show_books,
    add_book,
    change_status,
    show_last_and_stats
)

try:
    books = read_books("books.json")

except FileNotFoundError:
    print("找不到 books.json，程式結束。")
    raise SystemExit

except json.JSONDecodeError:
    print("books.json 格式錯誤，程式結束。")
    raise SystemExit

except OSError as error:
    print(f"讀取檔案時發生錯誤：{error}")
    raise SystemExit

while True:
    print("""--- 簡易書籍管理系統 ---
1. 顯示全部書籍
2. 新增書籍
3. 查詢書籍
4. 變更借閱狀態
5. 顯示最後 3 筆書籍與統計
6. 匯出書籍資料
7. 離開系統
------------------------
""")

    choice = input("請選擇功能：").strip()

    if choice == "1":
        print("--- 全部書籍 ---")
        show_books(books)

    elif choice == "2":
        add_book(books)

    elif choice == "3":
        keyword = input_required("請輸入書名關鍵字：")

        result = search_books(books, keyword)

        if result:
            print("--- 查詢結果 ---")
            show_books(result)
        else:
            print("查無符合的書籍")

    elif choice == "4":
        change_status(books)

    elif choice == "5":
        show_last_and_stats(books)

    elif choice == "6":
        try:
            write_books(books, "output.json")

        except OSError as error:
            print(f"匯出失敗：{error}")

        else:
            print(
                f"已匯出 {len(books)} 筆書籍資料至 output.json。"
            )

    elif choice == "7":
        print("系統已退出")
        break

    else:
        print("輸入錯誤，請輸入 1～7。")