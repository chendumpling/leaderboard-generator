# Markdown Leaderboard Generator
Generates a markdown leaderboard table from a text file

## Summary

  - [Getting Started](#getting-started)
  - [How To Use](#how-to-use)
  - [Contributing](#contributing)
  - [Authors](#authors)
  - [License](#license)

## Getting Started

Refer to [sample_input.txt](https://github.com/robchendev/leaderboard-generator/blob/master/sample_input.txt) and [sample_output.txt](https://github.com/robchendev/leaderboard-generator/blob/master/sample_output.txt) for example input and output. This program can take any number of categories and names, as long as the names are alphabetical ("Name 3" wont work but "Name3" will) and the number of category scores match the number of categories.

When the contents of [sample_output.txt](https://github.com/robchendev/leaderboard-generator/blob/master/sample_output.txt) is pasted into a discord message, it will look like: 

![sample_discord_message.jpg](https://github.com/robchendev/leaderboard-generator/blob/master/sample_discord_message.jpg)

Do note that if you are pasting this markdown into Discord, this doesn't display well on mobile if your leaderboard is wide.

## How To Use

This program was tested using Python 3.8.2. To ensure everything works properly, please make sure your python is up-to-date.

Run the program to display the output by using this command

    cat input.txt | ./leaderboard-generator.py

If you prefer having the output in the format of a text file,

    cat input.txt | ./leaderboard-generator.py > output.txt

If you want to change the spacing of each column or the name of the "Score" column, you can do so by editing the "spacing" and "first_col" variables at the top of [leaderboard-generator.py](https://github.com/robchendev/leaderboard-generator/blob/master/leaderboard-generator.py)

## Contributing

Your contributions are very welcome and appreciated. Following are the things you can do to contribute to this project.

1. **Report a bug** <br>
If you think you've encountered a bug, please inform me by creating an issue [here](https://github.com/robchendev/leaderboard-generator/issues).

2. **Request a feature** <br>
You can request for a feature by creating an issue [here](https://github.com/robchendev/leaderboard-generator/issues), and if it is viable, it will be picked for development.

3. **Create a pull request** <br>
If you improved the bot yourself and would like to contribute to this project, I really appreciate it!

> If you are new to open-source, make sure to check read more about it [here](https://www.digitalocean.com/community/tutorial_series/an-introduction-to-open-source) and learn more about creating a pull request [here](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github).

## Authors

  - **Robert Chen** -
    [robchendev](https://github.com/robchendev)

See also the list of
[contributors](https://github.com/robchendev/leaderboard-generator/contributors)
who participated in this project.

## License

See the [LICENSE](https://github.com/robchendev/leaderboard-generator/blob/master/LICENSE) file for details.
