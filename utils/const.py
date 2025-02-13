# L3 or Eco role
# TODO: change roles back to Eco Discord when testing is done
ROLE_IDS_ALLOWED = (1063903240925749389,)
#  ROLE_IDS_ALLOWED = (812675567438659624, 1038497110754086913)

GRANT_PROPOSAL_TIMER_SECONDS = 259200  # 3 days
GRANT_PROPOSAL_TIMER_SLEEP_SECONDS = 60  # 1 minute

LOG_PATH = "logs/lazy-consensus-bot.log"
TESTS_PATH = "tests/"
LOG_FILE_SIZE = 1024 * 1024 * 10
DB_NAME = "lazy-consensus-bot.db"

DISCORD_COMMAND_PREFIX = "!"
# Nickname of a person who's responsible for maintaining the bot (used in some error messages to ping).
RESPONSIBLE_MENTION = "@yulston#0081"

GRANT_PROPOSAL_COMMAND_NAME = 'propose'
COMMAND_FORMAT_RESPONSE = """Hi {author}! This command should look like:

`!propose @username amount description`

> @username - the user you would like to reward.
> amount - how many points you would like to give.
> description - a text that should explain for others what the grant is given for (this is required). If the grant will be applied, I'll post this message.

Some examples:
!propose {author} 100 for being awesome
!propose {author} 100 for using Lazy Consensus bot
"""
# validation.py error messages
ERROR_MESSAGE_NO_MENTIONS = (
    "No mentions found. Please mention the user you want to propose the grant to."
)
ERROR_MESSAGE_INVALID_COMMAND_FORMAT = (
    "The mention must follow after `!propose `. Example: `!propose @mention`."
)
ERROR_MESSAGE_INVALID_USER = "Unable to resolve username. Is the user on this Discord server?"
ERROR_MESSAGE_INVALID_AMOUNT = (
    "The amount must be a positive integer. Example: `!propose @mention 100`."
)
ERROR_MESSAGE_NEGATIVE_AMOUNT = "The amount must be a positive integer: {amount}"
ERROR_MESSAGE_INVALID_DESCRIPTION = (
    "Please provide a description of the grant, like this: `!propose @mention amount description`."
)
