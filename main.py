import os
import sys
import subprocess
from langchain.agents import create_openai_agent, AgentExecutor
from langchain.chat_models import ChatOllama
from operate.config import Config
from operate.utils.style import (
    ANSI_GREEN,
    ANSI_RESET,
    ANSI_YELLOW,
    ANSI_RED,
    ANSI_BRIGHT_MAGENTA,
    ANSI_BLUE,
    style,
)
from operate.operate import main as operate_main

# Load configuration
config = Config()

def create_react_agent():
    chat_ollama = ChatOllama(model="llava", temperature=0.7)
    agent = create_openai_agent(chat_ollama, "task_description")
    agent_executor = AgentExecutor.from_agent(agent, chat_ollama, max_iterations=3, verbose=True)
    return agent_executor

def main():
    load_dotenv()
    config.verbose = True

    print(f"{ANSI_BLUE}[CREATING REACT AGENT]{ANSI_RESET}")
    react_agent = create_react_agent()

    print(f"{ANSI_BRIGHT_MAGENTA}[STARTING REACT AGENT]{ANSI_RESET}")
    react_agent.run("Create a task to go to Github.com and verify that the page is visible.")

    print(f"{ANSI_BLUE}[EXECUTING TASK WITH ORIGINAL OPERATE]{ANSI_RESET}")
    operate_main(
        "llava",
        terminal_prompt="Go to Github.com",
        voice_mode=False,
        verbose_mode=True,
        chat_ollama=ChatOllama(model="llava", temperature=0.7)
    )

if __name__ == "__main__":
    main()
