import difflib
import pyfiglet
import cowsay
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter

from utility.addressbook import AddressBook
from utility.notes import Notes
from utility.cli_addressbook_interaction import CliAddressBookInteraction
from utility.sorter import FileSorter
from utility.cli_notes_interaction import CliNotesInteraction
from utility.exit_interrupt import ExitInterrupt


class CliPyassist:
    
    # function to handle with errors
    def _error_handler(func):
        def wrapper(self, *args):
            while True:
                try:
                    return func(self, *args)
                except (ExitInterrupt, KeyboardInterrupt):
                    self.cli_pyassist_exit("")
                except Exception as e:
                    return f"Error: {e}. Please try again."
        return wrapper

    
    def __init__(self) -> None:
        self.cli_addressbook_interaction = CliAddressBookInteraction(AddressBook())
        self.cli_notes_interaction = CliNotesInteraction(Notes())


    def addressbook_interaction(self, *args):
        return self.cli_addressbook_interaction.cli_addressbook_menu()
    
    
    def notes_interaction(self, *args):
        return self.cli_notes_interaction.cli_notes_menu()
    
    
    def sort_init(self, folder_path):
        if not folder_path:
            folder_path = input("Type the path to the folder whose contents you want to sort: ").strip()
        sorter = FileSorter()
        return sorter.sort(folder_path)
    
    
    # exit / close program
    def cli_pyassist_exit(self, argument):
        self.cli_addressbook_interaction.save_addressbook(None)
        self.cli_notes_interaction.save_notes(None)
        cowsay.cow("Your data has been saved.\nGood bye!") 
        sys.exit()
    
    # show help
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
        'notes': notes_interaction,
        'sort': sort_init,
        'exit': cli_pyassist_exit,
        'help': help,
    }
    
    
    COMMANDS_HELP = {
        "addressbook": "open addressbook",
        "notes": "open notes",
        "sort <folder path>": "sort files <in given folder>",
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
        commands_completer = FuzzyWordCompleter(self.COMMANDS.keys())
        user_input = prompt(f'main menu >>> ', completer=commands_completer).strip()
        if user_input:
            return self._parse_command(user_input)
        return "", ""
    

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
    
    
    @_error_handler
    def main_menu(self):
        while True:
            cmd, argument = self._user_command_input()
            print(self._execute_commands(cmd, argument))    


def main():
    print(pyfiglet.figlet_format("PyAssist", font = "slant"))
    cli_pyassist = CliPyassist()
    cli_pyassist.cli_addressbook_interaction.load_addressbook(None)
    cli_pyassist.cli_notes_interaction.load_notes(None)
    cli_pyassist.main_menu()       

if __name__ == "__main__":
    main()