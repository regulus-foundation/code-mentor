"""Configuration class to store the state of bools for different scripts access."""
import os
import re

from colorama import Fore

from codementor.core.configuration.schema import Configurable, SystemSettings


class ConfigSettings(SystemSettings):
    fast_llm_model: str
    smart_llm_model: str
    description: str


class Config(Configurable):
    default_plugins_config_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "plugins_config.yaml"
    )

    elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")
    if os.getenv("USE_MAC_OS_TTS"):
        default_tts_provider = "macos"
    elif elevenlabs_api_key:
        default_tts_provider = "elevenlabs"
    elif os.getenv("USE_BRIAN_TTS"):
        default_tts_provider = "streamelements"
    else:
        default_tts_provider = "gtts"

    defaults_settings = ConfigSettings(
        name="Default Server Config",
        description="This is a default server configuration",
        smart_llm_model="gpt-3.5-turbo",
        fast_llm_model="gpt-3.5-turbo",
    )


def check_openai_api_key(config: Config) -> None:
    """Check if the OpenAI API key is set in config.py or as an environment variable."""
    if not config.openai_api_key:
        print(
            Fore.RED
            + "Please set your OpenAI API key in .env or as an environment variable."
            + Fore.RESET
        )
        print("You can get your key from https://platform.openai.com/account/api-keys")
        openai_api_key = input(
            "If you do have the key, please enter your OpenAI API key now:\n"
        )
        key_pattern = r"^sk-\w{48}"
        openai_api_key = openai_api_key.strip()
        if re.search(key_pattern, openai_api_key):
            os.environ["OPENAI_API_KEY"] = openai_api_key
            config.openai_api_key = openai_api_key
            print(
                Fore.GREEN
                + "OpenAI API key successfully set!\n"
                + Fore.YELLOW
                + "NOTE: The API key you've set is only temporary.\n"
                + "For longer sessions, please set it in .env file"
                + Fore.RESET
            )
        else:
            print("Invalid OpenAI API key!")
            exit(1)
