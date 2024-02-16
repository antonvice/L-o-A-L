# Imports
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel, Field
from typing import List, Optional

class LoawlConfig(BaseModel):
    openai_api_key: str = Field(default_factory=lambda: os.getenv("OPENAI_API_KEY"), env="OPENAI_API_KEY")
    max_tokens: int = 1024
    temperature: float = 0.7
    top_p: float = 1.0
    

class Loawl(BaseModel):
    config: LoawlConfig
    document: str
    abstraction_levels: Optional[List[str]] = Field(default_factory=list)
    client: OpenAI = Field(default_factory=OpenAI)
    
    class Config:
        arbitrary_types_allowed = True
        
    
    def __init__(self, **data):
        super().__init__(**data)
        # Initialize the OpenAI API key
        self.client.api_key = self.config.openai_api_key
        # create a dict to store texts


    def generate_abstraction(self, detail_level: int) -> str:
        """
        Generates an abstraction of the document at a specified detail level.

        Args:
            detail_level (int): A value that influences the level of detail in the generated abstraction.
                                Higher values generate more detailed text.

        Returns:
            str: The generated abstraction of the document.
        """
        # Setup OpenAI API
        OpenAI.api_key = self.config.openai_api_key

        # Adjust parameters based on detail level
        prompt = f"Summarize the following text with detail level {detail_level}:\n\n{self.document}"
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],  # prompt,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            top_p=self.config.top_p
        )

        # Extract and return the generated text

        abstraction = response.choices[0].message.content.strip()
        return abstraction

    def update_document_abstractions(self):
        """
        Updates the abstraction_levels list with different levels of document abstraction.
        """
        # Example abstraction levels: 1 (less detailed) to 5 (more detailed)
        self.abstraction_levels = [self.generate_abstraction(level) for level in range(1, 6)]
        
    def get_abstractions(self):
        return self.abstraction_levels

# Create an instance of LoawlConfig with the necessary configuration
config = LoawlConfig()


