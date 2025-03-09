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

Uploading an Agent





---

copyright 2025 by sleet.near
