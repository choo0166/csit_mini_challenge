from datetime import datetime 
from werkzeug.exceptions import BadRequest

def format_date(date: str):
    """
    Converts date string as datetime object
    compatible with mongo's ISODate format.

    :param str date: Date in yyyy-mm-dd format
    :return: datetime object
    :raises BadRequest: When input date does not match yyyy-mm-dd format
    """
    fmt = "%Y-%m-%d"
    try:
        dt = datetime.strptime(date, fmt)
        return dt
    except:
        raise BadRequest("Improper input date format.")
