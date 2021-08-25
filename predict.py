import dotenv
dotenv.load_dotenv()

import commands
commandmap = {
    "currency": commands.currency,
    "translate": commands.translate
}

def predict(message:str):
    from google.cloud import dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path("mcs-vf-xn9a", "blank_session")
    text_input = dialogflow.TextInput(text=message, language_code="en")
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    response_text = response.query_result.fulfillment_text
    if not response_text.startswith("cmd::"):
        return response_text
    args = response_text.split(" ")
    command = args[0][5:]
    command_args = args[1:]
    return run_command(command, command_args)

def run_command(command:str, args:list[str]):
    return commandmap[command](*args)