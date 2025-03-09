# Agent Registry

Links
- https://docs.near.ai/agents/registry/
- https://app.near.ai/agents

---

**View all agents**
<br/>
To view all agents with nearai CLI, run:

```sh
nearai registry list --category agent
```

**Filtering Agents**
<br/>
You can further filter the agents with two flags:
- --namespace : The developer that created it
- --tags: Any tags that were added to the agent

For example, to find all agents created by gagdiez.near with the tag template, run:

```sh
nearai registry list  --category agent \
                      --namespace gagdiez.near \
                      --tags template \
                      --show_all
```

**Downloading an Agent**
Once you find an agent that you would like to download, use the download command to save it locally. Agent details are passed in the following format:

```sh
nearai registry download <account.near>/<agent_name>/<version>
```
The version can be a specific version number, or latest to download the most recent version.

**Example: Download a hello world agent**
```sh
nearai registry download gagdiez.near/hello-ai/latest
```
This command saves the agent locally in .nearai/registry under your home directory.

The example above would save to: ~/.nearai/registry/gagdiez.near/hello-ai/latest.


---

**Uploading an Agent**
If you created an agent and would like to share it with others, you can upload it to the registry. To upload an agent, you must be logged in.

The upload command requires the path to the agent folder stored locally, for example:

```sh
nearai registry upload ~/.nearai/registry/<your-account.near>/<agent_folder>

# optionally you can run this directly in the folder
nearai registry upload
```

The folder must contain:
- agent.py: Agent logic
- metadata.json: Agent information (ex: description, tags, and model, etc.)

> DANGER: All files in this folder will be uploaded to the registry which is PUBLIC! Make sure you are not including any sensitive data.


---

**Embedding an Agent**
You can embed NEAR AI agents directly into your website using an iframe. This allows users to interact with your agent without leaving your site.
Basic Embedding¶

To embed an agent, use the following iframe code replacing the src with the agent you want to embed.

Example:
```html
<iframe 
  src="https://app.near.ai/embed/<your-account.near>/<your-agent-name>/latest" 
  sandbox="allow-scripts allow-popups allow-same-origin allow-forms"
  style="border: none; height: 100svh;">
</iframe>
```

https://docs.near.ai/agents/registry/#embedding-an-agent

---

copyright 2025 by sleet.near
