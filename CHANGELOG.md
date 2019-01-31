# Changelog
# 0.0.3
- Now able to generate insert statements by arguments parsed through the terminal
- Implemented yanigisawa Python Vin Generator into the program (https://github.com/yanigisawa/VinGenerator)
- Updated yanigisawa VinGenerator to be Python 3 compatible
- Able to generate random vin's

# 0.0.2
- added some functional argument parsing, loosely using functional
- started framework to convert outputs of functions into SQL INSERT formats
- I think I was able to get it to work, we will see in the next update

# 0.0.1
- initial bare-minimum functionality
- generate license plate function
- generate full names and first name based on gender, and last name using names module
- generate a fake email using random characters and numbers or using the name module
- generate a fake phone number, with the format of (xxx)-xxx-xxxx
- can grab an active manufactorer randomly from the manufactorers.txt file
- can grab a year, model, and manufactorer randomly from loaded MySQL data
- adding SQL files from a StackOverflow post, linked their repository in db/thanks
