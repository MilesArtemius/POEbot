import system.command_system


def info():
    message = ''
    for c in system.command_system.command_list:
        message += c.key + ' - ' + c.description + '\n'
    return message, ''


info_command = system.command_system.Command()

info_command.key = 'помощь'
info_command.description = 'Покажу список команд'
info_command.process = info
