from app import app
from flask import Flask, request


@app.route('/query_example')
def query_example():
	language = request.args.get('language')
	framework = request.args.get('framework')
	website = request.args.get('website')

	return '''<h1>Language is: {}</h1>'
			<h1>The framework is: {} </h1>
			<h1>The website is: {}</h1>'''.format(language,framework,website)


@app.route('/form_example', methods=['POST', 'GET'])
def form_example():
	if request.method == 'POST':
		language = request.form.get('language')
		framework = request.form['framework']

		return 'The language is {} and the framework is {}'.format(language, framework)

	return '''<form method="POST" action="">
		Language <input type="text" name="language">
		Framework<input type="text" name="framework">
		<input type="submit">
		</form>'''

if __name__ == "__main__":
	app.run(debug=True, port=5000)