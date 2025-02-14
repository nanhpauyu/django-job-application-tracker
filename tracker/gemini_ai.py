from google import genai
import os


def get_information(text):
    try:
        client = genai.Client(api_key=os.getenv('API_KEY_G'))
        question = f'''Give me
        Job Title
        Job Location (only city and state if not mention as USA)
        remote or hybrid or onsite (just in one word)
        compensation min and max (calculate and estimate in per year)
        company name
        fetch job description
            Project
            Responsibilities
            Qualifications
            Benefits
        from {text}. In this format
        Title =
        Location =
        remote or hybrid =
        compensation =
        company =
        '''
        response = client.models.generate_content(
        model="gemini-2.0-flash", contents=question
        )
        return response.text
    except Exception as e:
        return e