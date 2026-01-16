# Code files from "Python Workout"

My book, "Python Workout" (https://PythonWorkout.com/) contains 50 exercises that help to improve your Python fluency.  This repository contains the code and solutions to those exercises, including all of the "beyond the exercise" additional, bonus exercises.

The main exercises have "pytest" tests, while the "beyond" exercises don't.

## Setup with uv

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Initialize the project (creates pyproject.toml)
uv init

# Pin to Python 3.12
uv python pin 3.12

# Create the virtual environment
uv venv

# Add dependencies (also syncs the venv)
uv add pandas pytest
```

To activate the virtual environment:
```bash
source .venv/bin/activate
```

Or run commands directly with uv:
```bash
uv run python your_script.py
uv run pytest
```

If you like this, you might also like:

- My YouTube channel: https://YouTube.com/reuvenlerner
- Better developers, new, free articles about Python every week: https://BetterDevelopersWeekly.com/
- "Bamboo Weekly," where I analyze data related to current events using Pandas: https://www.BambooWeekly.com/
- My Bluesky feed: https://bsky.app/profile/lernerpython.com
- My first book, "Python Workout": https://PythonWorkout.com/
- My second book, "Pandas Workout": https://PandasWorkout.com/
- LinkedIn, where I also post: https://linkedin.com/in/reuven

Want to get access to all of my courses? Check out my classes at https://LernerPython.com/

And of course, you can always e-mail me at reuven@LernerPython.com .
