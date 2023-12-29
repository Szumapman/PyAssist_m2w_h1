import difflib
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter

from utility.abstract_notes_interaction import AbstractNotesInteraction
from utility.notes import Notes
from utility.note import Note
from utility.title import Title
from utility.content import Content
from utility.exit_interrupt import ExitInterrupt


class CliNotesInteraction(AbstractNotesInteraction):
    
    def __init__(self, notes: Notes) -> None:
        self.notes = notes


    def show_notes(self, arg):
        return self._display_notes(self.notes, "Your notes:")


    def _display_notes(self, notes: Notes, arg: str) -> str:
        if notes:
            notes_to_show = arg
            i = 0;
            for note in notes.values():
                notes_to_show += f'\nNote {i+1}:\n{note}\n{"═"*30}'
            return notes_to_show   
            
    
    def _set_title_str(self, arg: str) -> str:
        title_completer = FuzzyWordCompleter(self.notes.keys())
        if arg:
            return arg.strip().lower()
        return prompt('Type note title or <<< if you want to cancel: ', completer=title_completer).strip().lower()
        
    
    def _add_title(self, arg):
        title = self._set_title_str(arg)
        while True:
            if title not in self.notes.keys() or title == "<<<" or title == "":
                return title
            print(f"Note with title {title} already exists. Choose another title.")
            title = self._set_title_str("")
            
            
    def create_note(self, arg):
        title = self._add_title(arg)
        if title == "" or title == "<<<":
            return "Operation canceled." 
        content = input("Enter note content: ")
        tags = list(input("Tags (separated by space): ").strip().split())
        self.notes.add_note(Note(Title(title), Content(content), tags))
        return f'Note with title: "{title}", created successfully.'
            
    def choice_note(self):
        pass



    def edit_note(self):
        pass



    def delete_note(self):
        pass



    def add_tag_to_note(self):
        pass



    def sort_notes_by_tag(self):
        pass

    

    def search_notes(self):
        pass
    
    
    def exit_program(self, argument):
        raise ExitInterrupt
    
    
    def help(self, argument):
        width = 75
        help = f'╔{"═"*width}╗\n' 
        help += "║ {:>22} - {:<48} ║\n".format('command', 'description <optional argument>')   
        help += f'╠{"═"*width}╣\n'
        for command, description in self.COMMANDS_HELP.items():
            help += "║ {:>22} - {:<48} ║\n".format(command, description)
        help += f'╚{"═"*width}╝'
        return help
    
    
    # dict for addressbook menu
    NOTES_MENU_COMMANDS = {
        "add": create_note, 
        # "edit": edit_record,
        "show": show_notes,
        # "delete": del_record,
        # "export": export_to_csv, 
        # "import": import_from_csv, 
        # "birthday": show_upcoming_birthday, 
        # "search": search,
        # "save": save_addresbook, 
        "up": 'up',
        "exit": exit_program,
        "help": help,
    }
    
    
    COMMANDS_HELP = {
        "add <title>": "add new note <title>", 
        "edit <title>": "edit note <title>",
        "show": "show all notes",
        "show <title>": "show specific note",
        "delete <title>": "delete note <title>",
        # "export <file name>": "export addressbook to csv file <file name>", 
        # "import <file name>": "import addressbook from csv file <file name>", 
        "search <query>": "search in notes <query>",
        # "save": save_addresbook, 
        "up": 'back tu main menu',
        "exit": "exit from the program",
        "help": "show this menu",
    }
    
    def _execute_command(self, commands_dict: dict, cmd: str, argument):
        """Function to execute user commands

        Args:
            cmd (str): user command
            argument: argument to process
        """
        if cmd not in commands_dict:
            matches = difflib.get_close_matches(cmd, commands_dict)
            info =  f'\nmaybe you meant: {' or '.join(matches)}' if matches else ''
            return f'Command {cmd} is not recognized' + info
        cmd = commands_dict[cmd]
        return cmd(self, argument)
    
    
    # function that parses user input commands
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
        return command, argument
    
    
    # receiving a command from a user
    def _user_command_input(self):
        commands_completer = FuzzyWordCompleter(self.NOTES_MENU_COMMANDS.keys())
        user_input = prompt(f'PyAssist  notes >>> ', completer=commands_completer).strip()
        if user_input:
            return self._parse_command(user_input)
        return "", ""
    
    
    def cli_notes_menu(self):
        while True:
            cmd, argument = self._user_command_input()
            if cmd == 'up':
                return 'back to main menu'
            print(self._execute_command(self.NOTES_MENU_COMMANDS, cmd, argument))