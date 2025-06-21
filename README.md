# 🌄 Auto Image Generator – Puteri Gunung Ledang

This Python script is part of a digital storytelling project based on the Malaysian legend of **Puteri Gunung Ledang**, reimagined through AI-generated anime-style visuals using **ComfyUI**.

---

## 🧝‍♀️ About the Project

This project presents a modern artistic retelling of *Puteri Gunung Ledang*, the mystical Malay princess of Mount Ophir.  
We generated **4 high-quality anime-style images** that represent key scenes in the story, using a shared workflow template and **randomized seeds**.

- 📖 Narration is stored in `story.txt`  
- 🎨 Text prompts are stored in `prompts.txt`  

---

## 🎥 Final Showcase

📎 *Watch the final video here 
https://youtu.be/LRnxm0dGxL8?si=xPEkrBBpzfSXWNgZ

---

## 👥 Team Info

- **Team Name**: Hello Kitty  
- **Competition**: Young Digital Innovators (Python Category)  
- **GitHub Repo**: [https://github.com/PenangScienceCluster/python2025](https://github.com/PenangScienceCluster/python2025)

---

## 🛠 Tools & Resources

### 🎨 Image Generation:
- **ComfyUI**  
  → https://github.com/comfyanonymous/ComfyUI

- **Model Used**: *Illustrious-XL v0.1 (GUIDED)*  
  Trained by Onoma AI  
  Download:  
  [HuggingFace Link](https://huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0/blob/main/Illustrious-XL-v0.1-GUIDED.safetensors)

### ✂️ Video Editing:
- 必剪（BiJian）

---

## ⚙️ Project Highlights

- ✅ Built using **Python 3.12**
- 📂 Uses **ComfyUI prompt-style workflow** (not full graph .json)
- 🔄 Automatically injects:
  - Positive prompt (from `prompts.txt`)
  - Negative prompt (predefined list)
  - Random seed per image
  - Filename prefix (`puteri_1`, `puteri_2`, etc.)
- 📤 Sends prompt JSON to local ComfyUI API (`http://127.0.0.1:8188`)
- 💾 Saves results in ComfyUI’s `/output/` folder

---

## ✅ Requirements

- Python 3.12+
- ComfyUI installed and running locally on `http://127.0.0.1:8188`
- Illustrious-XL model placed in `ComfyUI/models/checkpoints`

Install dependencies:
```bash
pip install requests
```

---


## ▶️ How to Use

1. **Start ComfyUI**
   - Make sure ComfyUI is running locally on `http://127.0.0.1:8188`.

2. **Checkpoints & Settings**
   - Confirm that the following model is installed and available:
     ```
     Illustrious-XL-v0.1-GUIDED (1).safetensors
     ```
   - Resolution used: `768x1152`

3. **Run the script**
   ```bash
   python main.py
