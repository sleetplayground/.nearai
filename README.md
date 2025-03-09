# ❄️ ~/.nearai
my playground for learning and developing near ai agents

Links:
- https://near.ai/
- https://docs.near.ai/
- https://app.near.ai/
- https://github.com/nearai
- https://github.com/nearai/nearai

![](DOCS/src/sleet_banner_100px_7d84b2.svg)

---

### Installing NEAR AI CLI
https://docs.near.ai/cli/

```sh
python3 -m pip install nearai
```
> near cli may require a certain version of python, but setting up pythin is beyond the scope of this doc, you can learn more about near cli from their offical documentation.

### Login to NEAR AI

```sh
nearai login

# It's probably safe to logout
# so you don't accidently upload something
nearai logout

### Login with NEAR Account ID Only
nearai login --accountId name.near

### Login with Account ID and Private Key
nearai login --accountId name.near --privateKey key
```


### Create an Agent
https://docs.near.ai/agents/quickstart/

```sh
nearai agent create
```

Useful commands to get started interacting with it
```sh
# Run agent locally
nearai agent interactive <path-to-agent> --local

# Select from a list of agents you created to run locally
nearai agent interactive --local

# Upload agent to NEAR AI's public registry
nearai registry upload <path-to-agent>
```


---

### Docs
- [README](DOCS/README.md)
- [models](DOCS/models.md)

registry
- [README](registry/README.md)

py
- [README](py/README.md)


---
![](DOCS/src/sleet_banner_100px_7d84b2.svg)
copyright 2025 by sleet.near