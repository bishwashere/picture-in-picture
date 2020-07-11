""" Webapp for picture-in-picture

Author: Bishwas

"""
from flask import Flask
app = Flask(__name__)
import sys
from flask import request

@app.route('/<path:url>', methods=['GET'])
def home(url):
	# print(url, file=sys.stderr)
	v = request.args.get('v', None)
	url = url.replace('watch', '')
	if v:
		embed_url = url+'/embed/'+v
	else:
		url_list = url.split('/')
		print(url, file=sys.stderr)
		embed_url = 'https://youtube.com'  + '/embed/'+  url_list[3]
		print(embed_url, file=sys.stderr)
	print(embed_url, file=sys.stderr)
	return '<iframe allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" class="embed-responsive-item" src="%s?modestbranding=1&amp;rel=0&amp;showinfo=0" scrolling="no"></iframe>' % embed_url

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
