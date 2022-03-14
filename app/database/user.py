from app.database import get_db


# list:
# mylist = [1, 2, 3]
# mylist = list()


# tuple:
# mytuple = (1, 2, 3)
# mytuple = tuple()

# mytuplelement = (1,)

def output_formatter(results):
    out = []
    for result in results:
        res_dict = {}
        res_dict["id"] = result(0)
        res_dict["first_name"] = result[1]
        res_dict["last_name"] = result[2]
        res_dict["hobbies"] = result[3]
        res_dict["active"] = result[4]
        out.append(res_dict)
    return out


def insert(user_dict):
    value_tuple = (
        user_dict["first_name"],
        user_dict["last_name"],
        user_dict["hobbies"],
    )

    stmt = """
        INSERT INTO user (
            first_name,
            last_name,
            hobbies
        )   VALUES (?, ?, ?)
    """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple)
    cursor.commit()
    cursor.close()


def scan():
    cursor = get_db().execute(
        "SELECT * FROM user WHERE activate=1", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def select_by_id(pk):
    cursor = get_db()
    cursor.execute(
        "SELECT * FROM user WHERE id=?", (pk,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def deactive_user(pk):
    cursor = get_db()
    cursor.execute(
        "SELECT * FROM user WHERE id=?", (pk,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)
