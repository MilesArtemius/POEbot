import system.command_system
import vk_io.vk_api


def cat():
    # null
    return 'fuck da life', ''


cat_command = system.command_system.Command()

cat_command.key = 'котик'
cat_command.description = 'Fuck you!'
cat_command.process = cat
