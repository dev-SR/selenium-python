from rich.console import Console
from rich.table import Table
from rich import box


console = Console()

table = Table(show_header=True, box=box.ROUNDED,
              title="Your Results", title_style="bold yellow")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Production Budget", justify="right")
table.add_column("Box Office", justify="right")
table.add_row(
    "Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
)
table.add_row(
    "May 25, 2018",
    "[red]Solo[/red]: A Star Wars Story",
    "$275,000,000",
    "$393,151,347",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VIII: The Last Jedi",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VII: The Force Awakens",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VII: The Force Awakens",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VII: The Force Awakens",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VII: The Force Awakens",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)

console.print(table)
