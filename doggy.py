import click
import time
import random

@click.group(invoke_without_command=True)
@click.option('--username','-u', default=False)
@click.pass_context
def cli(ctx,username):
    ctx.ensure_object(dict)
    ctx.obj['USER_NAME'] = username
    return

@cli.command(help="says hello n numer of times and also proves your dumb")
@click.option("--count","-c",default=5,help="says hello n times")
def hel(count):
    for x in range(count):
        click.echo("Hello DUMBO")

@cli.command(short_help = "proves that you are dumb")
@click.argument('name',default="you are an idiot")
def name(name):
    click.secho("Hello idiot,",fg="white",bg="black")
    time.sleep(1.2)
    click.secho("OH shit my bad.",fg="white",bg="black")
    time.sleep(1)
    if name == "you are an idiot":
        click.secho("give me your name to greet IDIOT",fg="white",bg="black")
    else:
        click.secho("Hello %s" % name, fg="red",bg="white")

@cli.command()
@click.pass_context
def info(ctx):
    print(ctx.obj)
    print(ctx.obj['USER_NAME'])
    
