from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        res_dict = {
            "id": result[0],
            "color": result[1],
            "license_plate": result[2],
            "vehicle_type": result[3],
            "user_id": result[4],
            "active": result[5]
        }
        out.append(res_dict)
    return out


def select_by_user_id(uid):
    cursor = get.db().execute(
        "SELECT * FROM vehicle WHERE user_id=?", (uid, ))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)
