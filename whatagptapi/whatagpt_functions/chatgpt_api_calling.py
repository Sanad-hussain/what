import frappe
import requests
import openai

@frappe.whitelist()
def chatgpt_api_calling(user_content, previous_content=None, system_content=None, model=None, max_tokens=None, temperature=None, id=None,):
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = "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"

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        #{"role": "system", "content": system_content },
        {"role": "assistant", "content": str(previous_content)},
        {"role": "user", "content": user_content}
      ]
    )
    return completion.choices[0].message.content