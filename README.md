# VIBE YAML

Disclaimer, I am a huge yaml fan but she can be a mess (like me).

Have you ever wondered "well, yaml is a mess but it's not *that* bad, I wish it was actually". 
Did you ever wish you could bring in a bit more enthusiasm when setting values in your config files?
Well, do I have the tool for you. 

Introducing: VIBE YAML.

VIBE YAML runs sentiment analysis on properties in order to determine how truth-y they are! Wanna enable ssh? Hell yeah! 
Gotta open up registration? Nah bestie, but thanks. Rate limit? Yeah I could go for that probably. 

With VIBE YAML you can turn any configuration into an undeterministic nightmare to maintain and use, but fun to read!

## Examples

Have some examples:

```yaml
# example.yml
smtp:
  username: "user"
  password: "secret"
  ssl: I love security, gimme
other:
  test: take it or leave it 
  sure: yeah I am pretty sure I want it
  really: yes, I really want it now gimme
  curse: oh hell yeah sib
```

```python
from vibe_yaml_miawinter import vibe_my_yaml
import json

if __name__ == '__main__':
	with open("example.yml") as example:
		result = vibe_my_yaml(example)
		print(json.dumps(result, indent=2))

```

Which would be interpreted by VIBE YAML as:

```json
{
  "smtp": {
    "username": "user",
    "password": "secret",
    "ssl": true
  },
  "other": {
    "test": "take it or leave it",
    "sure": true,
    "really": true,
    "curse": true
  }
}
```

## Q&A

> Who hurt you?

My Parents.

> Will you find god?

Idk I've been looking all over the place but she just too good at hide and seek.

> Can I use this in prod?

Sure, it's high time to switch careers anyway since IT is fucked and soulcrushing now.

> Can I pet the parser?

Of course. She a good girl, she just a bit ✨special✨.

## How it works

It loads the file via `pyyaml` and then runs a `transformers` pipeline on it 
(`finiteautomata/bertweet-base-sentiment-analysis` to be specific). It then
sees if the score is high enough and if it's labeled as positive/negative and 
re-assigns the value to a boolean.   