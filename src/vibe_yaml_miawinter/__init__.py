from yaml import load, dump
try:
	from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
	from yaml import Loader, Dumper

from transformers import pipeline, logging


def vibe_my_yaml(stream, score_cutoff = 0.9):
	logging.disable_progress_bar()
	logging.set_verbosity(logging.FATAL)
	data = load(stream, Loader=Loader)
	pipe = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
	
	def trans(d): # (rights)
		for k, v in d.items():
			if isinstance(v, dict):
				trans(v)
			elif isinstance(v, str):
				sentiment = pipe(v)[0]
				if sentiment["score"] >= score_cutoff and sentiment["label"] != "NEU":
					d[k] = sentiment["label"] == "POS"
			else:
				pass
	trans(data)
	return data
