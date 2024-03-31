<h1 align="center">Self-Operating Computer Framework</h1>

<p align="center">
  <strong>A framework to enable multimodal models to operate a computer.</strong>
</p>
<p align="center">
  Using the same inputs and outputs as a human operator, the model views the screen and decides on a series of mouse and keyboard actions to reach an objective. 
</p>

<div align="center">
  <img src="https://github.com/OthersideAI/self-operating-computer/blob/main/readme/self-operating-computer.png" width="750"  style="margin: 10px;"/>
</div>

<!--
:rotating_light: **OUTAGE NOTIFICATION: gpt-4-vision-preview**
**This model is currently experiencing an outage so the self-operating computer may not work as expected.**
-->


## Key Features
- **Compatibility**: Designed for various multimodal models.
- **Integration**: Currently integrated with **GPT-4v, Gemini Pro Vision, LLaVa, and Claude 3**.
- **Future Plans**: Support for additional models.

## Ongoing Development
At [HyperwriteAI](https://www.hyperwriteai.com/), we are developing Agent-1-Vision, a multimodal model with more accurate click location predictions.

## Agent-1-Vision Model API Access
We will soon be offering API access to our Agent-1-Vision model.

If you're interested in gaining access to this API, sign up [here](https://othersideai.typeform.com/to/FszaJ1k8?typeform-source=www.hyperwriteai.com).

## Demo

https://github.com/OthersideAI/self-operating-computer/assets/42594239/9e8abc96-c76a-46fb-9b13-03678b3c67e0


## Run `Self-Operating Computer`

1. **Install the project**
```
pip install self-operating-computer
```
2. **Run the project**
```
operate
```
3. **Enter your API keys**: If you don't have them, you can obtain the necessary API keys from the following sources:
   - OpenAI: [Get an OpenAI API key](https://platform.openai.com/account/api-keys)
   - Google AI Studio: [Get a Google AI Studio API key](https://makersuite.google.com/app/apikey)
   - Anthropic (for Claude 3): [Get a Claude API key](https://console.anthropic.com/dashboard)

<div align="center">
  <img src="https://github.com/OthersideAI/self-operating-computer/blob/main/readme/key.png" width="300"  style="margin: 10px;"/>
</div>

4. **Give Terminal app the required permissions**: As a last step, the Terminal app will ask for permission for "Screen Recording" and "Accessibility" in the "Security & Privacy" page of Mac's "System Preferences".

<div align="center">
  <img src="https://github.com/OthersideAI/self-operating-computer/blob/main/readme/terminal-access-1.png" width="300"  style="margin: 10px;"/>
  <img src="https://github.com/OthersideAI/self-operating-computer/blob/main/readme/terminal-access-2.png" width="300"  style="margin: 10px;"/>
</div>

## Using `operate` Modes

### Multimodal Models  `-m`
The Self-Operating Computer Framework supports several multimodal models:

#### GPT-4 with Vision `-m gpt-4-with-ocr`
This mode integrates Optical Character Recognition (OCR) capabilities, allowing GPT-4 to interact with on-screen elements by text.

#### GPT-4 with Set-of-Mark Prompting `-m gpt-4-with-som`
This mode uses the Set-of-Mark (SoM) Prompting method to enhance the visual grounding capabilities of GPT-4.

#### Gemini Pro Vision `-m gemini-pro-vision`
Use Google's Gemini Pro Vision model to operate the computer.

#### Claude 3 `-m claude-3`
Use Anthropic's Claude 3 model with Vision to see how it performs.

#### LLaVa `-m llava`
Use the LLaVa model hosted through Ollama to experiment with the Self-Operating Computer Framework.

### Voice Mode `--voice`
The framework supports voice inputs for the objective. Follow the instructions in the "Voice Mode" section to set it up.

### Optical Character Recognition Mode `-m gpt-4-with-ocr`
The Self-Operating Computer Framework now integrates Optical Character Recognition (OCR) capabilities with the `gpt-4-with-ocr` mode.

### Set-of-Mark Prompting `-m gpt-4-with-som`
The Self-Operating Computer Framework now supports Set-of-Mark (SoM) Prompting with the `gpt-4-with-som` command.

## Contributions are Welcomed!:

If you want to contribute yourself, see [CONTRIBUTING.md](https://github.com/OthersideAI/self-operating-computer/blob/main/CONTRIBUTING.md).

## Feedback

For any input on improving this project, feel free to reach out to [Josh](https://twitter.com/josh_bickett) on Twitter. 

## Join Our Discord Community

For real-time discussions and community support, join our Discord server. 
- If you're already a member, join the discussion in [#self-operating-computer](https://discord.com/channels/877638638001877052/1181241785834541157).
- If you're new, first [join our Discord Server](https://discord.gg/YqaKtyBEzM) and then navigate to the [#self-operating-computer](https://discord.com/channels/877638638001877052/1181241785834541157).

## Follow HyperWriteAI for More Updates

Stay updated with the latest developments:
- Follow HyperWriteAI on [Twitter](https://twitter.com/HyperWriteAI).
- Follow HyperWriteAI on [LinkedIn](https://www.linkedin.com/company/othersideai/).

## Compatibility
- This project is compatible with Mac OS, Windows, and Linux (with X server installed).

## OpenAI Rate Limiting Note
The ```gpt-4-vision-preview``` model is required. To unlock access to this model, your account needs to spend at least \$5 in API credits. Pre-paying for these credits will unlock access if you haven't already spent the minimum \$5.   
Learn more **[here](https://platform.openai.com/docs/guides/rate-limits?context=tier-one)**