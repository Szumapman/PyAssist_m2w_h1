import difflib
import pyfiglet
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter

from utility.addressbook import AddressBook
from utility.cli_addressbook_interaction import CliAddressBookInteraction


class CliPyassist:
    
    def __init__(self) -> None:
        self.cli_addressbook_interaction = CliAddressBookInteraction(AddressBook())
        
    def addressbook_interaction(self, *args):
        self.cli_addressbook_interaction.cli_addressbook_menu()
    
    
    def help(self, argument):
        width = 60
        help = f'╔{"═"*width}╗\n' 
        help += "║ {:>12} - {:<43} ║\n".format('command', 'description')   
        help += f'╠{"═"*width}╣\n'
        for command, description in self.COMMANDS_HELP.items():
            help += "║ {:>12} - {:<43} ║\n".format(command, description)
        help += f'╚{"═"*width}╝'
        return help

    COMMANDS = {
        'addressbook': addressbook_interaction,
        'help': help,
    }
    
    COMMANDS_HELP = {
        "addressbook": "open addressbook",
        "exit": "exit from the program",
        "help": "show this menu",
    }
    # a function that parses user input commands
    def  _parse_command(self, user_input: str) -> (str, str):
        """
        Parse user input command

        Args:
            user_input (str): user input command
        
        Returns:
            str: command
            str: argument
        """
        tokens = user_input.split()
        command = tokens[0].lower()
        argument = "".join(tokens[1:])
        return command, tuple(argument)

    # receiving a command from a user
    def _user_command_input(self):
    # def user_command_input(completer: CommandCompleter, menu_name=""):
        commands_completer = FuzzyWordCompleter(self.COMMANDS.keys())
        user_input = prompt(f'PyAssist main menu >>> ', completer=commands_completer).strip()
        # user_input = input(f'CLI_PyAssist main menu >>> ')
        if user_input:
            return self._parse_command(user_input)
        return "", ""
    # dict for addressbook menu

    def _execute_commands(self, cmd: str, argument: str):
        """Function to execute user commands

        Args:
            menu_commands (dict): dict for menu-specific commands
            cmd (str): user command
            argument (str): argument from user input

        Returns:
            func: function with data_ti_use and arguments
        """
        if cmd not in self.COMMANDS:
            matches = difflib.get_close_matches(cmd, self.COMMANDS)
            info =  f'\nmaybe you meant: {' or '.join(matches)}' if matches else ''
            return f"Command {cmd} is not recognized" + info
        cmd = self.COMMANDS[cmd]
        return cmd(self, argument)
    
    
    def main_menu(self):
        while True:
            # cmd, arguments = user_command_input(completer, "address book")
            cmd, argument = self._user_command_input()
            print(self._execute_commands(cmd, argument))    
        

def main():
    print(pyfiglet.figlet_format("PyAssist", font = "slant"))

    cli_pyassist = CliPyassist()
    cli_pyassist.main_menu()       

if __name__ == "__main__":
    main()