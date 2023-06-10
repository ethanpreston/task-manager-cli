from rich.console import Console
from rich.table import Table
import random


def display(tasks):
    console = Console()
    console.print("[bold magenta]Task Manager[/bold magenta]!", "💻")

    # Format the table for the tasks
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Task", min_width=20)
    table.add_column("Priority", min_width=12, justify="center")
    table.add_column("Due Date", min_width=12, justify="center")
    table.add_column("Category", min_width=12, justify="center")
    table.add_column("Completed", min_width=12, justify="center")

    # Collect all the tasks
    categories = [task[3] for task in tasks]

    # Standard colors according to the Rich documentation
    colors1 = ["red", "green", "yellow", "blue", "magenta", "cyan"]
    colors2 = ["bright_red", "bright_green", "bright_yellow", "bright_blue", "bright_magenta", "bright_cyan"]

    def assign_colors(categories_list, colors_1, colors_2):
        color_assignments = dict()
        while categories_list:
            category = categories_list.pop()
            if colors_1:
                index = random.randint(0, len(colors_1) - 1)
                color = colors_1[index]
                color_assignments[category] = color
                colors_1.pop(index)
            else:
                index = random.randint(0, len(colors_2) - 1)
                color = colors_2[index]
                color_assignments[category] = color
                colors_2.pop(index)
        return color_assignments

    colors_categories = assign_colors(list(categories), list(colors1), list(colors2))

    for idx, task in enumerate(tasks, start=1):
        c = colors_categories[task[3]]
        is_done_str = '✅' if task[4] else '❌'
        table.add_row(str(idx), task[0], task[1], task[2], f'[{c}]{task[3]}[/{c}]', is_done_str)
    console.print(table)
