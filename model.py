from transformers import pipeline
from openai import OpenAI
from diffusers import DiffusionPipeline

def img2text(imgURL):
    img_to_text_pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
    text = img_to_text_pipe(imgURL)[0]["generated_text"]
    return text

def textGeneration(msg):
    client = OpenAI()

    msg_list = [{"role": "system", "content": "You are an expert short story teller. Using a simple narrative you generate story in less than 100 words based on the given scenario."}]
    msg_list.append(msg)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        max_completion_tokens= 200,
        messages= msg_list,
    )

    out_message = response.choices[0].message.content
    return(out_message)

def runModels(url):
    scenario = img2text(url)
    message = {"role": "user", "content": scenario}
    story = textGeneration(message)
    return([scenario,story])

def text2img(url):
    result = runModels(url)
    
    text_to_image_pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0")
    # text_to_image_pipe.to("cuda")

    prompt = result[1]
    generatedImage = text_to_image_pipe(prompt).images[0]
    generatedImage.save("static/generated_image.png")
    print("Image generated and saved.")
    return "static/generated_image.png"
