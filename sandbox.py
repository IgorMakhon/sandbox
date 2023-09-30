import sys
from _datetime import datetime
import colorama

# initial_logs = """
# 2022-02-03 00:01:13.623 [http-nio-*8625*-exec-*7*] ERROR *i.k.i.repository.FunctionsRepository* - Sql exception for geometry {"type":"GeometryCollection","geometries":[{"type":"Polygon","coordinates":[[[*69*.*9*,*-18.03*],[*69*.*90147203*,*-18.029963864*],[*69*.*902940514*,*-18.029855542*],[*69*.*90870854*,*-18.02870821*],[*69*.*912826653*,*-18.027119679*],,[*69*.*920146769*,*-18.022228534*], Where: SQL function "calculate_validated_input" statement 1
# SQL function "calculate_population_and_gdp" statement 1
# 	at io.zxv.rpeapi.repository.PopulationRepository.getPopulationAndGdp(PopulationRepository.java:67) ~[classes!/:0.0.1-SNAPSHOT]
# 	at io.zxv.rpeapi.repository.PopulationRepository$$FastClassBySpringCGLIB$$924c19cd.invoke(<generated>) ~[classes!/:0.0.1-SNAPSHOT][*69*.*921213203*,*-18.021213203*],,[*69*.*924944088*,*-18.016667107*],[*69*.*925731858*,*-18.015423082*]ERROR: canceling statement due to user request; nested exception is org.postgresql.util.PSQLException: ERROR: canceling statement due to user request
# 2022-03-04 00:06:13.838 [http-nio-8625-exec-5] ERRORi.k.i.repository.FunctionsRepository - Sql exception for geometry {"type":"GeometryCollection","geometries":[{"type":"Polygon","coordinates":[[[127.169737423,10.375975952],[127.107035489,10.343227271], Where: SQL function "calculate_validated_input" statement 1
# SQL function "calculate_population_and_gdp" statement 1
# 	at io.zxv.rpeapi.repository.PopulationRepository.getPopulationAndGdp(PopulationRepository.java:67) ~[classes!/:0.0.1-SNAPSHOT]
# 	at io.zxv.rpeapi.repository.PopulationRepository$$FastClassBySpringCGLIB$$924c19cd.invoke(<generated>) ~[classes!/:0.0.1-SNAPSHOT][127.090680778,10.336408073[127.074093751,10.33015369],[127.023142134,10.314852137],[126.970841345,10.304865966],[126.917764405,10.300304586],[126.9,10.3],[126.882235595,10.300304586],[126.864492834,10.301217975],[126.846793332,10.302739052],[126.829158655,10.304865966],[126.811610286,10.307596123[125.689185268,10.579053728],[124.712383426,10.858838449],[123.98071637tage from stat_area st]; ERROR: canceling statement due to user request; nested exception is org.postgresql.util.PSQLException: ERROR: canceling statement due to user requestat org.springframework.jdbc.core.JdbcTemplate.execute(JdbcTemplate.java:651) ~[spring-jdbc-5.3.10.jar!/:5.3.10]at org.springframework.jdbc.core.JdbcTemplate.execute(JdbcTemplate.java:651) ~[spring-jdbc-5.3.10.jar!/:5.3.10]
# 	... 103 common frames omitted
# 	... 103 common frames omitted
# 2024-12-12 00:11:14.384 [http-nio-8625-exec-3] ERROR i.k.i.repository.FunctionsRepository - Sql exception for geometry {"type":"GeometryCollection","geometries":[{"type":"Polygon","coordinates":[[[137.023916564,14.815552392],[134.190691128,15.239091832],[134.151694677,15.21660222],[134.111904237,15.195432561],[134.071368286,15.175608648],[134.030136211,15.157154632],[133.988258246,15.140092998],[133.945785414,15.124444531],[1at org.springframework.jdbc.core.JdbcTemplate.execute(JdbcTemplate.java:651) ~[spring-jdbc-5.3.10.jar!/:5.3.10]
# 	... 103 common frames omitted"""


initial_logs = '''
2022-02-03 00:01:13.623 Error GREEENFUCKINGDAY at io.zxv.rpeapi.repository.PopulationRepository$$FastClassBySpringCGLIB$$924c19cd.invoke(<generated>) ~[classes!/:0.0.1-SNAPSHOT - ][127.090680778,10.336408073[127.074093751,10.33015369],[127.023142134,10.314852137],[126.970841345,10.304865966],[126.917764405,10.300304586],[126.9,10.3],[126.882235595,10.300304586],[126.864492834,10.301217975],[126.846793332,10.302739052],[126.829158655,10.304865966],[126.811610286,10.307596123[125.689185268,10.579053728],[124.712383426,10.858838449],[123.98071637tage from stat_area st]; ERROR: canceling statement due to user request; nested exception is org.postgresql.util.PSQLException: ERROR: canceling statement due to user requestat org.springframework.jdbc.core.JdbcTemplate.execute(JdbcTemplate.java:651)
... 103 common frames omitted
... 103 common frames omitted
2023-03-04 00:06:13.838 [http-nio-8625-exec-5] !!newyorkbabY!!! ERRORi.k.i.repository.FunctionsRepository - Sql exception for geometry {"type":"GeometryCollection"
2024-12-12 00:11:14.384 [http-nio-8625-exec-3] LONDON is_the_capital! Warn i.k.i.repository.FunctionsRepository - Sql exception for geometry {"type":"GeometryCollection","geometries":[{"type":"Polygon","coordinates":[[[137.023916564,14.815552392],[134.190691128,15.239091832],[134.151694677,15.21660222],[134.111904237,15.195432561],[134.071368286,15.175608648],[134.030136211,15.157154632],[133.988258246,15.140092998],[133.945785414,15.124444531],[1at org.springframework.jdbc.core.JdbcTemplate.execute(JdbcTemplate.java:651) ~[spring-jdbc-5.3.10.jar!/:5.3.10]
... 103 common frames omitted"""
'''

log_dict = {}
lines = initial_logs.strip().split('\n')
# Counter of logs in the file/s
count_logs = 0
for line in lines:
    # The '2' parameter passed to the split() function indicates that the splitting should happen only two times.
    parts = line.split(' ', 2)
    # The parts list contains three elements: the date, the time, and the rest of the line after the timestamp.
    timestamp = ' '.join(parts[:2]).strip()
    # The size of the timestamp is always 23 chars and the 10 element is 'whitespace'
    if len(timestamp) != 23:
        continue
    # Convert timestamp to datetime object
    timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
    print(timestamp)
    log_dict[timestamp] = parts[2]
    count_logs += 1
    # string_dict = str(log_dict)
    # print(string_dict[:100])
print("===========================================================================")
print(str(log_dict))
print("Count_logs", count_logs)


# log_dict = {
#     datetime(2023, 9, 30, 10, 0): "Error: Something went wrong",
#     datetime(2023, 9, 30, 11, 0): "Info: Task completed successfully",
#     datetime(2023, 9, 30, 12, 0): "Warning: Disk space low",
# }
#

def datetime_converter_searcher(log_dictionary, datetime_to_search=None):
    if datetime_to_search is None:
        return None
    elif datetime_to_search[:3] == '../' and len(datetime_to_search) == 26:
        search_to = datetime.strptime(datetime_to_search[3:], "%Y-%m-%d %H:%M:%S.%f")
        # Initialize an empty dictionary to store the filtered results
        search_results = {}
        for log_datetime, log_text in log_dictionary.items():
            if log_datetime <= search_to:
                search_results[log_datetime] = log_text
        return search_results or None
    elif datetime_to_search[-3:] == '/..' and len(datetime_to_search) == 26:
        search_from = datetime.strptime(datetime_to_search[:-3], "%Y-%m-%d %H:%M:%S.%f")
        # Initialize an empty dictionary to store the filtered results
        search_results = {}
        for log_datetime, log_text in log_dictionary.items():
            if log_datetime >= search_from:
                search_results[log_datetime] = log_text
        return search_results or None
    elif datetime_to_search[:1] == '=' and len(datetime_to_search) == 24:
        search_exact = datetime.strptime(datetime_to_search[1:], "%Y-%m-%d %H:%M:%S.%f")
        # Initialize an empty dictionary to store the filtered results
        search_results = {}
        for log_datetime, log_text in log_dictionary.items():
            if log_datetime == search_exact:
                search_results[log_datetime] = log_text
        return search_results or None
    elif datetime_to_search[23:-23] == '|' and len(datetime_to_search) == 47:
        datetime_from, datetime_to = datetime_to_search.split('|')
        search_from_to = (
            datetime.strptime(datetime_from, "%Y-%m-%d %H:%M:%S.%f"),
            datetime.strptime(datetime_to, "%Y-%m-%d %H:%M:%S.%f")
        )
        # Initialize an empty dictionary to store the filtered results
        search_results = {}
        for log_datetime, log_text in log_dictionary.items():
            if search_from_to[0] <= log_datetime <= search_from_to[1]:
                search_results[log_datetime] = log_text
        return search_results or None


def search_by_text(log_dictionary1, search_text=None, exclude_text=None):
    # Initialize an empty dictionary to store the filtered results
    search_results = {}
    for log_datetime, log_text in log_dictionary1.items():
        # Convert all strings to lowercase for ease of search
        log_text_lower = log_text.lower()

        if search_text is not None and exclude_text is not None:
            # Both search_text and exclude_text provided
            if search_text.lower() in log_text_lower and exclude_text.lower() not in log_text_lower:
                search_results[log_datetime] = log_text
        elif search_text is not None:
            # Only search_text provided
            if search_text.lower() in log_text_lower:
                search_results[log_datetime] = log_text
        elif exclude_text is not None:
            # Only exclude_text provided
            if exclude_text.lower() not in log_text_lower:
                search_results[log_datetime] = log_text
    return search_results or None


dates = "2024-12-12 00:11:14.384/.."
texts = None
excludes = "http"
full = True

# Perform the datetime search only if dates is not None
if dates is not None:
    datetime_results = datetime_converter_searcher(log_dict, dates)
else:
    datetime_results = None

# Perform the text search only if texts is not None
if texts is not None or excludes is not None:
    text_results = search_by_text(log_dict, texts, excludes)
else:
    text_results = None

# Initialize an empty dictionary to store the filtered results
filtered_results = {}

# Check which filter was applied and populate filtered_results accordingly
if datetime_results and text_results:
    # Both datetime and text filters are applied
    for log_datetime, log_text in datetime_results.items():
        if log_datetime in text_results:
            filtered_results[log_datetime] = log_text
elif datetime_results:
    # Only datetime filter is applied
    filtered_results = datetime_results
elif text_results:
    # Only text filter is applied
    filtered_results = text_results

if filtered_results:
    # Initialize an empty dictionary and populate it with a for loop
    result_dict = {}
    for log_datetime, log_text in filtered_results.items():
        result_dict[str(log_datetime)] = log_text

    print(result_dict)
else:
    print("No matching entries found.")
