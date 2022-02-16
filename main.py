# Project WingCap
# Author: Dr_Longshanks
#
# A program to assist speedrunners focus their practice sessions on parts of the game (segments) that need
# the most work, as determined by their own segment times and those of user-selected benchmarks.
#
# A user selects their language, skill level, desired category, platform, and region. These will be saved and used to
# access relevant data in some database.

# Eventually I would like to collaborate with SM64 players from around the world to implement more languages.
language_set = ["English"]

# List of skill levels the user can select
skill_list = ["Total Noob", "Beginner", "Intermediate", "Expert", "WR Contender"]

# List of categories for the user to select
# --Perhaps this should be split between base game categories and category extension to prevent the possibility of
# overwhelming new players, and for the sake of pushing out a product that will be more accessible to the greater
# population, at first. Category extensions should eventually be added, or added in an "Other Categories" section
cat_list = ["120 Star", "70 Star", "16 Star", "16 Star No LBLJ", "1 Star", "0 Star"]

# If the player selects "Total Noob" or "Beginner", AND "1 Star" or "0 Star", maybe an alert should appear to inform
# the user that those are considered technically challenging categories and are not recommended for beginners.
# A "Play at your own risk..." type of deal.

# List of platforms the user could be playing on
plat_list = ["N64", "Emulator (PJ64)", "WiiVC", "WiiUVC", "Switch"]

# List of regions the user could be playing on
region_list = ["US", "JP", "PAL"]