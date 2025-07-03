import os
import json
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.markdown import Markdown
from rich.text import Text

from available_tools import available_tools
from tool_convert_temperature_units import convert_temperature_units
from tool_calculate import calculate
from tool_convert_distance_units import convert_distance_units
from openai import OpenAI

# Load environment variables and set up console
load_dotenv()
console = Console()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if not client.api_key:
    console.print("[bold red]❌ OPENAI_API_KEY not found. Check your .env file.[/bold red]")
    exit(1)

# Initialise the conversation
messages = [
    {"role": "system", "content": "You are a helpful assistant that can answer questions, perform calculations, and convert units."}
]

# Function to format and display tool calls
def display_tool_call(name: str, arguments: dict) -> None:
    table = Table(title=f"🔧 Calling tool: [bold]{name}[/bold]", box=None)
    table.add_column("Parameter", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")
    for k, v in arguments.items():
        table.add_row(k, str(v))
    console.print(table)

# Function to handle user input and tool interaction
def chat_with_functions(user_input):
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=available_tools,
        tool_choice="auto"
    )

    assistant_message = response.choices[0].message
    messages.append(assistant_message.model_dump())

    if assistant_message.tool_calls:
        console.print("[bold magenta]🔁 Processing function calls...[/bold magenta]")

        for tool_call in assistant_message.tool_calls:
            function_name = tool_call.function.name
            try:
                arguments = json.loads(tool_call.function.arguments)
            except json.JSONDecodeError:
                console.print(f"[bold red]❌ Failed to decode arguments for {function_name}[/bold red]")
                continue

            display_tool_call(function_name, arguments)

            result = None
            try:
                if function_name == "convert_temperature_units":
                    result = convert_temperature_units(
                        value=arguments["value"],
                        unit_from=arguments["unit_from"],
                        unit_to=arguments["unit_to"]
                    )
                elif function_name == "convert_distance_units":
                    result = convert_distance_units(
                        value=arguments["value"],
                        unit_from=arguments["unit_from"],
                        unit_to=arguments["unit_to"]
                    )
                elif function_name == "calculate":
                    result = calculate(arguments["operation"], arguments["x"], arguments["y"])
                else:
                    console.print(f"[bold red]⚠️ Unknown function:[/bold red] {function_name}")
            except Exception as e:
                console.print(f"[bold red]❌ Error calling function {function_name}:[/bold red] {e}")
                continue

            if result is not None:
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": str(result) if not isinstance(result, dict) else json.dumps(result)
                })

        final_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        final_message = final_response.choices[0].message
        messages.append(final_message.model_dump())

        return final_message.content
    else:
        return assistant_message.content

# Welcome panel
welcome_text = Text.from_markup(
    "[bold blue]🤖 Function-Calling CLI Chatbot[/bold blue]\n"
    "Connected to [green]OpenAI[/green] with tool support.\n"
    "Type your message or 'exit' to quit."
)
console.print(Panel(welcome_text, title="[bold green]Welcome[/bold green]", padding=(1, 2)))

# Main input loop
while True:
    try:
        user_input = Prompt.ask("\n[bold cyan]You[/bold cyan]")
        if user_input.lower() in ["exit", "quit", "bye"]:
            console.print("[bold yellow]👋 Goodbye![/bold yellow]")
            break

        reply = chat_with_functions(user_input)
        console.print(Panel.fit(Markdown(reply), title="[bold green]Assistant[/bold green]"))

    except KeyboardInterrupt:
        console.print("\n[bold red]Interrupted by user. Exiting...[/bold red]")
        break
