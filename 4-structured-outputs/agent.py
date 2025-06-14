from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field


class EmailContent(BaseModel):
    subject: str = Field(
        description = "The subject line of the email. Should be concise and descriptive"
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with the proper greeting, paragraphs."
    )


root_agent = LlmAgent(
    name='email_agent',
    model='gemini-2.0-flash',
    description="generates professional emails with structured subject and body",
    instruction="""
        You are an Email Generation Assitant.
        Your task is to generate a professionale mail based on the user's request.
        IMPORTANT: Your response must be valid json matching this structure:
        {
        "subject":"Subject line here",
        "body":"Email body here with proper paragraphs and formatting",
        }
    """,
    output_schema=EmailContent,
    output_key="email"
)