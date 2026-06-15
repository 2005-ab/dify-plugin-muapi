# MuAPI Dify Plugin

A custom Dify Tool Plugin that integrates **MuAPI** into Dify, enabling image generation directly from Dify workflows, chatflows, and agents.

## Features

### Current Features

* Generate images using MuAPI
* Configure MuAPI API key through Dify credentials
* Return generated images directly into Dify
* Support custom prompts
* Configurable image generation parameters:

  * Model
  * Width
  * Height
  * Number of Images

### Planned Features

* Video Generation
* Image Editing
* Background Removal
* Image Upscaling
* Audio Generation
* Audio Remix
* Model Discovery

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
│   └── generate_image.yaml
│
└── _assets/
```

---

## Installation

### Prerequisites

* Docker Desktop
* WSL2
* Dify
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
3. Enter:

```text
MUAPI API Key
```

Save configuration.

---

## Usage

### Generate Image

Add the **Generate Image** tool to a workflow.

Example prompt:

```text
A futuristic city at sunset with flying cars
```

Example workflow:

```text
User Input
      ↓
Generate Image
      ↓
Output Image
```

---

## Example Output

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

---

## Development Journey

During development the following issues were resolved:

### Environment Issues

* Docker Desktop not starting
* WSL2 not configured
* Hypervisor disabled (`hypervisorlaunchtype Off`)
* Virtual Machine Platform configuration

### Dify Plugin Issues

* Invalid plugin identifier
* Plugin signature verification
* Missing provider metadata
* Missing YAML schema fields
* Incorrect plugin bootstrap
* Empty `main.py`
* Tool parameter validation errors

### MuAPI Integration Issues

* Incorrect PyPI package (`muapi`)
* SDK packaging problems
* Missing command modules
* API key authentication failures

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
Generated Image
      ↓
Returned to Dify
```

Status:

```text
✅ Plugin Packaging
✅ Plugin Installation
✅ Credential Configuration
✅ Image Generation
✅ Image Delivery to Dify
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
