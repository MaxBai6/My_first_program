# coding=utf-8

import pandas as pd

class Security(object):
    code = None
    display_name = None
    name = None
    start_date = None
    end_date = None
    type = None
    parent = None

    def __init__(self, **kwargs):
        self.code = kwargs.get("code", None)
        self.display_name = kwargs.get("display_name", None)
        self.name = kwargs.get("name", None)
        self.start_date = to_date(kwargs.get("start_date", None))
        self.end_date = to_date(kwargs.get("end_date", None))
        self.type = kwargs.get("type", None)
        self.parent = kwargs.get("parent", None)

    def __repr__(self):
        return self.code

    def __str__(self):
        return self.code


def no_sa_warnings(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        import warnings
        from sqlalchemy import exc as sa_exc
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=sa_exc.SAWarning)
            return f(*args, **kwds)
    return wrapper


def get_tables_from_sql(sql):
    """ 从 sql 语句中拿到所有引用的表名字 """
    m = re.search(r'FROM (.*?)($| WHERE| GROUP| HAVING| ORDER)', sql, flags=re.M)
    return [t.strip() for t in m.group(1).strip().split(',')] if m else []


@no_sa_warnings
def check_no_join(query):
    """ 确保 query 中没有 join 语句, 也就是说: 没有引用多个表 """
    tables = get_tables_from_sql(str(query.statement))
    if len(tables) != 1:
        raise Exception("only a table is allowed to query every time")





class ParamsError(Exception):
    pass


def today():
    return datetime.date.today()






def is_list(l):
    return isinstance(l, (list, tuple))


def to_date(date):
    """
    >>> convert_date('2015-1-1')
    datetime.date(2015, 1, 1)

    >>> convert_date('2015-01-01 00:00:00')
    datetime.date(2015, 1, 1)

    >>> convert_date(datetime.datetime(2015, 1, 1))
    datetime.date(2015, 1, 1)

    >>> convert_date(datetime.date(2015, 1, 1))
    datetime.date(2015, 1, 1)
    """
    if is_str(date):
        if ':' in date:
            date = date[:10]
        return datetime.datetime.strptime(date, '%Y-%m-%d').date()
    elif isinstance(date, datetime.datetime):
        return date.date()
    elif isinstance(date, datetime.date):
        return date
    elif date is None:
        return None
    raise ParamsError("type error")


def _get_session():
    from sqlalchemy.orm import scoped_session, sessionmaker
    session = scoped_session(sessionmaker())
    return session


session = _get_session()



