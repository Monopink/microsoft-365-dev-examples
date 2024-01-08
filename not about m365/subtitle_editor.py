def adjust_subtitle_timing(subtitle_file, time_interval_ms):
    with open(subtitle_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i in range(1, len(lines), 4):
        timing_line = lines[i].strip().split(" --> ")
        start_time = timing_line[0].split(",")
        end_time = timing_line[1].split(",")

        if i + 4 < len(lines):
            next_timing_line = lines[i + 4].strip().split(" --> ")
            next_start_time = next_timing_line[0].split(",")

            # Convert start time to milliseconds
            start_time_ms = convert_time_to_milliseconds(start_time[0]) + int(start_time[1])

            # Calculate the time difference in milliseconds
            next_start_time_ms = convert_time_to_milliseconds(next_start_time[0]) + int(next_start_time[1])
            time_difference_ms = next_start_time_ms - start_time_ms

            # Update the current timing line
            lines[i] = "{} --> {}\n".format(timing_line[0], convert_milliseconds_to_time(start_time_ms + time_difference_ms - time_interval_ms))

    new_subtitle_file = subtitle_file.replace(".srt", "_adjusted.srt")

    with open(new_subtitle_file, 'w', encoding='utf-8') as file:
        file.writelines(lines)

    print("Adjusted subtitle file has been saved as: {}".format(new_subtitle_file))


def convert_time_to_milliseconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(":"))
    return hours * 3600000 + minutes * 60000 + seconds * 1000


def convert_milliseconds_to_time(milliseconds):
    seconds = int(milliseconds / 1000)
    minutes = int(seconds / 60)
    hours = int(minutes / 60)

    milliseconds %= 1000
    seconds %= 60
    minutes %= 60

    return "{:02d}:{:02d}:{:02d},{:03d}".format(hours, minutes, seconds, milliseconds)


# Usage example

# Replace with your subtitle file path
subtitle_file_path = "your_subtitle_file.srt"
# Replace with the desired time interval in milliseconds
time_interval_ms = 10

adjust_subtitle_timing(subtitle_file_path, time_interval_ms)
