import click

@click.command()
@click.option('--count',default = 1, help = "Number of greetings")
@click.option('--name',prompt = "your name", help = "The person to greet")

def hello(count, name):
    for x in range(count):
        click.echo("Hello %s!" % name)

if __name__ == "__main__":
    hello()