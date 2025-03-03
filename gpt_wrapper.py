import openai
import os

class GPTWrapper:
    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        # Use the provided API key or fall back to an environment variable
        if api_key is None:
            api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("An OpenAI API key must be provided.")
        openai.api_key = api_key
        self.model = model

    def generate_insight(self, prompt, temperature=0.5, max_tokens=150):
        """
        Generates a GPT response based on the provided prompt.
        
        Args:
            prompt (str): The prompt to send to GPT.
            temperature (float): Sampling temperature for creativity (default 0.5).
            max_tokens (int): Maximum tokens in the response (default 150).
        
        Returns:
            str: The generated text from GPT.
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an AI assistant that provides insightful analytics summaries."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=max_tokens
            )
            # Extract and return the response text
            message = response['choices'][0]['message']['content'].strip()
            return message
        except Exception as e:
            print("Error generating insight:", e)
            return None

# Example usage:
if __name__ == "__main__":
    # Replace with your actual API key or set the OPENAI_API_KEY environment variable
    api_key = "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"
    wrapper = GPTWrapper(api_key=api_key)
    
    # Example prompt for generating an insight
    prompt = "Summarize the key trends in monthly sales data for our company."
    insight = wrapper.generate_insight(prompt)
    print("Generated Insight:\n", insight)