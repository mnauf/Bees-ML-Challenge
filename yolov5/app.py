import gradio as gr
from sample_solution import main as detect_bees

badges = """
<div style="display: flex">
<span style="margin-right: 5px"> 
<a href="https://www.linkedin.com/in/mnauf/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/LinkedIn_Logo.svg/2560px-LinkedIn_Logo.svg.png" alt="Linkedin" width=100 height=auto> </a>
</span>
<span style="margin-right: 5px"> 
 <a href="https://github.com/mnauf/Bees-ML-Challenge" target="_blank"> <img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" alt="Github"> </a>
</span>
<span style="margin-right: 5px"> 
 <a href="https://twitter.com/MNaufil" target="_blank"> <img src="https://img.shields.io/badge/Twitter-%231DA1F2.svg?style=for-the-badge&logo=Twitter&logoColor=white" alt="Twitter"> </a>
</span>
</div>
"""

description="""Detect bees in the image"""
with gr.Blocks() as block:
    # gr.Markdown("""![Imgur](https://i.imgur.com/iPZlUa8.png)""")
    gr.HTML("<img src=https://i.imgur.com/mG2WSlK.png width=auto height=200>")
    gr.Markdown(badges)
    gr.Markdown(description)
    with gr.Row():
        file_input = gr.Image()
        file_output = gr.Image()

    btn = gr.Button(value="Count the number of Bees")
    btn.click(detect_bees, inputs=[file_input], outputs=[file_output], queue=True)

block.queue(concurrency_count=5).launch(server_name="localhost", share=True)
# block.queue().launch()