import openai
import os

def generate_blog_post(keyword):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    prompt = f"""
    Write a detailed blog post about '{keyword}'. 
    Include an introduction, several headings, and a conclusion. 
    Use the following placeholders for affiliate links: 
    {{AFF_LINK_1}}, {{AFF_LINK_2}}, {{AFF_LINK_3}}.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=800,
        n=1,
        stop=None,
        temperature=0.7,
    )

    blog_post = response.choices[0].text.strip()
    
    # Replace placeholders with dummy URLs
    blog_post = blog_post.replace("{{AFF_LINK_1}}", "https://dummyurl.com/1")
    blog_post = blog_post.replace("{{AFF_LINK_2}}", "https://dummyurl.com/2")
    blog_post = blog_post.replace("{{AFF_LINK_3}}", "https://dummyurl.com/3")

    return blog_post