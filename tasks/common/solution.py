import datetime as dt



event_list = [
    {
        "dt": "2022-02-23 04:39:45.789123",
        "event": "start"
    },
    {
        "dt": "2022-02-23 04:41:19.123456",
        "event": "stop"
    },
    {
        "dt": "2022-02-23 04:45:02.345678",
        "event": "start"
    },
    {
        "dt": "2022-02-23 04:46:57.987654",
        "event": "stop"
    },
    {
        "dt": "2022-02-23 04:50:11.456789",
        "event": "start"
    },
    {
        "dt": "2022-02-23 04:51:34.876543",
        "event": "stop"
    },
    {
        "dt": "2024-02-23 04:55:28.567890",
        "event": "start"
    },
    {
        "dt": "2024-02-23 09:56:43.456789",
        "event": "stop"
    },
{
        "dt": "2024-06-30 05:02:11.987654",
        "event": "start"
    },
    {
        "dt": "2024-06-30 06:03:34.345678",
        "event": "stop"
    },
    {
        "dt": "2024-06-25 05:02:11.987654",
        "event": "start"
    },
    {
        "dt": "2024-06-25 06:03:34.345678",
        "event": "stop"
    }
]


def get_hours_between_events(data_list: list[dict],
                             start_date: str = None,
                             end_date: str = None) -> int:
    if start_date:
        start_date_dt = dt.datetime.strptime(start_date, '%Y-%m-%d')

    if end_date:
        end_date_dt = dt.datetime.strptime(end_date, '%Y-%m-%d')
    else:
        end_date_dt = start_date_dt

    seconds_counter = 0
    for i in range(0, len(data_list), 2):

        start_time_dt = dt.datetime.strptime(data_list[i]["dt"], '%Y-%m-%d %H:%M:%S.%f')
        end_time_dt = dt.datetime.strptime(data_list[i + 1]["dt"], '%Y-%m-%d %H:%M:%S.%f')

        # Проверяем, что start_time не может быть раньше даты начала
        # И  не может быть позже даты конца
        if start_date_dt.date() <= start_time_dt.date() <= end_date_dt.date():
            time_difference = end_time_dt - start_time_dt
            seconds_counter += time_difference.total_seconds()

    total_hours = seconds_counter / 3600
    return round(total_hours)


def get_hours_in_date_range(data_list: list[dict],
                            start_date: str,
                            end_date: str,) -> int:
    return get_hours_between_events(
        data_list=data_list,
        start_date=start_date,
        end_date=end_date
    )


def get_hours_today(data_list: list[dict]) -> int:
    current_date = str(dt.date.today())
    return get_hours_between_events(
        data_list=data_list,
        start_date=current_date
    )


def get_hours_this_week(data_list: list[dict] = None) -> int:
    current_date = dt.date.today()
    start_date = current_date
    while start_date.isoweekday() != 1:
        start_date = start_date - dt.timedelta(days=1)
    end_date = start_date + dt.timedelta(days=6)
    return get_hours_between_events(
        data_list=data_list,
        start_date=str(start_date),
        end_date=str(end_date)
    )


def get_last_day_of_month(date: dt.date) -> dt.date:
    next_month = date.replace(day=28) + dt.timedelta(days=4)
    last_day = next_month - dt.timedelta(days=next_month.day)
    return last_day


def get_hours_this_month(data_list: list[dict]) -> int:
    current_date = dt.date.today()
    first_day = current_date.replace(day=1)
    last_day = get_last_day_of_month(current_date)
    return get_hours_between_events(
        data_list=data_list,
        start_date=str(first_day),
        end_date=str(last_day)
    )


def get_hours_this_year(data_list: list[dict]) -> int:
    current_date = dt.date.today()
    first_day = dt.datetime(year=current_date.year, month=1, day=1)
    last_day = dt.datetime(year=current_date.year, month=12, day=31)

    return get_hours_between_events(
        data_list=data_list,
        start_date=str(first_day.date()),
        end_date=str(last_day.date())
    )


print(
    get_hours_this_year(
        data_list=event_list
    )
)

