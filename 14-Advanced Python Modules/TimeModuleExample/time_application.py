import file_reader
import time
import calendar


def get_time_float(original_struct_time):
    if original_struct_time.tm_zone == 'GMT':  # original_struct_time is UTC based
        return calendar.timegm(original_struct_time)
    else: # original_struct_time is in local time zone
        return time.mktime(original_struct_time)


def calculate_struct_time(time_float, zone):
    if zone == 'GMT':
        return time.gmtime(time_float)
    else: # calculate local time based on time_float
        return time.localtime(time_float)


if __name__ == '__main__':

    dict_list = file_reader.read_file('timestamps.json')
    print('dict_list = ', dict_list)

    for d in dict_list:
        original_struct_time = time.strptime(d['timestamp'], d['format_string'])
        time_float = get_time_float(original_struct_time)
        calculated_struct_time = calculate_struct_time(time_float, original_struct_time.tm_zone)
        calculated_timestamp = time.strftime(d['format_string'], calculated_struct_time)

        print('********************************************')
        print(f'Original timestamp:   {d["timestamp"]} ')
        print('Original struct_time:    ', original_struct_time, original_struct_time.tm_zone, original_struct_time.tm_gmtoff)
        print(f'Time float {time_float}')
        print('Calculated struct_time:  ', calculated_struct_time, calculated_struct_time.tm_zone, calculated_struct_time.tm_gmtoff)
        print(f'Calculated timestamp: {calculated_timestamp}')
        print(f'Original timestamp == Calculated Timestamp : {d["timestamp"] == calculated_timestamp}')
