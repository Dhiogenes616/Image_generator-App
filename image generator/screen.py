import tkinter

import customtkinter as ctk
import os
import openai
import requests
from PIL import Image, ImageTk   #pip install pillow
import resource, io


# this function "generate" will interact with the bottton generate
def generate():
    openai.api_key = "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"
    user_prompt = prompt_entry.get("0.0", tkinter.END)
    user_prompt += "in style: " + style_dropdown.get()

    response = openai.Image.create(
        prompt=user_prompt,
        n=int(number_slider.get()),
        size="512x512"
    )

    image_urls = []
    for i in range(len(response['data'])):
        image_urls.append(response['data'][i]['url'])
    print(image_urls)

    images = []
    for url in image_urls:
        response = requests.get(url)
        image = Image.open(io.BytesIO(response.content))
        photo_image = ImageTk.PhotoImage(image)
        images.append(photo_image)

    def update_image(index=0):
        canvas.image = images[index]
        canvas.create_image(0, 0, anchor="nw", image=images[index])
        index = (index + 0) % len(images)
        canvas.after(3000, update_image, index)

    update_image()


root = ctk.CTk()
root.title("AI image generator")

ctk.set_appearance_mode('dark')

input_frame = ctk.CTkFrame(root)
input_frame.pack(side="left", expand="true", padx="20", pady="20")

# here text bottom
prompt_label = ctk.CTkLabel(input_frame, text="Prompt")
prompt_label.grid(row=0, column=0, pady="10", padx="10")

# here text box
prompt_entry = ctk.CTkTextbox(input_frame, height=10)
prompt_entry.grid(row="0", column="1" ,padx="10", pady="20")

# here create style bottom
style_label = ctk.CTkLabel(input_frame, text="Style")
style_label.grid(row="1", column="0", padx="10", pady="10")

# here we will create a card options
style_dropdown = ctk.CTkComboBox(input_frame, values=["Realistic", "Cartoon", "3D Illustration", "Flat Art"])
style_dropdown.grid(row=1, column=1, padx=10, pady=10)

# here we will create a slide options
number_label = ctk.CTkLabel(input_frame, text="# Images")
number_label.grid(row=2, column=0)
# here we are saying the number of image using the from= and to=
number_slider = ctk.CTkSlider(input_frame, from_=1, to=10, number_of_steps=9)
number_slider.grid(row=2, column=1)

# here we will create the generate button
generate_button = ctk.CTkButton(input_frame, text="Generate", command=generate)
generate_button.grid(row=3, column=0, columnspan=2, sticky="news", padx=10, pady=10)

# Now here we will put the canvas, for the image-box
canvas = tkinter.Canvas(root, width=512, height=512)
canvas.pack(side="left")

root.mainloop()

# image_url = response['data'][0]['url']
# print(image_url)
# response = requests.get(image_url)
# image = Image.open(io.BytesIO(response.content))
# image = ImageTk.PhotoImage(image)
#
# canvas.image = image
# canvas.create_image(0, 0, anchor="nw", image=image)
