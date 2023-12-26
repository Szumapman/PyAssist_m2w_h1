from utility.addressbook import AddressBook
from utility.cli_addressbook_interaction import CliAddressBookInteraction


CLI_ADDRESSBOOK_INTERACTION = CliAddressBookInteraction(AddressBook())
ADDRESSBOOK_MENU_COMMANDS = {
    # "exit": cli_pyassist_exit,
    "add": CLI_ADDRESSBOOK_INTERACTION.add_record, #lambda *args: add_record(ADDRESSBOOK, *args),
    "edit": CLI_ADDRESSBOOK_INTERACTION.edit_record, #lambda *args: edit_record(ADDRESSBOOK, *args),
    "show": CLI_ADDRESSBOOK_INTERACTION.show, #lambda *args: show(ADDRESSBOOK, *args),
    "delete": CLI_ADDRESSBOOK_INTERACTION.del_record, #lambda *args: del_record(ADDRESSBOOK, *args),
    # "export": export_to_csv, #lambda *args: export_to_csv(ADDRESSBOOK, *args),
    # "import": import_from_csv, #lambda *args: import_from_csv(ADDRESSBOOK, *args),
    "birthday": CLI_ADDRESSBOOK_INTERACTION.show_upcoming_birthday, #lambda *args: show_upcoming_birthday(ADDRESSBOOK, *args),
    # "search": search, #lambda *args: search(ADDRESSBOOK, *args),
    # "up": pyassit_main_menu,
    # "help": addressbook_commands,
}

# a function that parses user input commands
def  parse_command(user_input: str) -> (str, tuple):
    """
    Parse user input command

    Args:
        user_input (str): user input command
    
    Returns:
        str: command
        tuple: arguments
    """
    tokens = user_input.split()
    command = tokens[0].lower()
    arguments = tokens[1:]
    return command, tuple(arguments)

# receiving a command from a user
def user_command_input():
# def user_command_input(completer: CommandCompleter, menu_name=""):
    # user_input = prompt(f"{menu_name} >>> ", completer=completer).strip()
    user_input = input("???> ")
    if user_input:
        return parse_command(user_input)
    return "", ""
# dict for addressbook menu

def execute_commands(menu_commands: dict, cmd: str, arguments: tuple):
    """Function to execute user commands

    Args:
        menu_commands (dict): dict for menu-specific commands
        cmd (str): user command
        arguments (tuple): arguments from user input

    Returns:
        func: function with data_ti_use and arguments
    """
    if cmd not in menu_commands:
        return f"Command {cmd} is not recognized" #+ similar_command(cmd, menu_commands.keys())
    cmd = menu_commands[cmd]
    return cmd(*arguments)

def main():
    # print(pyfiglet.figlet_format("PyAssist", font = "slant"))
    # print("     ╔════════════════════════════╗")
    # print("     ║         Main Menu          ║")
    # print("     ╠════════════════════════════╣")
    # print("     ║ - addressbook              ║")
    # print("     ║ - notes                    ║")
    # print("     ║ - sort                     ║")
    # print("     ║ - exit                     ║")
    # print("     ╚════════════════════════════╝")
    # pyassit_main_menu()
    while True:
        # cmd, arguments = user_command_input(completer, "address book")
        cmd, arguments = user_command_input()
        print(execute_commands(ADDRESSBOOK_MENU_COMMANDS, cmd, arguments))       
            

if __name__ == "__main__":
    main()