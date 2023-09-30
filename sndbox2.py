from datetime import datetime


def search_by_text(log_dictionary1, search_text=None, exclude_text=None):
    search_results = {}

    for log_datetime, log_text in log_dictionary1.items():
        if search_text is not None and exclude_text is not None:
            # Both search_text and exclude_text provided
            if search_text in log_text and exclude_text not in log_text:
                search_results[log_datetime] = log_text
        elif search_text is not None and exclude_text is None:
            # Only search_text provided
            if search_text in log_text:
                search_results[log_datetime] = log_text
        elif exclude_text is not None:
            # Only exclude_text provided
            if exclude_text not in log_text:
                search_results[log_datetime] = log_text

    return search_results


# Example usage:
log_dictionary1 = {
    datetime(2023, 9, 30, 10, 0): "Error: Something went wrong",
    datetime(2023, 9, 30, 11, 0): "Info: Task completed successfully",
    datetime(2023, 9, 30, 12, 0): "Warning: Disk space low",
}

search_text = "Warning"
exclude_text = None

results = search_by_text(log_dictionary1, search_text, exclude_text)
print(results)