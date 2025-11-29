Logs = ["ERROR: NullPointer at line 23",
        "INFO: Test started",
        "ERROR: Timeout at line 45",
        "WARNING: Low memory",
        "ERROR: Connection failed"]


# ["NullPointer at line 23", "Timeout at line 45", "Connection failed"]

def check_errors():
    Errors = []
    for error in Logs:
        if error.startswith("ERROR"):
            Errors.append(error)

    return Errors


print(check_errors())