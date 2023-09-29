import time
import requests

url = "https://api-mob1.ebanq-qa.com/accounts/private/v1/admin/requests/csv/import"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdXRoIjp7ImFsbG93ZWRfcGF0aHMiOlsiKioiXX0sImV4cCI6MTY5NTkyNTUzMiwiZmlyc3ROYW1lIjoiaWciLCJpYXQiOjE2OTU5MjM3MzIsImxhc3ROYW1lIjoiYWQiLCJyb2xlTmFtZSI6ImFkbWluIiwic2lnbmF0dXJlIjoiTG50TXI0VXdiTnEzTVc1LXRBLXNFRnVPRmszenZfM1UzcFpiUTVjMTNuZz0iLCJzdWIiOiJhY2Nlc3MiLCJ1aWQiOiJkNTRhN2EyMy1lMGZmLTRmOWYtYmQ3Yi1hNzgyNWVhNThjZTciLCJ1c2VybmFtZSI6ImlnYWQifQ.pj41EO-88yH1usi8Y4lzpalFUN3zTjOLgWIOqyyR3-qswdSHSVOkLy0yi7lOOC1MLg8CUX3xBxVR8aR4XqxXjg",
    "Cookie": "token_signature=kz08oIwlSDYg4yCI3OvC83FUZ767Rh9v"
}

duration = 3600  # 1 hour in seconds
interval = 60  # 60 seconds

start_time = time.time()
end_time = start_time + duration
count = 0
while time.time() < end_time:
    count += 1
    files = {
        "file": ("imp2.txt", open("imp2.txt", "rb"), "text/csv"),
    }
    try:
        response = requests.post(url, headers=headers, files=files)
        if response.status_code == 200:
            print(response.text, count)
        else:
            print(f"Error: {response.status_code} - {response.json()} and count = {count}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    time.sleep(interval)





# import sys
# from _datetime import datetime
# import colorama
#
# data = """
# 2022-02-03 00:01:13.623 [http-nio-*8625*-exec-*7*] ERROR *i.k.i.repository.FunctionsRepository* - Sql exception for geometry {"type":"GeometryCollection","geometries":[{"type":"Polygon","coordinates":[[[*69*.*9*,*-18.03*],[*69*.*90147203*,*-18.029963864*],[*69*.*902940514*,*-18.029855542*],[*69*.*904401914*,*-18.029675295*],[*69*.*90585271*,*-18.029423558*],[*69*.*907289405*,*-18.029100938*],[*69*.*90870854*,*-18.02870821*],[*69*.*910106696*,*-18.028246322*],[*69*.*911480503*,*-18.027716386*],[*69*.*912826653*,*-18.027119679*],[*69*.*914141902*,*-18.026457638*],[*69*.*915423082*,*-18.025731858*],[*69*.*916667107*,*-18.024944088*],[*69*.*917870979*,*-18.024096226*],[*69*.*919031799*,*-18.023190314*],[*69*.*920146769*,*-18.022228534*],[*69*.*921213203*,*-18.021213203*],[*69*.*922228534*,*-18.020146769*],[*69*.*923190314*,*-18.019031799*],[*69*.*924096226*,*-18.017870979*],[*69*.*924944088*,*-18.016667107*],[*69*.*925731858*,*-18.015423082*]ERROR: canceling statement due to user request; nested exception is org.postgresql.util.PSQLException: ERROR: canceling statement due to user request
# 2022-02-03 00:06:13.838 [http-nio-8625-exec-5] ERRORi.k.i.repository.FunctionsRepository - Sql exception for geometry {"type":"GeometryCollection","geometries":[{"type":"Polygon","coordinates":[[[127.169737423,10.375975952],[127.154508037,10.366987298],[127.138968572,10.358526204],[127.12313796,10.350602977],[127.107035489,10.343227271],[127.090680778,10.336408073],[127.074093751,10.33015369],[127.057294617,10.324471742],[127.040303845,10.319369152],[127.023142134,10.314852137],[127.005830393,10.3109262],[126.988389714,10.307596123],[126.970841345,10.304865966],[126.953206668,10.302739052],[126.935507166,10.301217975],[126.917764405,10.300304586],[126.9,10.3],[126.882235595,10.300304586],[126.864492834,10.301217975],[126.846793332,10.302739052],[126.829158655,10.304865966],[126.811610286,10.307596123],[126.794169607,10.3109262],[126.776857866,10.314852137],[125.714971742,10.572278205],[125.689185268,10.579053728],[124.712383426,10.858838449],[124.689663089,10.865645304],[124.667199016,10.873225022],[124.008490363,11.116296354],[123.98071637tage from stat_area st]; ERROR: canceling statement due to user request; nested exception is org.postgresql.util.PSQLException: ERROR: canceling statement due to user request
# 2022-02-03 00:11:14.384 [http-nio-8625-exec-3] ERROR i.k.i.repository.FunctionsRepository - Sql exception for geometry {"type":"GeometryCollection","geometries":[{"type":"Polygon","coordinates":[[[137.023916564,14.815552392],[136.409366555,15.045914225],[136.401292502,15.048062411],[135.830806031,15.199846286],[135.783411888,15.212455992],[135.530696713,15.244357164],[135.488757978,15.250729352],[135.447076609,15.25850175],[135.112960288,15.328825481],[134.30536366,15.311635216],[134.228846078,15.262873997],[134.190691128,15.239091832],[134.151694677,15.21660222],[134.111904237,15.195432561],[134.071368286,15.175608648],[134.030136211,15.157154632],[133.988258246,15.140092998],[133.945785414,15.124444531],[1"""
#
# log_dict = {}
# lines = data.split('\n')
# count_logs = 0
# for line in lines:
#     # For each non-empty line, the script splits it by spaces
#     if line.strip() != '':
#         parts = line.split(' ')
#         date_str = parts[0] + ' ' + parts[1]
#         log_message = ' '.join(parts[2:])
#         datetime_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
#         log_dict[datetime_obj] = log_message
#         count_logs += 1
#
# print(log_dict)
# print(count_logs)
#
#
# # Parser of the datetime input according to the -h(help description)
# # def datetime_converter_searcher(dict1, datetime_to_search):
# #     # do nothing if the user did not enter value - > return None
# #     if datetime_to_search is None:
# #         return None
# #     # add check if isinstance(datetime_to_search, datetime):
# #     elif datetime_to_search.startswith('../'):
# #         # convert to: ../2023-01-01 00:00:00.000
# #         # return <class 'datetime.datetime'>
# #         search_to = datetime.strptime(datetime_to_search[3:], "%Y-%m-%d %H:%M:%S.%f")
# #         # search result by 'date to'
# #         search_results = []
# #         for log_datetime, log_text in dict1.items():
# #             if log_datetime <= search_to:
# #                 search_results.append((log_datetime, log_text))
# #         return search_results
# #     elif datetime_to_search.endswith('/..'):
# #         # convert from: 2023-01-01 00:00:00.000/..
# #         # return <class 'datetime.datetime'>
# #         search_from = datetime.strptime(datetime_to_search[:-3], "%Y-%m-%d %H:%M:%S.%f")
# #         # search result by 'date from'
# #         search_results = []
# #         for log_datetime, log_text in dict1.items():
# #             if log_datetime >= search_from:
# #                 search_results.append((log_datetime, log_text))
# #         return search_results
# #     elif datetime_to_search.startswith('-'):
# #         # convert exact: -2023-01-01 00:00:00.000
# #         # return <class 'datetime.datetime'>
# #         search_exact = datetime.strptime(datetime_to_search[1:], "%Y-%m-%d %H:%M:%S.%f")
# #         # search result by 'exact date'
# #         search_results = []
# #         for log_datetime, log_text in dict1.items():
# #             if log_datetime == search_exact:
# #                 search_results.append((log_datetime, log_text))
# #         return search_results
# #     elif '|' in datetime_to_search:
# #         datetime_from, datetime_to = datetime_to_search.split('|')
# #         # convert from-to: 2023-01-01 00:00:00.000|2023-01-01 00:00:00.000
# #         # return <class 'datetime.datetime'> as tuple
# #         search_from_to = (
# #             datetime.strptime(datetime_from, "%Y-%m-%d %H:%M:%S.%f"),
# #             datetime.strptime(datetime_to, "%Y-%m-%d %H:%M:%S.%f")
# #         )
# #         # search result by 'from-to date'
# #         search_results = []
# #         for log_datetime, log_text in dict1.items():
# #             if search_from_to[0] <= log_datetime <= search_from_to[1]:
# #                 search_results.append((log_datetime, log_text))
# #         return search_results
#
# def datetime_converter_searcher(dict1, datetime_to_search):
#     # do nothing if the user did not enter value - > return None
#     if datetime_to_search is None:
#         return None
#     # add check if isinstance(datetime_to_search, datetime):
#     elif '../' in datetime_to_search:
#         # convert to: ../2023-01-01 00:00:00.000
#         # return <class 'datetime.datetime'>
#         search_to = datetime.strptime(datetime_to_search[3:], "%Y-%m-%d %H:%M:%S.%f")
#         # search result by 'date to'
#         search_results = []
#         for log_datetime, log_text in dict1.items():
#             if log_datetime <= search_to:
#                 search_results.append((log_datetime, log_text))
#         return search_results
#     elif '/..' in datetime_to_search:
#         # convert from: 2023-01-01 00:00:00.000/..
#         # return <class 'datetime.datetime'>
#         search_from = datetime.strptime(datetime_to_search[:-3], "%Y-%m-%d %H:%M:%S.%f")
#         # search result by 'date from'
#         search_results = []
#         for log_datetime, log_text in dict1.items():
#             if log_datetime >= search_from:
#                 search_results.append((log_datetime, log_text))
#         return search_results
#     elif '=' in datetime_to_search:
#         # convert exact: -2023-01-01 00:00:00.000
#         # return <class 'datetime.datetime'>
#         search_exact = datetime.strptime(datetime_to_search[1:], "%Y-%m-%d %H:%M:%S.%f")
#         # search result by 'exact date'
#         search_results = []
#         for log_datetime, log_text in dict1.items():
#             if log_datetime == search_exact:
#                 search_results.append((log_datetime, log_text))
#         return search_results
#     elif '|' in datetime_to_search:
#         datetime_from, datetime_to = datetime_to_search.split('|')
#         # convert from-to: 2023-01-01 00:00:00.000|2023-01-01 00:00:00.000
#         # return <class 'datetime.datetime'> as tuple
#         search_from_to = (
#             datetime.strptime(datetime_from, "%Y-%m-%d %H:%M:%S.%f"),
#             datetime.strptime(datetime_to, "%Y-%m-%d %H:%M:%S.%f")
#         )
#         # search result by 'from-to date'
#         search_results = []
#         for log_datetime, log_text in dict1.items():
#             if search_from_to[0] <= log_datetime <= search_from_to[1]:
#                 search_results.append((log_datetime, log_text))
#         return search_results
#
#
# datetime1 = input("datetime: ")
# search1 = datetime_converter_searcher(log_dict, datetime1)
# print(search1)
#
# # # Search by text
# # def search_by_text(dict1, search_text, exclude_text):
# #     if search_text is None:
# #         return None
# #     search_results = []
# #     for log_datetime, log_text in dict1.items():
# #         if search_text in log_text and (exclude_text is None or exclude_text not in log_text):
# #             search_results.append((log_datetime, log_text))
# #     return search_results
# #
# #
# # # Search by datetime and text
# # def search_by_datetime_and_text(dict1, search_dates, search_text, exclude_text, full):
# #     datetime_results = search_by_datetime(dict1, search_dates)
# #     text_results = search_by_text(dict1, search_text, exclude_text)
# #     if datetime_results is None and text_results is None:
# #         return sys.exit('Nothing to search :(')
# #     elif datetime_results is None:
# #         if full:
# #             return [f"{str(log_datetime)}, {str(log_text)}" for log_datetime, log_text in text_results]
# #         else:
# #             return [f"{str(log_datetime)}, {str(log_text)[:150]}" for log_datetime, log_text in text_results]
# #     elif text_results is None:
# #         if full:
# #             return [f"{str(log_datetime)}, {str(log_text)}" for log_datetime, log_text in datetime_results]
# #         else:
# #             return [f"{str(log_datetime)}, {str(log_text)[:150]}" for log_datetime, log_text in datetime_results]
# #     combined_results = []
# #     for datetime_result, log_text in datetime_results:
# #         if datetime_result in text_results:
# #             combined_results.append((datetime_result, log_text))
# #     if full:
# #         return [f"{str(log_datetime)}, {str(log_text)}" for log_datetime, log_text in combined_results]
# #     else:
# #         result = []
# #         for log_datetime, log_text in combined_results:
# #             result.append(f"{str(log_datetime)}, {str(log_text)[:150]}")
# #         return result
# #         # return [f"{str(log_datetime)}, {str(log_text)[:150]}" for log_datetime, log_text in combined_results]
# #
# #
# # print('Please see results:')
# # result = search_by_datetime_and_text(log_dict, datetime_parser(args.datetime), args.text, args.exclude, args.full)
# # print(str(result).strip('[]'))
# # print("*****************************************************************************************")
# # print("Total number of logs that were handled:", count_logs)
# # print("The number of logs that meet search criteria:", len(result))
