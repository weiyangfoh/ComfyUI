import random
import json
import requests

# List of positive prompts (1 for each image)
positive_prompts = [
    "A stunningly beautiful Malay princess stands alone in a quiet forest during golden hour, her long dark hair flowing gently in the breeze. Her refined facial features are elegant and noble, with expressive eyes that glow in the soft backlight. She wears a full-length traditional royal Malay dress made of layered songket fabric with intricate golden embroidery and long sleeves. A translucent kain lepas flows from her shoulders, trailing softly in the wind. Her accessories include a fine golden pendant, subtle earrings, and a royal crest brooch. She stands with grace and quiet strength, her face serene and composed. The background is inspired by Makoto Shinkai’s cinematic lighting, with sunrays filtering through tall tropical trees. Highly detailed, soft lighting, clean anime-style linework.",
    "Anime style, wide shot of the Melaka Sultanate Palace from a distance, majestic traditional Malay wooden architecture, large multi-tiered roof with curved eaves, golden carvings and red-brown wood tones, palace surrounded by tropical trees and clear blue sky, sunlight illuminating the palace roof, peaceful and regal atmosphere, no people in view, cinematic composition, detailed scenery, lush green landscape, grand historical building, sharp anime outlines, beautiful harmony of nature and architecture",
    "Studio Ghibli style, very old Malay woman walking slowly through a quiet tropical rainforest, hunched back, deeply wrinkled face, small tired eyes, white hair tied in a bun, modest faded batik sarong and long-sleeved kebaya, holding a wooden cane, soft painterly shading, inspired by the old Sophie in Howl’s Moving Castle, calm and wise expression, cinematic forest light, lush green foliage, peaceful atmosphere",
    "a golden bowl filled with thick dark red blood, resting on green forest grass, a few drops of blood have spilled beside the bowl, the liquid reflects sunlight naturally, surrounded by soft shadows from nearby leaves, no people, anime cinematic style, high realism, soft lighting, studio ghibli and violet evergarden inspired, ultra detailed, masterpiece"
]

# Corresponding negative prompts for each image
negative_prompts = [
    "childlike, baby face, cartoon, ghost, elf, modern fashion, short skirt, hoodie, sci-fi armor, glowing effect, cropped, multiple people, blurry face, glitch, deformed, chibi, text, watermark",
    "blurry, deformed, modern buildings, sci-fi, futuristic, glowing structures, people, fantasy, floating palace, surreal, ruins, horror, extra objects, chaotic background, elves",
    "young woman, teenager, sexy, revealing clothes, anime girl, big eyes, smooth skin, fashionable, cute, short skirt, tight dress, fantasy creature, glowing effects, vibrant colors, large bust, exaggerated curves",
    "golden liquid, glowing blood, purple blood, magical aura, fantasy, lowres, blurry, sketch, surreal, floating, concept art, character, people, pink blood, golden blood, unrealistic"
]

# Short narration for each image
narration = [
    "In the golden forest, a royal figure stands in silence, her gaze distant as if hearing ancient whispers.",
    "Far away, the grand palace of Melaka rises proudly under the morning sun, untouched by time.",
    "Deep in the jungle, an old woman walks slowly, holding secrets older than the trees around her.",
    "A golden bowl rests gently on the grass, its blood-red contents shimmering beneath the leaves."
]

# Template for a single ComfyUI prompt request
workflow_template = {
    "prompt": {
        "1": {"inputs": {"ckpt_name": "Illustrious-XL-v0.1-GUIDED (1).safetensors"}, "class_type": "CheckpointLoaderSimple"},
        "3": {"inputs": {"text": "", "clip": ["1", 1]}, "class_type": "CLIPTextEncode"},
        "5": {"inputs": {"text": "", "clip": ["1", 1]}, "class_type": "CLIPTextEncode"},
        "9": {"inputs": {"width": 768, "height": 1152, "batch_size": 1}, "class_type": "EmptyLatentImage"},
        "2": {
            "inputs": {
                "seed": 0,
                "steps": 35,
                "cfg": 7,
                "sampler_name": "dpmpp_2m",
                "scheduler": "karras",
                "denoise": 1.0,
                "model": ["1", 0],
                "positive": ["3", 0],
                "negative": ["5", 0],
                "latent_image": ["9", 0]
            },
            "class_type": "KSampler",
            "widgets_values": [0, "randomize", 35, 7, "dpmpp_2m", "karras", 1.0]
        },
        "6": {"inputs": {"samples": ["2", 0], "vae": ["1", 2]}, "class_type": "VAEDecode"},
        "10": {"inputs": {"images": ["6", 0], "filename_prefix": "puteri"}, "class_type": "SaveImage"}
    }
}

# ComfyUI API server URL
url = "http://127.0.0.1:8188/prompt"

# Repeat generation loop
keep_generating = True
while keep_generating:
    for i in range(4):
        print(f"\n▶️ Generating image {i+1}/4")
        print(f"📖 Story {i+1}: {narration[i]}")
        
        # Clone the workflow template (deep copy)
        workflow = json.loads(json.dumps(workflow_template))

        # Insert positive and negative prompts
        workflow["prompt"]["3"]["inputs"]["text"] = positive_prompts[i]
        workflow["prompt"]["5"]["inputs"]["text"] = negative_prompts[i]

        # Generate a random seed and insert into prompt
        seed = random.randint(1, 4294967295)
        workflow["prompt"]["2"]["inputs"]["seed"] = seed
        workflow["prompt"]["2"]["widgets_values"][0] = seed

        # Set filename prefix
        workflow["prompt"]["10"]["inputs"]["filename_prefix"] = f"puteri_{i+1}"

        # Send the prompt to ComfyUI
        response = requests.post(url, json=workflow)
        if response.ok:
            print(f"✅ Image {i+1} submitted successfully (seed: {seed})")
        else:
            print(f"❌ Failed to submit image {i+1}: {response.status_code}")
            print(response.text)

    # Ask the user whether to generate more
    user_input = input("\n🌀 Do you want to generate another set of 4 images? (yes/no): ").strip().lower()
    if user_input != "yes":
        keep_generating = False
