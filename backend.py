import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

def generate_job_description(prompt):
    """
    Generate a job description using the Gemini API
    
    Args:
        prompt (str): The job description prompt
        
    Returns:
        str: The generated job description
    """
    try:
        # Get the Gemini Pro model
        model = genai.GenerativeModel('gemini-pro')
        
        # Enhanced prompt for better job descriptions
        enhanced_prompt = f"""
        As an expert HR consultant, create a comprehensive and professional job description based on the following details:
        
        {prompt}
        
        The job description should include:
        1. A concise company introduction (fictional if no company details provided)
        2. A compelling overview of the role
        3. Detailed responsibilities
        4. Required skills and qualifications
        5. Preferred qualifications (if applicable)
        6. Benefits and perks
        7. Equal opportunity employer statement
        
        Format the response with proper headings and bullet points for easy readability.
        """
        
        # Generate the job description
        response = model.generate_content(enhanced_prompt)
        
        # Return the text content
        return response.text
    
    except Exception as e:
        # Log the error and raise it
        print(f"Error generating job description: {str(e)}")
        raise Exception(f"Failed to generate job description: {str(e)}")
    