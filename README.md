# MuAPI Dify Plugin

A comprehensive Dify Tool Plugin that integrates **MuAPI** into Dify, enabling AI-powered image generation, video creation, audio production, image editing, and more — directly from Dify workflows, chatflows, and agents.

---

## Features

### Image Tools

* **Generate Image** — Create images from text prompts using AI models
* **Edit Image** — Transform existing images with text-guided editing
* **Remove Background** — Remove backgrounds to produce transparent images
* **Upscale Image** — Enhance image resolution with AI upscaling

### Video Tools

* **Generate Video** — Create videos from text prompts
* **Image to Video** — Animate static images into videos

### Audio Tools

* **Generate Audio** — Create music and audio from text descriptions
* **Remix Audio** — Transform existing audio with text-guided remixing

### Platform Features

* MuAPI API key credential management through Dify
* Real-time credential validation via API
* Rich Dify outputs (inline images, playable video/audio links)
* Support for 100+ AI models via MuAPI
* Configurable parameters per tool (model, dimensions, duration, etc.)

---

## Tech Stack

* Dify Plugin SDK
* Python 3.12
* MuAPI Python SDK
* Docker
* Dify Plugin Daemon

---

## Project Structure

```text
muapi-dify-plugin/
│
├── main.py
├── manifest.yaml
├── requirements.txt
│
├── provider/
│   ├── muapi.yaml
│   └── muapi_provider.py
│
├── tools/
│   ├── generate_image.py
│   ├── generate_image.yaml
│   ├── generate_video.py
│   ├── generate_video.yaml
│   ├── image_to_video.py
│   ├── image_to_video.yaml
│   ├── edit_image.py
│   ├── edit_image.yaml
│   ├── remove_background.py
│   ├── remove_background.yaml
│   ├── upscale_image.py
│   ├── upscale_image.yaml
│   ├── generate_audio.py
│   ├── generate_audio.yaml
│   ├── remix_audio.py
│   └── remix_audio.yaml
│
└── _assets/
    └── icon.png
```

---

## Installation

### Prerequisites

* Docker Desktop
* WSL2
* Dify (running instance)
* Python 3.12
* Go (required for packaging plugins)

---

### Clone Repository

```bash
git clone https://github.com/2005-ab/dify-plugin-muapi.git
cd dify-plugin-muapi
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

Requirements:

```txt
dify-plugin
git+https://github.com/SamurAIGPT/muapi-python.git
```

---

## Build Plugin Package

Navigate to the Dify Plugin Daemon repository:

```bash
cd dify-plugin-daemon
```

Package the plugin:

```bash
go run ./cmd/commandline plugin package <plugin-path>
```

Example:

```bash
go run ./cmd/commandline plugin package D:\dify\muapi-dify-plugin
```

Output:

```text
muapi-dify-plugin.difypkg
```

---

## Dify Configuration

### Disable Signature Verification (Development Only)

Edit:

```text
dify/docker/.env
```

Change:

```env
FORCE_VERIFYING_SIGNATURE=true
```

To:

```env
FORCE_VERIFYING_SIGNATURE=false
```

Restart Dify:

```bash
docker compose down
docker compose up -d
```

---

## Install Plugin

1. Open Dify
2. Navigate to **Plugins**
3. Click **Local Package File**
4. Upload:

```text
muapi-dify-plugin.difypkg
```

---

## Configure Credentials

After installation:

1. Open MuAPI Plugin
2. Configure Provider Credentials
3. Enter your **MuAPI API Key**
4. Save configuration

The plugin validates your API key by calling the MuAPI account balance endpoint. If the key is invalid, you will see a credential validation error.

Get your API key from: [https://muapi.ai/dashboard](https://muapi.ai/dashboard)

---

## Available Tools

### Generate Image

Create images from text prompts.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| prompt | string | Yes | — | Text prompt describing the image |
| model | string | No | flux-dev | Image generation model |
| width | number | No | 1024 | Width in pixels |
| height | number | No | 1024 | Height in pixels |
| num_images | number | No | 1 | Number of images to generate |

---

### Generate Video

Create videos from text prompts.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| prompt | string | Yes | — | Text prompt describing the video |
| model | string | No | kling-master | Video generation model |
| duration | number | No | 5 | Duration in seconds |
| aspect_ratio | string | No | 16:9 | Aspect ratio |

---

### Image to Video

Animate a static image into a video.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| image | string | Yes | — | URL of the source image |
| prompt | string | Yes | — | Animation description |
| model | string | No | kling-std | Image-to-video model |
| duration | number | No | 5 | Duration in seconds |
| aspect_ratio | string | No | 16:9 | Aspect ratio |

---

### Edit Image

Transform existing images with text-guided editing.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| image | string | Yes | — | URL of the source image |
| prompt | string | Yes | — | Edit description |
| model | string | No | flux-kontext-dev | Image editing model |
| aspect_ratio | string | No | — | Output aspect ratio |

---

### Remove Background

Remove the background from an image.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| image | string | Yes | — | URL of the source image |
| model | string | No | bria-rmbg | Background removal model |

---

### Upscale Image

Enhance image resolution.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| image | string | Yes | — | URL of the image to upscale |
| scale_factor | number | No | 2 | Upscale factor (e.g. 2 for 2x) |
| model | string | No | aura-sr | Upscaling model |

---

### Generate Audio

Create music or audio from text descriptions.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| prompt | string | Yes | — | Audio/music description |
| title | string | No | — | Track title |
| tags | string | No | — | Genre/style tags |
| instrumental | boolean | No | false | Instrumental only |

---

### Remix Audio

Transform existing audio with text-guided remixing.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| audio | string | Yes | — | URL of the audio to remix |
| prompt | string | Yes | — | Remix description |
| title | string | No | — | Track title |
| tags | string | No | — | Genre/style tags |

---

## Example Workflows

### Image Generation

```text
User Input → Generate Image → Output Image
```

Example prompt:

```text
A futuristic city at sunset with flying cars
```

### Video from Text

```text
User Input → Generate Video → Output Video Link
```

Example prompt:

```text
A drone flying over a mountain landscape at golden hour
```

### Image to Video

```text
Upload Image → Image to Video → Output Video Link
```

### Image Editing Pipeline

```text
Generate Image → Edit Image → Upscale Image → Output
```

### Background Removal

```text
Upload Image → Remove Background → Output Transparent Image
```

### Music Generation

```text
User Input → Generate Audio → Output Audio Link
```

Example prompt:

```text
A chill lo-fi beat with soft piano and rain sounds
```

---

## Example Output

### Image Output

```json
{
  "files": [
    {
      "extension": ".avif",
      "filename": "generated-image.avif"
    }
  ]
}
```

### Video Output

```json
{
  "video": "https://cdn.muapi.ai/videos/example-output.mp4"
}
```

### Audio Output

```json
{
  "audio": "https://cdn.muapi.ai/audio/example-output.mp3"
}
```

---

## Screenshots

<!-- Add screenshots of each tool in the Dify UI here -->

### Plugin Installation

_Screenshot placeholder: Plugin installed in Dify_

### Credential Configuration

_Screenshot placeholder: MuAPI API key configuration_

### Image Generation Workflow

_Screenshot placeholder: Image generation workflow in Dify_

### Video Generation Workflow

_Screenshot placeholder: Video generation workflow in Dify_

### Audio Generation Workflow

_Screenshot placeholder: Audio generation workflow in Dify_

---

## Verified Working Flow

```text
Dify Workflow
      ↓
MuAPI Tool
      ↓
MuAPI SDK
      ↓
MuAPI API
      ↓
Generated Output
      ↓
Returned to Dify
```

Status:

```text
✅ Plugin Packaging
✅ Plugin Installation
✅ Credential Configuration
✅ Credential Validation (API verification)
✅ Image Generation
✅ Image Editing
✅ Background Removal
✅ Image Upscaling
✅ Video Generation
✅ Image to Video
✅ Audio Generation
✅ Audio Remix
✅ Image Delivery to Dify
✅ Video Link Delivery to Dify
✅ Audio Link Delivery to Dify
```

---

## Development

### Adding New Tools

1. Create `tools/<tool_name>.py` with a class extending `Tool`
2. Create `tools/<tool_name>.yaml` with Dify tool schema
3. Register in `provider/muapi.yaml` under `tools:`
4. Repackage and reinstall the plugin

### Tool YAML Schema

Every tool parameter must include:

```yaml
human_description:
  en_US: ...
llm_description: ...
form: llm  # or form
```

Every tool must include:

```yaml
extra:
  python:
    source: tools/<tool>.py
```

---

## License

MIT License

---

Built using:

* Dify Plugin SDK
* MuAPI
* Docker
* Python
