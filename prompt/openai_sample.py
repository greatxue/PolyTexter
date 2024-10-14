from utils.openai import client

def ques_gpt(prompt="Hi, how do you do today?"):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
    )
    if response.choices[0]:
        return response
    else:
        print('No valid GPT-response generated.')

if __name__ == "__main__":
    response = ques_gpt()
    gpt_ans = response.choices[0].message.content.strip()
    print(gpt_ans)