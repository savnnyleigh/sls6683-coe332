q = HotQueue("queue", host='172.17.0.1', port=6379, db=1)
rd = redis.StrictRedis(host='172.17.0.1', port=6379, db=0)

def _generate_jid():
      return str(uuid.uuid4())

  def _generate_job_key(jid):
      return 'job.{}'.format(jid)

  def _instantiate_job(jid, status, start, end):
      if type(jid) == str:
          return {'id': jid,
                  'status': status,
                  'start': start,
                  'end': end
          }
      return {'id': jid.decode('utf-8'),
              'status': status.decode('utf-8'),
              'start': start.decode('utf-8'),
              'end': end.decode('utf-8')
      }

  def _save_job(job_key, job_dict):
      """Save a job object in the Redis database."""
      rd.hmset(.......)

  def _queue_job(jid):
      """Add a job to the redis queue."""
      ....

  def add_job(start, end, status="submitted"):
      """Add a job to the redis queue."""
      jid = _generate_jid()
      job_dict = _instantiate_job(jid, status, start, end)
      _save_job(......)
      _queue_job(......)
      return job_dict
