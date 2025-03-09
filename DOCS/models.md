# NEAR AI Models Overview

This document provides a comprehensive overview of the available models in the NEAR AI ecosystem, their capabilities, and recommendations for general-purpose use.

## Featured General-Purpose Models

### llama-v3p1-70b-instruct (Default Model)
- **Context Length**: 131,072 tokens
- **Key Features**:
  - Supports chat interactions
  - Tools support
  - Large context window
  - Excellent for general-purpose tasks

### mixtral-8x22b-instruct
- **Context Length**: 65,536 tokens
- **Key Features**:
  - Supports chat interactions
  - Tools support
  - Mixture of Experts architecture
  - Great balance of performance and efficiency

### qwen2p5-72b-instruct
- **Context Length**: 32,768 tokens
- **Key Features**:
  - Supports chat interactions
  - Tools support
  - Strong performance on complex tasks

## Model Categories

### Vision-Capable Models
1. llama-v3p2-90b-vision-instruct
   - Context Length: 131,072 tokens
   - Supports both chat and image input

2. qwen2-vl-72b-instruct
   - Context Length: 32,768 tokens
   - Visual-language capabilities

3. phi-3-vision-128k-instruct
   - Context Length: 32,064 tokens
   - Specialized in vision tasks

### Large Context Models
1. deepseek-r1
   - Context Length: 163,840 tokens
   - Largest context window available

2. qwq-32b
   - Context Length: 131,072 tokens
   - Extended context processing

### Specialized Models
1. llama-guard-3-8b
   - Focused on content moderation
   - Efficient with 131,072 token context

2. qwen2p5-coder-32b-instruct
   - Specialized in coding tasks
   - Large context window (131,072 tokens)

## Model Specifications

### Context Length Categories
- 163,840 tokens: deepseek-r1
- 131,072 tokens: Multiple models including llama-v3p1-70b-instruct
- 65,536 tokens: mixtral-8x22b-instruct
- 32,768 tokens: Several models including qwen2p5-72b-instruct
- 8,192 tokens: Some base llama-v3 models

### Capability Matrix

| Capability | Number of Models |
|------------|-----------------||
| Chat Support | Most models |
| Image Input | 4 models |
| Tools Support | 5 models |

## Usage Recommendations

1. **General Purpose Tasks**
   - Default choice: llama-v3p1-70b-instruct
   - Alternative: mixtral-8x22b-instruct

2. **Vision Tasks**
   - Primary: llama-v3p2-90b-vision-instruct
   - Alternative: qwen2-vl-72b-instruct

3. **Long Context Processing**
   - Primary: deepseek-r1
   - Alternative: llama-v3p1-70b-instruct

4. **Coding Tasks**
   - Recommended: qwen2p5-coder-32b-instruct

## Model Selection Guide

When choosing a model, consider:
1. Task requirements (text, vision, coding)
2. Context length needs
3. Tool support requirements
4. Performance vs efficiency tradeoffs

The default model (llama-v3p1-70b-instruct) is an excellent starting point for most use cases, offering a good balance of capabilities, context length, and performance.