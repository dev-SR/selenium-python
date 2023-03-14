from tkinter.messagebox import showinfo
import click
from gub.result.result import Result
from gub.resultNew.result_new import ResultNew
from rich.console import Console
from rich.table import Table
import inquirer

console = Console()
with console.capture() as capture:
    console.print("[green]Student ID[/]", end=" ")
str_id = capture.get()
with console.capture() as capture:
    console.print("[green]Password[/](hidden)", end=" ")
str_pass = capture.get()


def withLoadder(cb, message):
    done = False
    returns = None
    with console.status(f"[bold yellow] {message}...", spinner="aesthetic") as s:
        while not done:
            returns = cb()
            done = True
    return returns


def withLoadderWithParam(cb, param, message):
    done = False
    returns = None
    with console.status(f"[bold yellow] {message}...", spinner="aesthetic") as s:
        while not done:
            returns = cb(*param)
            done = True
    return returns


def fromOld():
    # id = click.prompt(str_id)
    # password = click.prompt(str_pass, hide_input=True)
    try:
        with Result() as bot:
            resultAfterLoginLoaded = False
            done = False
            with console.status("[bold yellow] Initializing...", spinner="aesthetic") as s:
                while not done:
                    resultAfterLoginLoaded = bot.land_result_page()
                    done = True
            if resultAfterLoginLoaded:
                print('Trying to login...')
                done = False
                resultFetched = False
                landedOnResultPage = False
                with console.status("[bold yellow]Loading...", spinner="aesthetic") as s:
                    while not done:
                        loginSuccess = bot.signIn(
                            id='191902061', password='soikotj201')
                        if loginSuccess:
                            landedOnResultPage = bot.landOnLoginPage()
                        done = True

                if resultFetched:
                    bot.print_result()
            else:
                # console.print("[red]Page could not be loaded in time[/]")
                bot.exit_message = "[red]Page could not be loaded in time[/]"

    except Exception as e:
        if 'in PATH' in str(e):
            print(
                'You are trying to run the bot from command line \n'
                'Please add to PATH your Selenium Drivers \n'
                'Windows: \n'
                '    set PATH=%PATH%;<C:path-to-your-folder> \n \n'
                'Linux: \n'
                '    PATH=$PATH:</path-to-your-folder \n'
            )
        else:
            raise


def fromNew(id, password):
    try:
        with ResultNew() as bot:
            landOnLoginPage = False
            done = False
            landOnLoginPage = withLoadder(
                bot.landOnLoginPage, "Initializing")

            if landOnLoginPage:
                console.print(
                    "[green]Done!![/] :muscle:")
                landOnResultPage = False
                loginSuccess = False
                if landOnLoginPage:
                    loginSuccess = withLoadderWithParam(
                        bot.signIn, [id, password], "Trying to login")

                if loginSuccess:
                    console.print(
                        "[green]Login Successful[/] :smiley:")
                    landOnResultPage = withLoadder(
                        bot.landOnResultPage, "Fetching Result")
                else:
                    bot.exit_message = "[red]Login Failed[/]"
                if landOnResultPage:
                    console.print(
                        "[green]Result Collected[/] :v:")
                    withLoadderWithParam(
                        bot.get_result, [id], "Showing Result;Please Wait")
                    bot.print_result()
                else:
                    bot.exit_message = "[red]Page could not be loaded in time[/]"
            else:
                # console.print("[red]Page could not be loaded in time[/]")
                bot.exit_message = "[red]Page could not be loaded in time[/]"

    except Exception as e:
        if 'in PATH' in str(e):
            print(
                'You are trying to run the bot from command line \n'
                'Please add to PATH your Selenium Drivers \n'
                'Windows: \n'
                '    set PATH=%PATH%;<C:path-to-your-folder> \n \n'
                'Linux: \n'
                '    PATH=$PATH:</path-to-your-folder \n'
            )
        else:
            raise


def App():
    id = click.prompt(str_id, default="191902061", show_default=True)
    password = click.prompt(str_pass, hide_input=True,
                            default='S.oikat!123', show_default=False)
    questions = [
        # inquirer.Text("id", message="ID", default='191902061'),
        # inquirer.Text("password", message="Password", default='S.oikat!123'),

        inquirer.List('option',
                      message="Get Result From",
                      choices=['Old Website', 'New Website'],
                      default='New Website'
                      ),
    ]
    answers = inquirer.prompt(questions)
    if answers['option'] == 'Old Website':
        fromOld()
    else:
        # fromNew(id=answers['id'], password=answers['password'])
        fromNew(id, password)


if __name__ == '__main__':
    App()
