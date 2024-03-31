import os
import sys
from dotenv import load_dotenv
from langchain.chat_models import ChatOllama
from prompt_toolkit.shortcuts import input_dialog

class Config:
    """
    Configuration class for managing settings.

    Attributes:
        verbose (bool): Flag indicating whether verbose mode is enabled.
        ollama_model (str): Model name for Ollama.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            # Put any initialization here
        return cls._instance

    def __init__(self):
        load_dotenv()
        self.verbose = False
        self.ollama_model = (
            None  # instance variable is a backup in case saving to a `.env` fails
        )

    def initialize_ollama(self):
        if self.verbose:
            print("[Config][initialize_ollama]")

        if self.ollama_model:
            if self.verbose:
                print("[Config][initialize_ollama] using cached ollama_model")
            model_name = self.ollama_model
        else:
            if self.verbose:
                print(
                    "[Config][initialize_ollama] no cached ollama_model, try to get from env."
                )
            model_name = os.getenv("OLLAMA_MODEL", "llava")

        chat_ollama = ChatOllama(model=model_name, temperature=0.7)
        return chat_ollama

    def validation(self, model):
        """
        Validate the input parameters for the dialog operation.
        """
        self.require_model(
            "OLLAMA_MODEL",
            "Ollama model",
            model == "llama2" or model == "llama7b" or model == "llava",
        )

    def require_model(self, key_name, key_description, is_required):
        key_exists = bool(os.environ.get(key_name))
        if self.verbose:
            print("[Config] require_model")
            print("[Config] key_name", key_name)
            print("[Config] key_description", key_description)
            print("[Config] key_exists", key_exists)
        if is_required and not key_exists:
            self.prompt_and_save_model(key_name, key_description)

    def prompt_and_save_model(self, key_name, key_description):
        key_value = input_dialog(
            title="Model Required", text=f"Please enter the {key_description}:"
        ).run()

        if key_value is None:  # User pressed cancel or closed the dialog
            sys.exit("Operation cancelled by user.")

        if key_value:
            self.ollama_model = key_value
            self.save_model_to_env(key_name, key_value)
            load_dotenv()  # Reload environment variables
            # Update the instance attribute with the new key

    @staticmethod
    def save_model_to_env(key_name, key_value):
        with open(".env", "a") as file:
            file.write(f"\n{key_name}='{key_value}'")
