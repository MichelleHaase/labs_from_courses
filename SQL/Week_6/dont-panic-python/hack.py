from cs50 import SQL


def main() -> None:
    db = SQL("sqlite:///dont-panic.db")
    password = input("password? ").strip()
    db.execute(
        """ UPDATE "users" SET "password" = ?
            WHERE "username" = "admin"; """,
        password,
    )
    print("Hacked!")


if __name__ == "__main__":
    main()
