# Exercise:

# Update the "What Did the Cat Say" program from an earlier section so that it can be run directly
# or imported as a module. When it runs as a program is should prompt for input and display a cat
# "saying" what was provided by the user. Place the input provided by the user inside a speech
# bubble. Make the speech bubble expand or contract to fit around the input provided by the user.

import cat

input = input("What does the cat say?: ")
cat.meow(input)