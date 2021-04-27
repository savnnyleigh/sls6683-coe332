
  app = Flask(__name__)

  @app.route('/jobs', methods=['POST'])
  def jobs_api():
      try:
          job = request.get_json(force=True)
      except Exception as e:
          return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
      return json.dumps(jobs.add_job(job['start'], job['end']))

  if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0')
