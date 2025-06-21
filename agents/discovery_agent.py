from core.logger import get_logger

logger = get_logger(__name__)

class DiscoveryAgent:
    def __init__(self, gemini_client):
        self.gemini_client = gemini_client

    def listen(self, user_input: str) -> dict:
        logger.info("Processing user input with Gemini")
        # TODO: Integrate with Gemini API for natural language understanding
        # Mock response example
        parsed_data = {"need": "financial aid", "details": user_input}
        logger.debug(f"Parsed user data: {parsed_data}")
        return parsed_data
