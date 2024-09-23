import database as db
def obtain_session():
  try:
    session = db.get_session()
  except Exception as e:
    #use if you have a logger set up
    #logger.error(f"Error obtaining session: {e}")
    print(f"Error obtaining session: {e}")
    raise
  return next(session)