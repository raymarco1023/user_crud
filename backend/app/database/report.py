from app.database import get_db


def get_users_and_vehicles_join():
    stmt = """
       SELECT user.last_name, 
       user.first_name, 
       user.hobbies,
       user.active,
       vehicle.license_plate,
       vehicle.color,
       vehicle_type.description
       FROM user 
       INNER JOIN vehicle ON user.id = vehicle.user_id
       INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id
    """
    cursor = get_db().execute(stmt())
    results = cursor.fetchall()
    cursor.close()
    out = []
    for result in results:
        res_dict = {}
        rest_dict = {
            "user_first_name": result[0],
            "user_last_name": result[1],
            "user_hobbies": result[2],
            "user_active": result[3],
            "vehicle_license_plate": result[4],
            "vehicle_color": result[5],
            "vehicle_type": result[6],
        }
        out.append(res_dict)
    return out
