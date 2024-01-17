import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
# STREAMLIT IMPORTS
import streamlit as st


# Our Host URL should not be prepended with "https" nor should it have a trailing slash.
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

# Sign up for an account at the following link to get an API Key.
# https://platform.stability.ai/

# Click on the following link once you have created an account to be taken to your API Key.
# https://platform.stability.ai/account/keys

# Paste your API Key below.

os.environ['STABILITY_KEY'] = 'sk-MiKZjA7Vfnn834Ao22H69BTNSONeKXgXJbd7yF0NpLMNKWj4'


# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], # API Key reference.
    verbose=True, # Print debug messages.
    engine="stable-diffusion-xl-1024-v1-0", # Set the engine to use for generation.
    # Check out the following link for a list of available engines: https://platform.stability.ai/docs/features/api-parameters#engine
)

st.title("FOMO.AI alpha testing tool Stable Diffusion API")
st.write("This app uses several inputs to generate an image using Stable Diffusion API models. ")

with st.form("user_inputs"):
    prompt = st.text_input("Prompt (Insert your prompt here to generate an image.)")
    seed = st.number_input("Seed", min_value=0, max_value=2147483647, value=42, step=1)
    st.write("If a seed is provided, the resulting generated image will be deterministic.")
    st.write("What this means is that as long as all generation parameters remain the same, you can always recall the same image simply by generating it again.")
    steps = st.number_input("Steps", min_value=1, max_value=150, value=50, step=1)
    st.write("Amount of inference steps performed on image generation. Defaults to 30. ")
    cfg_scale = st.number_input("CFG Scale", min_value=1.0, max_value=30.0, value=8.0, step=0.5)
    st.write("Influences how strongly your generation is guided to match your prompt.")
    st.write("Setting this value higher increases the strength in which it tries to match your prompt.")
    st.write("Defaults to 7.0 if not specified.")
    width = st.number_input("Width", min_value=256, max_value=2048, value=512, step=64)
    st.write("Generation width, defaults to 512 if not included.")
    height = st.number_input("Height", min_value=256, max_value=2048, value=512, step=64)
    st.write("Generation height, defaults to 512 if not included.")
    samples = st.number_input("Samples", min_value=1, max_value=4, value=1, step=1)
    st.write("Number of images to generate, defaults to 1 if not included.")
    # sampler = st.selectbox("Sampler", ("ddim", "plms", "k_euler", "k_euler_ancestral", "k_heun", "k_dpm_2", "k_dpm_2_ancestral", "k_dpmpp_2s_ancestral", "k_lms", "k_dpmpp_2m", "k_dpmpp_sde"))
    # st.write("Choose which sampler we want to denoise our generation with.")
    # st.write("Defaults to k_dpmpp_2m if not specified. Clip Guidance only supports ancestral samplers.")
    # st.write("Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m, k_dpmpp_sde")
    submit_button = st.form_submit_button(label="Generate")


# Set up our initial generation parameters.
answers = stability_api.generate(
    prompt=prompt,
    seed=seed, # Note: This isn't quite the case for Clip Guided generations, which we'll tackle in a future example notebook.
    steps=steps,
    cfg_scale=cfg_scale, # Influences how strongly your generation is guided to match your prompt.
                   # Setting this value higher increases the strength in which it tries to match your prompt.
                   # Defaults to 7.0 if not specified.
    width=width, # Generation width, defaults to 512 if not included.
    height=height, # Generation height, defaults to 512 if not included.
    samples=samples, # Number of images to generate, defaults to 1 if not included.
    sampler=generation.SAMPLER_K_DPMPP_2M # Choose which sampler we want to denoise our generation with.
                                                 # Defaults to k_dpmpp_2m if not specified. Clip Guidance only supports ancestral samplers.
                                                 # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m, k_dpmpp_sde)
)

# Set up our warning to print to the console if the adult content classifier is tripped.
# If adult content classifier is not tripped, save generated images.
for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again.")
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            # display img on streamlit
            st.image(img, caption=f"Seed: {artifact.seed}")

            # img.save(str(artifact.seed)+ ".png") # Save our generated images with their seed number as the filename.

