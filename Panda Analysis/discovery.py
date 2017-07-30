import json
import watson_developer_cloud

discovery = watson_developer_cloud.DiscoveryV1(
    '2016-11-07',
    username='ca173b9c-3b20-4c97-8f01-10b57e979a2c',
    password='NQJXfxHHbmkg')

def getkey(search):

    query_options = {
             'count' : 0,
             'query': search,
             'return':'aggregation',
             'aggregation':'term(keywords.text,count:5)'
            }
    keywords = discovery.query("cd53de2f-1e40-4dd8-a908-0ccee4456902",
                                    "8febeb2b-3857-4977-aab7-5c7c95f601dd",
                                    query_options)
    key=[]
    for x in keywords["aggregations"][0]["results"]:
        key.append([x["key"],x["matching_results"]])
    return key

def getsent(search):
    query_options = {
             'count' : 0,
             'query': search,
             'return':'aggregation',
             'aggregation':'term(docSentiment.type,count:3)'
            }
    sentiments = discovery.query("cd53de2f-1e40-4dd8-a908-0ccee4456902",
                                    "8febeb2b-3857-4977-aab7-5c7c95f601dd",
                                    query_options)
    sent=[]
    s = 0
    for x in sentiments["aggregations"][0]["results"]:
        sent.append([x["key"],x["matching_results"]])
        s = s + int(x["matching_results"])
    for i in range(3):
      sent[i][1] = float(sent[i][1]/s)*100

    return sent


def getent(search):
    query_options = {
             'count' : 0,
             'query': search,
             'return':'aggregation',
             'aggregation':'term(entities.text,count:5)'
            }
    entities = discovery.query("cd53de2f-1e40-4dd8-a908-0ccee4456902",
                                    "8febeb2b-3857-4977-aab7-5c7c95f601dd",
                                    query_options)
    ent=[]
    for x in entities["aggregations"][0]["results"]:
        ent.append([x["key"],int(x["matching_results"])])
    return ent

def getstor(search):
    query_options = {
      "count": 15,
      "return": "title,enrichedTitle.text,url,host,blekko.chrondate",
      "query": search+",language:english",
      "aggregations": [
        "nested(enrichedTitle.entities).filter(enrichedTitle.entities.type:Company).term(enrichedTitle.entities.text)",
        "nested(enrichedTitle.entities).filter(enrichedTitle.entities.type:Person).term(enrichedTitle.entities.text)",
        "term(enrichedTitle.concepts.text)",
        "term(blekko.basedomain).term(docSentiment.type)",
        "term(docSentiment.type)",
        "min(docSentiment.score)",
        "max(docSentiment.score)",
        "filter(enrichedTitle.entities.type::Company).term(enrichedTitle.entities.text).timeslice(blekko.chrondate,1day).term(docSentiment.type)"
      ],
      "filter": "blekko.hostrank>20,blekko.chrondate>1495218600,blekko.chrondate<1500489000"
      # "sort": "-blekko.chrondate,-_score"
    }
    stories = discovery.query("cd53de2f-1e40-4dd8-a908-0ccee4456902",
                                    "8febeb2b-3857-4977-aab7-5c7c95f601dd",
                                    query_options)
    stor=[]
    for x in stories["results"]:
        stor.append([x["url"],x["host"],x["title"],x["blekko"]["chrondate"]])
    return stor