import json
import watson_developer_cloud

tone_analyzer = watson_developer_cloud.ToneAnalyzerV3(
  username='31de6821-051e-4210-82d9-36ccae58ad0c',
  password='mthcTljLh1No',
  version='2016-05-19'
)

def gettone(text):
	tone = tone_analyzer.tone(text, tones='emotion', sentences=False)

	tones = dict()
	for i in tone["document_tone"]["tone_categories"][0]["tones"]:
		tones[i["score"]] = i["tone_name"]
	if max(tones.keys()) > 0:
		return tones[max(tones.keys())]
	else:
		return "No emotion"