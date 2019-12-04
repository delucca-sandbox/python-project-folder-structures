def select_option_command(option_obj: dict) -> dict:
    option = option_obj.get("selected_option")
    commands = option_obj.get("avaiable_commands") or dict()

    return dict(**option_obj, command=commands.get(option))
