from google.adk.agents import Agent

root_agent = Agent(
    name="basic_app",
    model="gemini-2.0-flash",
    description="Greeting Agent.",
    instruction="""
    You are a helpful assitant that greets the user.
    Ask for the user's name and greet them by name.
    """
)
