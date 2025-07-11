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
# Installing

## Windows Portable

There is a portable standalone build for Windows that should work for running on Nvidia GPUs or for running on your CPU only on the [releases page](https://github.com/comfyanonymous/ComfyUI/releases).

### [Direct link to download](https://github.com/comfyanonymous/ComfyUI/releases/latest/download/ComfyUI_windows_portable_nvidia.7z)

Simply download, extract with [7-Zip](https://7-zip.org) and run. Make sure you put your Stable Diffusion checkpoints/models (the huge ckpt/safetensors files) in: ComfyUI\models\checkpoints

If you have trouble extracting it, right click the file -> properties -> unblock

#### How do I share models between another UI and ComfyUI?

See the [Config file](extra_model_paths.yaml.example) to set the search paths for models. In the standalone windows build you can find this file in the ComfyUI directory. Rename this file to extra_model_paths.yaml and edit it with your favorite text editor.

## Jupyter Notebook

To run it on services like paperspace, kaggle or colab you can use my [Jupyter Notebook](notebooks/comfyui_colab.ipynb)


## [comfy-cli](https://docs.comfy.org/comfy-cli/getting-started)

You can install and start ComfyUI using comfy-cli:
```bash
pip install comfy-cli
comfy install
```

## Manual Install (Windows, Linux)

python 3.13 is supported but using 3.12 is recommended because some custom nodes and their dependencies might not support it yet.

Git clone this repo.

Put your SD checkpoints (the huge ckpt/safetensors files) in: models/checkpoints

Put your VAE in: models/vae


### AMD GPUs (Linux only)
AMD users can install rocm and pytorch with pip if you don't have it already installed, this is the command to install the stable version:

```pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.3```

This is the command to install the nightly with ROCm 6.4 which might have some performance improvements:

```pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.4```

### Intel GPUs (Windows and Linux)

(Option 1) Intel Arc GPU users can install native PyTorch with torch.xpu support using pip (currently available in PyTorch nightly builds). More information can be found [here](https://pytorch.org/docs/main/notes/get_start_xpu.html)
  
1. To install PyTorch nightly, use the following command:

```pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/xpu```

2. Launch ComfyUI by running `python main.py`


(Option 2) Alternatively, Intel GPUs supported by Intel Extension for PyTorch (IPEX) can leverage IPEX for improved performance.

1. For Intel® Arc™ A-Series Graphics utilizing IPEX, create a conda environment and use the commands below:

```
conda install libuv
pip install torch==2.3.1.post0+cxx11.abi torchvision==0.18.1.post0+cxx11.abi torchaudio==2.3.1.post0+cxx11.abi intel-extension-for-pytorch==2.3.110.post0+xpu --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/ --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/cn/
```

For other supported Intel GPUs with IPEX, visit [Installation](https://intel.github.io/intel-extension-for-pytorch/index.html#installation?platform=gpu) for more information.

Additional discussion and help can be found [here](https://github.com/comfyanonymous/ComfyUI/discussions/476).

### NVIDIA

Nvidia users should install stable pytorch using this command:

```pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu128```

This is the command to install pytorch nightly instead which might have performance improvements.

```pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128```

#### Troubleshooting

If you get the "Torch not compiled with CUDA enabled" error, uninstall torch with:

```pip uninstall torch```

And install it again with the command above.

### Dependencies

Install the dependencies by opening your terminal inside the ComfyUI folder and:

```pip install -r requirements.txt```

After this you should have everything installed and can proceed to running ComfyUI.

### Others:

#### Apple Mac silicon

You can install ComfyUI in Apple Mac silicon (M1 or M2) with any recent macOS version.

1. Install pytorch nightly. For instructions, read the [Accelerated PyTorch training on Mac](https://developer.apple.com/metal/pytorch/) Apple Developer guide (make sure to install the latest pytorch nightly).
1. Follow the [ComfyUI manual installation](#manual-install-windows-linux) instructions for Windows and Linux.
1. Install the ComfyUI [dependencies](#dependencies). If you have another Stable Diffusion UI [you might be able to reuse the dependencies](#i-already-have-another-ui-for-stable-diffusion-installed-do-i-really-have-to-install-all-of-these-dependencies).
1. Launch ComfyUI by running `python main.py`

> **Note**: Remember to add your models, VAE, LoRAs etc. to the corresponding Comfy folders, as discussed in [ComfyUI manual installation](#manual-install-windows-linux).

#### DirectML (AMD Cards on Windows)

This is very badly supported and is not recommended. There are some unofficial builds of pytorch ROCm on windows that exist that will give you a much better experience than this. This readme will be updated once official pytorch ROCm builds for windows come out.

```pip install torch-directml``` Then you can launch ComfyUI with: ```python main.py --directml```

#### Ascend NPUs

For models compatible with Ascend Extension for PyTorch (torch_npu). To get started, ensure your environment meets the prerequisites outlined on the [installation](https://ascend.github.io/docs/sources/ascend/quick_install.html) page. Here's a step-by-step guide tailored to your platform and installation method:

1. Begin by installing the recommended or newer kernel version for Linux as specified in the Installation page of torch-npu, if necessary.
2. Proceed with the installation of Ascend Basekit, which includes the driver, firmware, and CANN, following the instructions provided for your specific platform.
3. Next, install the necessary packages for torch-npu by adhering to the platform-specific instructions on the [Installation](https://ascend.github.io/docs/sources/pytorch/install.html#pytorch) page.
4. Finally, adhere to the [ComfyUI manual installation](#manual-install-windows-linux) guide for Linux. Once all components are installed, you can run ComfyUI as described earlier.

#### Cambricon MLUs

For models compatible with Cambricon Extension for PyTorch (torch_mlu). Here's a step-by-step guide tailored to your platform and installation method:

1. Install the Cambricon CNToolkit by adhering to the platform-specific instructions on the [Installation](https://www.cambricon.com/docs/sdk_1.15.0/cntoolkit_3.7.2/cntoolkit_install_3.7.2/index.html)
2. Next, install the PyTorch(torch_mlu) following the instructions on the [Installation](https://www.cambricon.com/docs/sdk_1.15.0/cambricon_pytorch_1.17.0/user_guide_1.9/index.html)
3. Launch ComfyUI by running `python main.py`



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
