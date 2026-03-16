from vibe_yaml_miawinter import vibe_my_yaml
import json

if __name__ == '__main__':
	with open("src/vibe_yaml_miawinter/example.yml") as content_file:
		content = content_file.read()
		print(content)
	with open("src/vibe_yaml_miawinter/example.yml") as example:
		result = vibe_my_yaml(example)
		print(json.dumps(result, indent=2))
