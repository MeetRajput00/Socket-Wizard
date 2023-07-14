import typer

app = typer.Typer()


@app.command("hi")
def sample_func():
    print("Hello world!")

@app.command("helloWorld")
def sample_func():
    print("Whatup!!")

if __name__ == "__main__":
    app()    