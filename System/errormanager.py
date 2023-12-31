
#Do not run independently
def error(error_type, reason):
    if error_type == "user":
        print(f"user error. {reason}")

    elif error_type == "system":
        print(f"system error. {reason}")

    else:
        print("That is not valid error type. For developer")
