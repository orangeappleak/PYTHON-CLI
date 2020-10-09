import click

@click.group(name="uc", help="___THIS COMMAND CONTAINS SOME POWERFUL SUB COMMANDS___")
@click.option("--powerful","-p")
def pow_sub_com(powerful):
    pass

@pow_sub_com.command()
def pow():
    click.secho("I am POWERFULLLLLLL!!!")